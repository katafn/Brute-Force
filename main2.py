import json
from brute_force2 import BruteForce

def load_config(config_file):
    """Carica la configurazione da un file JSON."""
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("[ERROR] File di configurazione non trovato!")
        exit(1)
    except json.JSONDecodeError:
        print("[ERROR] Errore nel parsing del file di configurazione!")
        exit(1)

def main():
    config_file = "brute force/config.json"
    config = load_config(config_file)

    server = config.get("server")
    password_file = config.get("password_file")
    user_file = config.get("user_file")

    # Chiedi all'utente se conosce il nome utente
    username_known = input("[INFO] Conosci il nome utente? (sì/no): ").strip().lower()

    if not server or not password_file:
        print("[ERROR] Parametri mancanti nel file di configurazione!")
        exit(1)

    try:
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"[ERROR] File delle password '{password_file}' non trovato!")
        exit(1)

    if username_known == 'sì':
        # Se l'utente conosce il nome utente
        username = input("[INFO] Inserisci il nome utente: ").strip()
        usernames = None  # Non ci serve il file degli username
    else:
        # Se l'utente non conosce il nome utente
        try:
            with open(user_file, 'r') as file:
                usernames = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"[ERROR] File degli username '{user_file}' non trovato!")
            exit(1)

        username = None  # Non conosciamo il nome utente

    print(f"[INFO] Inizio brute force su {server}...")
    brute_force = BruteForce(server, username=username, passwords=passwords, usernames=usernames)
    brute_force.start()

if __name__ == "__main__":
    main()
