def fibonaccirecursion(i):
   if i <= 1:
       return i
   else:
       return(fibonaccirecursion(i-1) + fibonaccirecursion(i-2))

usernum = int(input("Input Fibonacci numbers request:"))
print(f"Here are the first {usernum} Fibonacci numbers:")
for i in range(usernum):
    print(fibonaccirecursion(i))