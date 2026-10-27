angles = [int(angle) for angle in input().split()]
print("Yes" if sum(angles) == 180 and all(angles) else "No")

