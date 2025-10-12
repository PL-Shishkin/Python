n=int(input("n:"))
if n<0:
    print("ведите неотрицательное число")
else:
    fa=1
    for i in range(1,n+1):
        fa*=i
    print(f"{n}!={fa}")
