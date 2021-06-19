import json
   
t = open('codes.json', 'r', encoding='utf-8')
code_dic = json.load(t)

n = 0
for code in code_dic:
    print(code)
    n += 1
t.close()
