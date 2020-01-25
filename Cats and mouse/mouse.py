q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    dist_a = abs(x-z)
    dist_b = abs(y-z)
    if dist_a < dist_b:
        print("Cat A")
    elif dist_a > dist_b:
        print("Cat B")
    else:
        print("Mouse C")
