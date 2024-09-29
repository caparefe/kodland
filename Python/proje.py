import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("kaça karakterlik bir şifre oluşturmak istersin"))
sifre = ""
for i in range(uzunluk):
    random.choice(karakter)
    sifre = sifre + random.choice(karakter)
print(sifre)