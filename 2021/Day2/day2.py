resp = open("input.txt").readlines()
x=0
y=0
aim=0
for r in range(0, len(resp)):
    cur = resp[r]
    print(x)
    print(y)
    if cur.startswith("forward"):
        diff = int(cur.split(" ")[1])
        x = x + diff
        y = y + aim * diff
        continue
    if cur.startswith("up"):
        aim = aim - int(cur.split(" ")[1])
        continue
    if cur.startswith("down"):
        aim = aim + int(cur.split(" ")[1])
        continue


print(y*x)