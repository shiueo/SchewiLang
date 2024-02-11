import json

with open("KrToSchewiUni.json", "r", encoding="utf8") as f:
    data = json.load(f)

test_str = "바부바부"

res = ""
for word in test_str:
    if word in data.keys() and data[word] != '':
        res += data[word]
    else:
        res += word

print(res)
