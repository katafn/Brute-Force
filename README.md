# Brute Force Tool per FTP e SSH

Questo progetto implementa un **Brute Force Tool** per attacchi su server **FTP** e **SSH**, permettendo di testare combinazioni di nome utente e password tramite liste predefinite caricate da file.  

⚠️ **Nota bene:** Questo strumento è inteso esclusivamente per scopi didattici o per test di sicurezza autorizzati. L'uso improprio può essere illegale.

---

## Requisiti

- Python 3.7 o superiore
- Moduli Python standard:
  - `ipaddress`
  - `ftplib`
  - `paramiko` (per SSH)
  - `socket`

---

## Configurazione

1. **Struttura dei file**  
   Assicurati di avere:
   - Un file contenente una lista di **password**, con una password per riga:
     ```
     password1
     password2
     password3
     ...
     ```
   - (Opzionale) Un file contenente una lista di **username**, con uno username per riga:
     ```
     username1
     username2
     username3
     ...
     ```

---

## Come utilizzare

1. **Esegui il programma**  
   Avvia il programma principale:
   ```bash
   python main.py
   ```

2. **Scegli il protocollo**  
   Quando richiesto, scegli il protocollo su cui eseguire il brute force:
   - FTP
   - SSH

3. **Inserisci l'indirizzo IP**  
   Digita l'indirizzo IP del server quando richiesto. Il programma verifica se l'indirizzo IP è valido e se il server è raggiungibile.

4. **Carica le liste di password e username**  
   - Fornisci il percorso del file contenente la lista delle password.  
   - Se **NON conosci il nome utente**, fornisci anche il file degli username quando richiesto.

5. **Avvio del brute force**  
   Il programma tenterà tutte le combinazioni di username e password sul protocollo scelto. Se trova una combinazione valida, verrà mostrato:
   ```
   [SUCCESS] Login riuscito con: username:password
   ```
   Altrimenti, al termine delle prove, apparirà:
   ```
   [INFO] Nessuna password trovata.
   ```

---

## Funzionalità principali

- **Supporto FTP e SSH:** È possibile scegliere se eseguire il brute force su server FTP o SSH.
- **Verifica indirizzo IP:** Controlla che l'indirizzo IP fornito sia valido e che il server sia raggiungibile.
- **Supporto multiutente:** Possibilità di utilizzare una lista di username se il nome utente non è noto.
- **Lettura da file:** Carica liste di password e username da file esterni.
- **Messaggi chiari:** Segnala tentativi riusciti e falliti in tempo reale.

---

## Esempio di utilizzo

```
[INFO] Scegli il protocollo per il brute force: (1) FTP (2) SSH: 1
[INFO] Inserisci l'indirizzo IP del server (ad esempio: 192.168.1.1): 192.168.1.1
[INFO] Inserisci il percorso del file contenente le password: passwords.txt
[INFO] Conosci il nome utente? (sì/no): no
[INFO] Inserisci il percorso del file contenente gli username: usernames.txt
[INFO] Inizio brute force su 192.168.1.1 con FTP...
[SUCCESS] Login riuscito con: admin:password123
```

---

## Disclaimer

Questo strumento è stato sviluppato a scopo didattico. L'uso su sistemi senza autorizzazione è **illegale** e punibile per legge. Utilizzare solo per test di sicurezza su server di proprietà o con il permesso del proprietario. L'autore non è responsabile per eventuali usi impropri.

---

### Come funziona:

1. **FTP:**  
   - Quando il protocollo scelto è **FTP**, il programma tenta di connettersi al server FTP sulla porta **21** e testare le combinazioni di username e password.  
   - Utilizza il modulo `ftplib` per la connessione e il login.

2. **SSH:**  
   - Quando il protocollo scelto è **SSH**, il programma tenta di connettersi al server SSH sulla porta **22** e testare le combinazioni di username e password.  
   - Utilizza il modulo `paramiko` per la connessione SSH.
  
---

### Modifiche recenti:

- **Aggiunta del supporto SSH**: Ora è possibile eseguire brute force su server **SSH** oltre che su server **FTP**.
