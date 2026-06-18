D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

D[6] = "Six"
print("After adding key 6:", D)

del D[2]
print("After removing key 2:", D)

if 6 in D:
    print("Key 6 is present")
else:
    print("Key 6 is not present")

print("Number of elements =", len(D))

print("All values:")
for value in D.values():
    print(value)
