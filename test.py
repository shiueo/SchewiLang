import json

with open("KrToSchewiUni.json", "r", encoding="utf8") as f:
    data = json.load(f)

test_str = "단단 오치테쿠 아이큐우 쿠소와로 / 칸젠타이노 야마다 / 무칸신난테 아리에나이 / 산젠타이노 쿠와타노 호오가 이이카나 / 와가마마바카리자 오치츠카나이"

res = ""
for word in test_str:
    if word in data.keys() and data[word] != '':
        res += data[word]
    else:
        res += word

print(res)
