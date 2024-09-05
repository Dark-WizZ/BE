d = {21: "car", 27: "bike", 90: "plane"}
k = int(input("Enter the key to search: "))
if k in d.keys():
    print(f"value = {d[k]}")
else:
    print("key doesn't exist")
