import numpy as np

#funzione x convertire decimali in binario
def conv_base(numero_iniz,nuova_base):

    numero=numero_iniz
    risultato=[]

    while numero>0:
        resto=numero%nuova_base
        risultato.append(resto)
        numero=numero//nuova_base

    risultato.reverse()
    array=np.array(risultato)
    return array

#---------------------------------------------------------------------------
letters="abcdefghijklmnopqrstuvwxyz"

nome=input("Inserire il nome da convertire in binario: ")
flag=True

while flag:
    #converte lettere in numeri
    nome_numero=[]
    corretto=True #verifica se il nome contiene SOLO lettere dell'alfabeto
    for i in nome.lower():
        if i in letters:
            nome_numero.append(letters.index(i)+1)
        else:
            corretto=False

    #se il nome inserito è corretto procede con la conversione
    if corretto:
        #converte numeri decimali in binario
        risultato=[]
        for n in nome_numero:
            risultato.append(conv_base(n,2))

        #stampa risultato contenuto nella lista
        print("il nome",nome,"in binario è: ")
        for i in risultato:
            print(str(i).strip("[]"), end=" ") #per stampare tutto il resto ma senza le parentesi quadre
    else:
        print("Nome inserito non valido per presenza di numeri, caratteri speciali o lettere sconosciute...")

    #iterazione per inserimento di un nuovo nome
    scelta=input("\nVuoi convertire un altro nome? (y/n): ")
    if scelta=="n":
        print("Esco dal programma...")
        flag=False
    else:
        nome=input("Inserire il nome da convertire in binario: ")

