usernum = int(input("Input Fibonacci numbers request:"))

fibnum0 = 0
fibnum1 = 0
fibnum2 = 1

print(f"Here are the first {usernum} Fibonacci numbers:")

for idx in range(usernum):
    print (fibnum1)
    fibnum0 = fibnum1 + fibnum2
    fibnum1 = fibnum2
    fibnum2 = fibnum0