import re
import itertools as it
def isprime(n):
    for i in range(2 , (n//2 + 1)):
        if n%i == 0:
            return False
    return True


def fibbo(lis1 = [] , count = None):
    for i in range(2,count):
        lis1.append(lis1[-1] + lis1[-2])
    return lis1[-1]

nums = input()
nums = re.findall('[0-9]+' , nums)

fl = [i for i in range(int(nums[0]) , int(nums[1]) + 1) if isprime(i)]

sl = []
for a,b in it.permutations(fl , r= 2):
    sl.append(
        int( str(a)+str(b) )
    )


sl = list(set(sl))
sl = list(filter(lambda x : isprime(x) , sl))
sl = sorted(sl)
fb = []
fb.append(sl[0])
fb.append(sl[-1])
print(fibbo(fb , len(sl)))


    