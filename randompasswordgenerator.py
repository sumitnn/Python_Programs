import random


n = int(input("enter password length"))
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*()[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
res = "".join(random.sample((characters), k=n))

print(f"Your {n} length password is {res}")
