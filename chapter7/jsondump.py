import json
x = json.dumps([1, 'simple', 'list'])
print(x)
with open('jsondump.txt', 'w+') as f:
    json.dump(x,f)

with open('jsondump.txt', 'r') as f1:
    c = json.load(f1)
    print(c)