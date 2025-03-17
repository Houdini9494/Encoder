import funzioni
import traceback

def main():
    try:
        while True:
            funzioni.menu()
            scelta=input("Scegli l'operazione da eseguire (1, 2, 3...): ")
            if scelta.isdigit():
                scelta=int(scelta)
                if 1<= scelta <= 4:
                    if scelta==1:
                        stringa=input("Inserisci una stringa: ").strip().lower()
                        # stampa risultato contenuto nella lista
                        print(f"la stringa '{stringa}', in binario equivale a: {funzioni.str_to_bin(stringa)}")
                    elif scelta==2:
                        stringa=input("Inserisci una stringa: ").strip()
                        # calcolo hash
                        print(f"l'hash sha512 di '{stringa}' è: {funzioni.hashing(stringa)}")
                    elif scelta==3:
                        while True:
                            stringa=input("Inserisci una stringa di caratteri: ")
                            if not stringa:
                                print("La stringa non può essere vuota!")
                            else:
                                break
                        while True:
                            lunghezza=input("Inserisci la lunghezza della psw da generare: ")
                            if lunghezza.isdigit():
                                lunghezza=int(lunghezza)
                                if lunghezza<8:
                                    print("Inserito valore non valido, selezionare un minimo 8 caratteri.")
                                else:
                                    try:
                                        password=funzioni.genera_psw(stringa,lunghezza)
                                        print(f"\n{password}")
                                        break
                                    except Exception as e:
                                        print(f"si è verificato un errore: {e}")
                                        break
                            else:
                                print("Inserita lungheza non valida, digitare un numero intero.")
                    elif scelta==4:
                        print("Esco dal programma...")
                        break
                else:
                    print("Scelta non valida.")
            else:
                print("Input non valido, inserire un numero.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
#--------------------------------------
if __name__ == "__main__":
    main()
