def phrase():
    global sentence
    sentence = input("Lettre : ")
def final():
    global sentence
    print(str(sentence),end=" ;) ")
def quitter():
    global qrun
    qrun = input("\nVoullez vous quitter ? : ")
def vérification():
    global qrun, ruun, runn2, run
    if qrun in ruun:
        run = 0
    if qrun in runn2:
        pass
    if not qrun in ruun and not qrun in runn2:
        print("Veuliez taper une réponse juste...\n")
        quitter()
        vérification()
    
run = 1

ruun = ["Oui","oui","o","O"]
runn2 = ["Non","non","n","N"]

while run:
    
    phrase()


    if len(sentence) > 1:
        print("Erreur : vous n'avez pas rentré une lettre")
        
    if len(sentence) == 1:
        final()
        comp2 = 0
        quitter()
        vérification()



