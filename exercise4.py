quad_zahl=[] #leere Liste
for zahl in range(1,11):
    if zahl%2 ==0:
        quad_zahl.append(zahl)
    else:
        quad_zahl.append(zahl**2)
print(quad_zahl)
    


quad_zahl_neu= [k if k%2 == 0 else k**2 for k in range (1, 11)]

print (quad_zahl_neu)
