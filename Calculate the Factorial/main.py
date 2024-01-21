usernum = int(input("Input number for Factoral Calculation:"))
curval = usernum
factnum = usernum
while curval > 1:
    curval-=1
    factnum*=curval

print(f"The Factoral of {usernum} is {factnum}")