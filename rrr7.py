DIM = 28

TAB= ['E','S','O','P','E',' ','R','E','S','T','E',' ','I','C','I',' ','E','T',' ','S','E',' ','R','E','P','O','S','E']
TAB2 = ['k','p']

def pali():
    BIS = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    for n in range(0,DIM):
        if TAB[(DIM-1)-n] != ' ':
            BIS[n] = TAB[(DIM-1)-n]
    n = 0
    res = 1
    if n < DIM-1-n:
        if BIS[n] != BIS[DIM-1-n]:
            res = 0
        n = n + 1
    if res == 1:
        print('OUI')
    print(BIS, res)


    
def qq():
    c = ''
    for n in range(0,2):
        if n < 2-1-n:
            c = TAB2[n]
            TAB2[n] = TAB2[len(TAB2)-n-1]
            TAB2[len(TAB2)-n-1] = c
    print(TAB2)

def tt(self):
    nb = 1
    for n in range(0,len(self)):
        if self[n] == ' ':
            nb = nb + 1
    print(nb)

def te(self,mot):
    nb = 1
    poit = 0
    l = 1
    for n in range(0,len(self)):
        if self[n] == ' ':
            l = 0
            nb = nb + 1
        if nb == mot and l == 0 and self[n] != ' ' :
            l = 1
            poit = n + 1
            print(poit)
