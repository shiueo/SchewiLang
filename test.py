import json

with open("KrToSchewiUni.json", "r", encoding="utf8") as f:
    data = json.load(f)

test_str = "즈에 이이카 아이로 오넨네시다네"

res = ""
for word in test_str:
    if word in data.keys() and data[word] != '':
        res += data[word]
    else:
        res += word

print(res)
