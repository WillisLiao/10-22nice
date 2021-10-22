import random as rand
n=int(input())
rand.seed(n)
for i in range(6):
    print(rand.randrange(42),end="\t")
