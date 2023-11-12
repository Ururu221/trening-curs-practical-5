import math
print ("4 варіант")
k1 = int(input("катет: "))
a = int(input("кут протилежного кута: "))
print ("")
k2 = round(k1 / math.sin(a), 1)
k3 = round(k1 / math.tan(a), 1)
P = k1 + k2 + k3
a2 = 90 - a
h = 0.5 * P
s = round(math.sqrt(h * (h - k1) * (h - k2) * (h - k3)), 1)
print ("сторони прямокутника: ", k1, k2, k3)
print ("периметр: ", P)
print ("кути: 90", a, a2)
print ("площа: ", s)