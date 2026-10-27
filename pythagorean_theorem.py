side_a = int(input())
side_b = int(input())
side_c = int(input())
sides = sorted([side_a, side_b, side_c])
print("Yes" if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 else "No")


