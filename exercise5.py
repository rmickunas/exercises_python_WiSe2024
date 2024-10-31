import matplotlib.pyplot as plt

s_n=[]
r = 0.5
a = 1
n = 10
summe=0

for k in range(n):
    summe += a*r**k
    s_n.append(summe)

s_nsum = sum(s_n)
print(s_n)


plt.plot(s_n)
