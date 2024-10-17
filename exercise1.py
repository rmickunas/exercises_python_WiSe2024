P=100
t=10
i=0.03
A=P*(1+i)**t
print(A)

P=1
t=1
i=1
n=365*24*60
A=P*(1+i/n)**(n*t)
print(A)