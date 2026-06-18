L = [10, 20, 30, 40, 50, 60, 70, 80]

L.append(200)
L.append(300)
print("After adding 200 and 300:", L)

L.remove(10)
L.remove(30)
print("After removing 10 and 30:", L)

L.sort()
print("Ascending order:", L)

L.sort(reverse=True)
print("Descending order:", L)
