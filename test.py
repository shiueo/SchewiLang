import json

with open("KrToSchewiUni.json", "r", encoding="utf8") as f:
    data = json.load(f)

test_str = "단단 오치테쿠 아이큐우 쿠소와로 칸젠타이노 야마다"

res = ""
for word in test_str:
    if word in data.keys() and data[word] != '':
        res += data[word]
    else:
        res += word

print(res)
