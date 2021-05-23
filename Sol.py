from sys import stdin
from sys import stdout

def primefactor(n):
    if n<=9:
        print('Invalid number')
    else:
            flag=False
            for i in range(3, int(n/2),2):
                if (n % i) == 0:
                    # print(n%i)
                    flag = True
                    break
            if flag!=True:
                print('Invalid Number')
            else:
                mul=1
                pf=[]
                for i in range(2,int(n/2)):
                    if n%i==0:
                        pf.append(i)
                        mul*=i
                pf.sort(reverse=True)
                print(pf)
                print(mul)

n=int(stdin.readline())
primefactor(n)
