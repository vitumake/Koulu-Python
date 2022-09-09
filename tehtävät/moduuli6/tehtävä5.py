import random
def delOddN(arr):
    for i in arr:
        if i%2!=0: arr.remove(i)
    return arr
testArr=[]
for i in range(10):
    testArr.append(random.randint(0, 100))
print(f'Alkuperäinen lista: {testArr}\n Listan parilliset numerot: {delOddN(testArr)}')