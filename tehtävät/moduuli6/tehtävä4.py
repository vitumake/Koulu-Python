import random
def sumArr(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
testArr=[]
for i in range(10):
    testArr.append(random.randint(0, 100))
print(sumArr(testArr))