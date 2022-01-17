'''
Question – :  Some prime numbers can be expressed as a sum of other consecutive prime numbers.

For example
5 = 2 + 3,
17 = 2 + 3 + 5 + 7,
41 = 2 + 3 + 5 + 7 + 11 + 13.
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Constraints: 2<N<=12,000,000,000
'''

def factor(n):
    count = 0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        return True
    return False
# Method 1
def total(num):
    l=[i for i in range(2,num+1) if factor(i)]
    count = 0
    for n in range(len(l)):
        i = 0
        x = 0
        while i<n:
            x+=l[i]
            if x == l[n]:
                count+=1
                break
            else:
                i+=1
    return count
# Method2
def total(num):
    l = [i for i in range(2, num + 1) if factor(i)]
    count = 0
    sum = 2
    for n in range(1, len(l)):
        sum += l[n]
        if sum in l:
            count +=1
    return count

print(total(50))
