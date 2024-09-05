marks = {
    "Alibaba": [80, 60, 77],
    "Ben": [63, 98, 76],
    "Drag": [99, 76, 54],
    "Peter": [98, 69, 55],
    "Luis": [87, 67, 59],
}

for k, v in marks.items():
    print(k, " => ", round(sum(v) / len(v), 2))
