import json

with open("KrToSchewiUni.json", "r", encoding="utf8") as f:
    data = json.load(f)

print(f"Key num = {len(data.keys())}\nVal num = {len(set(data.values()))}")