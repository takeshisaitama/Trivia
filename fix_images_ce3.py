import json

with open("Simulados Aguia/01/TI/conhecimentos_especificos_3.json", "r", encoding="utf-8") as f:
    deck3 = json.load(f)

# Update paths and replace text tables with images
base_path = "C:/Users/ACER/Documents/GitHub/Trivia/Simulados Aguia/01/Conhecimentos Específicos/IMG/"

for card in deck3["cards"]:
    if card["id"] == "ti_ce3_q120":
        # Q120 already has an image tag, let's just make sure the path is exactly as provided with forward slashes
        img_tag = f"{{{{img:{base_path}Q120.png|100%|Tabela Transacional}}}}"
        # It was already added in my previous script roughly like this. Let's ensure it's exact.
        if "{{img:" in card["front"]:
            import re
            card["front"] = re.sub(r"\{\{img:.*?\}\}", img_tag, card["front"])

    elif card["id"] == "ti_ce3_q126":
        # Q126 had a text table
        table_text = "**Origem -> Destino**\n`stg_notas -> dw_fato_notas`\n`stg_contrib -> dw_dim_contrib`\n`dw_dim_contrib -> mart_arrecadacao`\n`dw_dim_contrib -> mart_fiscalizacao`\n`mart_arrecadacao -> painel_arrecadacao`\n`mart_arrecadacao -> modelo_risco`\n`mart_fiscalizacao -> painel_risco`\n`modelo_risco -> painel_risco`\n\n"
        img_tag = f"{{{{img:{base_path}Q126.png|100%|Tabela de Linhagem}}}}\n\n"
        card["front"] = card["front"].replace(table_text, img_tag)

    elif card["id"] == "ti_ce3_q128":
        # Q128 had a text table
        table_text = "`uf  qtd preco`\n`SC  1   18`\n`SC  6   12`\n`PR  2   25`\n`PR  3   10`\n\n"
        img_tag = f"{{{{img:{base_path}Q128.png|100%|Tabela Vendas}}}}\n\n"
        card["front"] = card["front"].replace(table_text, img_tag)

    elif card["id"] == "ti_ce3_q132":
        # Q132 had a text table
        table_text = "`F1: 120 | F2: 700 | F3: 40 | F4: 300 | F5: 15 | F6: 160 | F7: 500 | F8: 60 | F9: 25 | F10: 80`\n\n"
        img_tag = f"{{{{img:{base_path}Q132.png|100%|Tabela Fornecedores}}}}\n\n"
        card["front"] = card["front"].replace(table_text, img_tag)

with open("Simulados Aguia/01/TI/conhecimentos_especificos_3.json", "w", encoding="utf-8") as f:
    json.dump(deck3, f, ensure_ascii=False, indent=2)

print("Imagens do CE3 ajustadas!")
