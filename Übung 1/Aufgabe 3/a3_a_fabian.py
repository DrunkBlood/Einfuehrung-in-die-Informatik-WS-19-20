x = int(input('x'))
y = int(input("y"))
z = int(input("z"))
xy = x * 60 + y
xy: int = z - xy

if xy < 0: xy = xy + 24 * 60
print(str(xy // 60) + ":" + str(xy // 60))
if xy % 60 < 10:
    a = "0" + str(xy % 60)
else:
    a = str(xy % 60)
if xy // 60 < 10:
    b = "0" + str(xy // 60)
else:
    b = str(xy // 60)
print("(i)" + a + ":" + b)

# Boarding

xy -= 30
if xy < 0: xy += 24 * 60
if xy // 60 < 10:
    a = "0" + str(xy // 60)
else:
    a = str(xy // 60)
if xy % 60 < 10:
    b = "0" + str(xy % 60)
else:
    b = str(xy % 60)
print("(ii)" + a + ":" + b)
