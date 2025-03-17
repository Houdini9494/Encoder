import hashlib
import os
import secrets
#---------------------------------------------------------------------------
#funzione x convertire decimali in binario
def conv_base(numero,nuova_base):
    if numero == 0:
        return [0]
    risultato=[]
    while numero>0:
        resto=numero%nuova_base
        risultato.append(resto)
        numero//=nuova_base
    risultato.reverse()
    return risultato
#---------------------------------------------------------------------------
#funzione di conversione da stringa a binario
def str_to_bin(stringa):
    # converte una stringa in una lista di numeri usando la tabella ASCII
    stringa_ascii=[]
    for i in stringa:
        stringa_ascii.append(ord(i))

    # converte ogni numero della lista in binario
    stringa_binario=[]
    for i in stringa_ascii:
        # map() applica la funzione str() ad ogni elemento della lista restituita dalla funz. conv_base(), quindi converte tutti gli int a str
        # "".join() unisce tutti gli elem. della lista di stringhe prodotta da map() in una unica stringa senza spazi e senza virgole di separazione
        stringa_binario.append("".join(map(str,conv_base(i,2))))

    # formatta il risultato unendo le liste di valori binari; ogni lettera è una lista binaria quindi devono essere unite tutte in una stringa unica
    risultato="".join(stringa_binario)
    return risultato
#---------------------------------------------------------------------------
#funzione x hashare l'seed
def hashing(seed):
    digest=hashlib.sha3_512((seed).encode()).hexdigest() #hexdigest() restituisce il digest in un formato esadecimale piu facilemnte leggibile
    return digest
#---------------------------------------------------------------------------
#funzione genera psw
def genera_psw(seed,lunghezza):
    iterazioni=1000 #numero di iterazioni di hashing per generare entropia
    sale=os.urandom(32).hex() #un pizzico di sale per aggiungere sicurezza
    pepe="-.,<_:;>°#@+*]€['^?=)(/&%$£!|\\"

    #hash iterativo dell'input
    digest=seed+sale
    for i in range(iterazioni):
        digest=hashlib.sha3_512((digest+sale).encode()).hexdigest()

    #mixer di caratteri alfanumerici e simboli
    mix=[]
    for i in range(lunghezza):
        if i%2==0:
            mix.append(secrets.choice(digest))
        else:
            mix.append(secrets.choice(pepe))

    #sostituzione dei caratteri uguali consecutivi
    for e in range(len(mix)-1):
        if mix[e]==mix[e+1]:
            if mix[e+1] in digest:
                mix[e+1]=secrets.choice(digest)
            else:
                mix[e+1]=secrets.choice(pepe)

    return "".join(mix)

#-----------------------------------------------------------
# menu
def menu():
    opzioni={
        1:"Converti stringa in binario",
        2:"Calcola hash di una stringa",
        3:"Genera psw",
        4:"Esci dal programma"
    }
    print("\n--------ENCODER--------\n")
    print("\tMENU")
    for k,v in opzioni.items():
        print(f"{k}-{v}")
    print("\n-----------------------\n")
#---------------------------------------------------------------------------
