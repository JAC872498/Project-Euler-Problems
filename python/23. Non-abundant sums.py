"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

#Is this a non-optimal solution? Absolutely
#Did it take too long to run? Absolutely
#Could it be improved and optimised? Absolutely
#Was it fun to build and mess around with? Absolutely

def a(n):
    t=0
    for x in range(n-1):
        if(n%(x+1)==0):
            t+=x+1
            if(t>n): return True
    return False

def g(g):
    for n in range(g):
        if(a(n+1) and a(g-n-1)): return False
    return True
    
t=0
for n in range(20161):
    if(g(n+1)): t+=n+1
print(t)
