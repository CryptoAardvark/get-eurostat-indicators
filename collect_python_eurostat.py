import eurostat
import json

# Fetch the table of contents

toc = eurostat.get_toc()
print(len(toc[1]))
print(toc[1])
# Extract relevant fields from each indicator
indicators = []
for item in toc:
    indicator = {
        'indicator': item[1],
        'description': item[0],
        'label': item[0],
        'target': "eurostat"
    }
    indicators.append(indicator)

# Save the extracted data to a JSON file
output_file = "indicators1.json"
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(indicators, json_file, indent=4, ensure_ascii=False)

print(f"Indicators saved to {output_file}")