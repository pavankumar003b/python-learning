#python program ,find factorialof a number provided by the uses
num=14
factorial = 1
if num < 0:
    print('factorial does not exist for negative numbe')
elif num==0:
    print('the factorial of 0 is 1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print('the factorial is',num,factorial)
