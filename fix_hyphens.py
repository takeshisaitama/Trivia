import json
import re

with open("Simulados Aguia/01/TI/conhecimentos_especificos_4.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for card in data["cards"]:
    if "back" in card:
        back = card["back"]

        # Remove hyphens before bold subitems in Teoria
        lines = back.split("\n")
        new_lines = []
        for line in lines:
            stripped = line.lstrip()
            # If it starts with a hyphen and then a bold, remove the hyphen.
            if stripped.startswith("- **"):
                # Handle cases like "- **Title:**"
                new_line = line.replace("- **", "**", 1)
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        card["back"] = "\n".join(new_lines)

with open("Simulados Aguia/01/TI/conhecimentos_especificos_4.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Hyphens removed successfully!")