#funzione x convertire decimali in binario
def conv_base(numero,nuova_base):
    risultato=[]
    while numero>0:
        resto=numero%nuova_base
        risultato.append(resto)
        numero//=nuova_base
    risultato.reverse()
    return risultato

#---------------------------------------------------------------------------
while True:
    nome=input("Inserire il nome da convertire in binario: ").strip().lower()

    # converte il nome in una lista di numeri ASCII
    nome_ascii=[]
    for i in nome:
        nome_ascii.append(ord(i))

    # converte ogni numero ASCII in binario
    nome_binario=[]
    for i in nome_ascii:
        # map() applica la funzione str() ad ogni elemento della lista restituita dalla funz. conv_base(), quindi converte tutti gli int a str
        # "".join() unisce tutti gli elem. della lista di stringhe prodotta da map() in una unica stringa senza spazi e senza virgole di separazione
        nome_binario.append("".join(map(str,conv_base(i,2))))

    # formatta il risultato unendo le liste di valori binari; ogni lettera è una lista binaria
    risultato="".join(nome_binario)

    # stampa risultato contenuto nella lista
    print(f"il nome '{nome}', in binario equivale a: {risultato}")

    # iterazione per inserimento di un nuovo nome
    scelta=input("\nVuoi convertire un altro nome? (y/n): ").strip().lower()
    if scelta=="n":
        print("Esco dal programma...")
        break
