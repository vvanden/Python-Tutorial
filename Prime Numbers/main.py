usernum = int(input("Display request for prime numbers below:"))
worknum = usernum
divisor = 2
if usernum < divisor:
    print("If the number 0 or 1, it is not a prime number.")
    exit()
else:
    while worknum > 2:
        while divisor <= worknum:
            if (worknum == divisor):
                if (worknum == usernum):
                    print(worknum)
                else:
                    print(worknum)
                break
            elif (worknum % divisor) == 0:
                break
            else:
                divisor+=1
        worknum-=1
        divisor=2
print(worknum)