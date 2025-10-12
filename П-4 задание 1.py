A=int(input("A:"))
B=int(input("B:"))
if A<=B:
    for i in range(A,B+1):
        print(i,end=" ")
else:
    print("A должно быть больше B")
