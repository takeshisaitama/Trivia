import json
import re

with open("Simulados Aguia/01/TI/conhecimentos_especificos_4.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for card in data["cards"]:
    if "back" in card:
        back = card["back"]
        # Replace **> CERTO <** followed by multiple newlines with just one newline
        back = re.sub(r"(\*\*> CERTO <\*\*)\n+", r"\1\n", back)
        # Replace **> ERRADO <** followed by multiple newlines with just one newline
        back = re.sub(r"(\*\*> ERRADO <\*\*)\n+", r"\1\n", back)

        card["back"] = back

with open("Simulados Aguia/01/TI/conhecimentos_especificos_4.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Formatting applied successfully!")