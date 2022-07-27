liste = [5,4,3,15,777,88,999, 1]
liste2 = []
print(enumerate(liste))

for z in range ( len ( liste ) ) :
    maxin = 0
    maxi = liste [ 0 ]
    for i,v in enumerate(liste):
        if maxi < v:
            maxin = i
            maxi = v
    liste [ maxin : maxin + 1 ] = []
    liste2 = [ maxi ] + liste2 
        
        
print(liste2)

