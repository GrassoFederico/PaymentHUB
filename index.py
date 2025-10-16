# Importa le dipendenze

import os
from init_database import engine, text

# Stampa il titolo dell'applicativo

print("\n\nPAYMENT HUB\n")

# Inizializza il loop per mostrare a video il menù

loop = True

while loop == True:

    # Stampa tutte le voci del menù

    print("1. Mostra dati")
    print("2. Inserisci dati")
    print("3. Modifica dati")
    print("4. Cancella dati")
    print("5. Esci")

    # Richiede un'opzione

    response = input("\nSeleziona un'opzione e premi invio: ")

    # Pulisce lo schermo

    os.system('cls')

    # Decide cosa fare in base all'opzione scelta

    if response == "1":
        print("Tabelle\n")
        with engine.connect() as connection:
            result = connection.execute(text('SHOW TABLES'))
            
            i = 1
            for single_result in result:
                print(str(i) + ". " + single_result[0])
                i = i + 1
    elif response == "2":
        print("Inserisco i dati")
    elif response == "3":
        print("Modifico i dati")
    elif response == "4":
        print("Cancello i dati")
    elif response == "5":
        # Se esce interrompe la condizione del ciclo ed esce direttamente dal ciclo
        loop = False
        break
    else:
        print("Opzione non valida, riprova")

    # Se l'utente decide di non uscire dal software mostro le informazioni richieste

    response = input("\nTorna al menù [Invio] ")
        
    os.system('cls')

# Saluta

print("\nBye\n")