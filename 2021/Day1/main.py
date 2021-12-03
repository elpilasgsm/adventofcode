resp = open("input.txt").readlines()
cur = None
prev = None
count = 0
for r in range(0, len(resp) - 2):
    cur = int(resp[r]) + int(resp[r+1]) +int(resp[r+2])
    if prev == None:
        prev = cur
        continue

    if cur - prev > 0:
        count = count + 1
    prev = cur
print(count)
