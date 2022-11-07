import random
import time
n=0
N=int(input('Anna testattavien pistiden määrä: '))
ts=time.time()
for i in range(N):
    if pow(random.uniform(-1, 1), 2) + pow(random.uniform(-1, 1), 2) < 1:
        n+=1
print(f"Pi:n likiarvo on: {4*n/N} Ajassa {round(time.time() - ts, 3)}s")