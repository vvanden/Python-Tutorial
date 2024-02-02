def factorrecursion(i):
   if i == 1:
       return i
   else:
       return i*factorrecursion(i-1)

usernum = int(input("Input number for Factoral Calculation:"))
factnum = factorrecursion(usernum)
print(f"The Factoral of {usernum} is {factnum}")