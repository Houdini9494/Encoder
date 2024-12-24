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
try:
    while True:
        nome=input("Inserire la stringa da convertire in binario: ").strip().lower()

        # converte il nome in una lista di numeri ASCII
        stringa_ascii=[]
        for i in nome:
            stringa_ascii.append(ord(i))

        # converte ogni numero ASCII in binario
        stringa_binario=[]
        for i in stringa_ascii:
            # map() applica la funzione str() ad ogni elemento della lista restituita dalla funz. conv_base(), quindi converte tutti gli int a str
            # "".join() unisce tutti gli elem. della lista di stringhe prodotta da map() in una unica stringa senza spazi e senza virgole di separazione
            stringa_binario.append("".join(map(str,conv_base(i,2))))

        # formatta il risultato unendo le liste di valori binari; ogni lettera è una lista binaria
        risultato="".join(stringa_binario)

        # stampa risultato contenuto nella lista
        print(f"il nome '{nome}', in binario equivale a: {risultato}")

        # iterazione per inserimento di un nuovo nome
        scelta=input("\nVuoi convertire un altro nome? (y/n): ").strip().lower()
        if scelta=="n":
            print("Esco dal programma...")
            break
except:
    print("Si è verificato un errore, riavviare il programma.")
