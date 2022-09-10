import random
def delOddN(arr):
    evenArr=[]
    for i in arr:
        if i%2==0: evenArr.append(i)
    return evenArr
testArr=[]
for i in range(10):
    testArr.append(random.randint(0, 100))
print(f'Alkuperäinen lista: {testArr}\n Listan parilliset numerot: {delOddN(testArr)}')