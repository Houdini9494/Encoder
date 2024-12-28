import hashlib
import os
import random
import traceback
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
#funzione x hashare l'input
def hashing(input):
    hash=hashlib.sha3_512((input).encode()).hexdigest() #hexdigest() restituisce il digest in un formato esadecimale piu facilemnte leggibile
    return hash
#---------------------------------------------------------------------------
#funzione genera psw
def genera_psw(input,lunghezza):
    iterazioni=1000 #numero di iterazioni di hashing per generare entropia
    sale=os.urandom(32).hex() #un pizzico di sale per aggiungere sicurezza
    pepe="-.,<_:;>°#@+*]€['^?=)(/&%$£!|\\"

    #hash iterativo dell'input
    hash=input+sale
    for i in range(iterazioni):
        hash=hashlib.sha3_512((hash+sale).encode()).hexdigest()

    #mixer di caratteri alfanumerici e simboli
    mix=[]
    for i in range(lunghezza):
        if i%2==0:
            mix.append(random.choice(hash))
        else:
            mix.append(random.choice(pepe))

    return "".join(mix)

#-----------------------------------------------------------
# menu
def menu():
    opzioni={
        1:"Converti stringa in binario",
        2:"Calcola hash di una stringa",
        3:"Genera psw sicura",
        4:"Esci dal programma"
    }
    print("\n--------ENCODER--------\n")
    print("\tMENU")
    for k,v in opzioni.items():
        print(f"{k}-{v}")
    print("\n-----------------------\n")
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def main():
    try:
        menu()
        while True:
            scelta=int(input("Scegli l'operazione da eseguire (1, 2, 3...): "))
            while scelta<1 or scelta>3:
                print("Inserita scelta errata!")
                scelta=int(input("\nScegli l'operazione da eseguire (1, 2, 3...): "))

            if scelta==1:
                stringa=input("Inserisci una stringa: ").strip().lower()
                print(f"la stringa '{stringa}', in binario equivale a: {str_to_bin(stringa)}")
            elif scelta==2:
                stringa=input("Inserisci una stringa: ").strip()
                print(f"l'hash sha512 di '{stringa}' è: {hashing(stringa)}")
            elif scelta==3:
                stringa=input("Inserisci una stringa di caratteri: ")
                lunghezza=int(input("Inserisci la lunghezza della psw da generare: "))
                while lunghezza<=8:
                    lunghezza=int(input("Inserito valore errato, consigliato un minimo di 8 caratteri: "))
                print(f"\n{genera_psw(stringa,lunghezza)}")
            elif scelta==4:
                print("Esco dal programma...")
                break
            else:
                print("Inserita scelta errata.")
                break
            menu()
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
#---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
