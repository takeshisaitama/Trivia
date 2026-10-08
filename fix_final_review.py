import json
import re

with open('/app/Simulados Aguia/01/Exatas/Exatas 01.json', 'r', encoding='utf-8') as f:
    deck = json.load(f)

# If deck is a dictionary containing a list, get the list
if isinstance(deck, dict) and "cards" in deck:
    cards = deck["cards"]
elif isinstance(deck, dict):
    # What is the format? Let's check keys
    print("Keys in deck:", deck.keys())
    cards = []
else:
    cards = deck

for card in cards:
    if not isinstance(card, dict):
        continue

    if card.get('id') == 'boss_tutorial':
        back = card.get('back', '')

        back = re.sub(r'(- \*\*Como aparece\*\*:) (.+)', r'\1\n\2', back)
        back = re.sub(r'(- \*\*Pegadinha\*\*:) (.+)', r'\1\n\2', back)
        back = re.sub(r'(- \*\*Decisão\*\*:) (.+)', r'\1\n\2', back)

        card['back'] = back

    if card.get('id') == 'sefaz_sc_01_exatas_q30':
        front_text = card.get('front', '')

        statements = []
        pattern = r'\(\s*\) (.*?)\n'
        for match in re.finditer(pattern, front_text):
            statements.append("vf(" + match.group(1).strip() + ")")

        front_text = re.sub(r'\(\s*\) .*?\n', '', front_text)

        card['stem'] = statements
        card['front'] = front_text.strip()

        back = card.get('back', '')

        back = back.replace('- **1ª afirmação (V).** ', '**1ª afirmação (V).**\n**> CERTO <**\n')
        back = back.replace('- **2ª afirmação (V).** ', '**2ª afirmação (V).**\n**> CERTO <**\n')
        back = back.replace('- **3ª afirmação (F).** ', '**3ª afirmação (F).**\n**> ERRADO <**\n')
        back = back.replace('- **4ª afirmação (F).** ', '**4ª afirmação (F).**\n**> ERRADO <**\n')

        card['back'] = back

with open('/app/Simulados Aguia/01/Exatas/Exatas 01.json', 'w', encoding='utf-8') as f:
    json.dump(deck, f, ensure_ascii=False, indent=2)

print("Fixes applied.")
