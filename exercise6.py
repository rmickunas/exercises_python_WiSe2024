a=1
r=0.5
s=0
k=0

limit = (a/(1-r))
epsilon = 0.001


while True:
    s+=a*r**k
    k+=1 
    print(s, end = " ")
    
    #if s==(a/(1-r)):
    #   break
    
    if(limit-s)<epsilon:
        break