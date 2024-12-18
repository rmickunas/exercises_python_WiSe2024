import matplotlib.pyplot as plt 

def buchstaben_häufigkeit(x):
    mein_d = {} #Dictionary not a list
    
    for b in x.lower():
        if b.isalpha():
            if b not in mein_d:
                mein_d[b] = 1
            else:
                mein_d[b] += 1
                
    mein_b_sorted = dict(sorted(mein_d.items()))
    
    return mein_b_sorted

bh_dict1 = buchstaben_häufigkeit(x= "123wie geht es Ihnen%$?")

plt.bar(bh_dict1.keys(), bh_dict1.values())
