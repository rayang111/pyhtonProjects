tab = [10,8,2,23,1,0,15,16,10,14,9,5]
def R(self,Max,Mini,Maxi):
    Maxi = tab[0]
    Mini = tab[0]

    for n in range(1,Max-1):
        if Maxi < tab[n+1]:
            Maxi = tab[n+1]
        if Mini > tab[n+1]:
            Mini = tab[n+1]

    print(Mini,Maxi)
