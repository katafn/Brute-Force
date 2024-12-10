import json
import ipaddress
from brute_force2 import BruteForce, is_server_reachable

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


def is_valid_ip(ip):
    """Verifica se l'indirizzo IP è valido."""
    try:
        ipaddress.ip_address(ip)  # Tentiamo di interpretare l'indirizzo IP
        return True
    except ValueError:
        return False


def load_file_list(file_path):
    """Carica una lista di username o password da un file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"[ERROR] File '{file_path}' non trovato!")
        exit(1)


def main():
    config_file = "brute force/config.json"
    config = load_config(config_file)

    # Chiedi all'utente di inserire l'indirizzo IP del server
    server = input("[INFO] Inserisci l'indirizzo IP del server (ad esempio: 192.168.1.1): ").strip()

    # Verifica se l'indirizzo IP è valido
    if not server or not is_valid_ip(server):
        print("[ERROR] Devi inserire un indirizzo IP valido!")
        exit(1)

    # Verifica se il server è raggiungibile
    if not is_server_reachable(server):
        print(f"[ERROR] Il server {server} non è raggiungibile. Impossibile eseguire il brute force.")
        exit(1)

    # Chiedi all'utente se vuole caricare le password da un file
    password_file = input("[INFO] Inserisci il percorso del file contenente le password: ").strip()
    passwords = load_file_list(password_file)

    # Chiedi all'utente se conosce il nome utente
    username_known = input("[INFO] Conosci il nome utente? (sì/no): ").strip().lower()

    # Se l'utente non conosce il nome utente, chiedi di caricare un file di username
    if username_known == 'no':
        user_file = input("[INFO] Inserisci il percorso del file contenente gli username: ").strip()
        usernames = load_file_list(user_file)
    else:
        usernames = None  # Non ci serve il file degli username se il nome utente è conosciuto

    # Verifica se l'utente ha inserito correttamente i dati
    if not passwords:
        print("[ERROR] Devi inserire almeno una password!")
        exit(1)
    if username_known == 'no' and not usernames:
        print("[ERROR] Devi inserire almeno uno username se non conosci il nome utente!")
        exit(1)

    print(f"[INFO] Inizio brute force su {server}...")
    brute_force = BruteForce(server, username=None if username_known == 'no' else input("[INFO] Inserisci il nome utente: "), passwords=passwords, usernames=usernames)
    brute_force.start()


if __name__ == "__main__":
    main()
