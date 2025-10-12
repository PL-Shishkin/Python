a=int(input())
if a%3==0 and a%5==0:
    print(a,"число кратно 3 и 5")
elif a%3==0:
    print(a,"число кратно 3")
elif a%5==0:
    print(a,"число кратно 5")
else:
    print(a,"исло не кратно 3 и 5")
