import os

def load_file(filepath):
    """Carica il file di password e restituisce una lista di password."""
    with open(filepath, 'r') as file:
        return file.read().splitlines()

def save_file(filepath, passwords):
    """Salva la lista filtrata di password in un nuovo file."""
    with open(filepath, 'w') as file:
        file.write("\n".join(passwords))

def filter_passwords(passwords):
    """Filtra le password rimuovendo quelle che iniziano con parole specifiche o che contengono altre parole chiave."""
    filtered = []
    
    # Lista di parole che determinano l'inizio della stringa
    start_words_to_remove = ['the', 'mr', 'iam', 'good', 'welcome', 'my', 'password', 'name', 'surname', 'example']
    
    # Lista di parole chiave che devono essere contenute
    contains_words_to_remove = ['king', 'Name', 'Test', 'Admin', 'User', 'Account', 'Password', 'America', 'Example', 'test', 'user', 'admin', 'orange', 'lemon', 
                                'dog', 'cat', 'america', 'pizza', 'account', 'banana', 'work', 
                                'password', 'name', 'surname', 'example']
    
    for password in passwords:
        # Rimuove password di tre lettere o composte solo da numeri
        if len(password) == 3 or password.isdigit():
            continue
        
        # Rimuove password che iniziano con le parole specificate (case-insensitive)
        if any(password.lower().startswith(word) for word in start_words_to_remove):
            continue

        # Rimuove password che contengono le parole chiave specificate
        if any(word in password.lower() for word in contains_words_to_remove):
            continue
        
        filtered.append(password)
    return filtered

# Percorso del Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Nome del file (senza estensione) che si trova sul Desktop
input_filename = ""  # nome del file delle password senza estensione

# Percorso completo del file di input (aggiungiamo ".txt" se non c'è)
input_file = os.path.join(desktop_path, input_filename + ".txt")

# Percorso per salvare il file filtrato sul Desktop
output_file = os.path.join(desktop_path, "filtered_password_list.txt")

# Stampa il percorso per il debug
print(f"Sto cercando il file di input in: {input_file}")
print(f"Il file filtrato sarà salvato in: {output_file}")

# Controlla se il file di input esiste
if not os.path.exists(input_file):
    print(f"Errore: il file {input_file} non esiste sul Desktop.")
else:
    # Carica la lista originale di password
    passwords = load_file(input_file)

    # Filtra la lista
    filtered_passwords = filter_passwords(passwords)

    # Salva la lista filtrata
    save_file(output_file, filtered_passwords)

    # Mostra il numero di password prima e dopo il filtraggio
    print(f"Lista sfoltita è di {len(filtered_passwords)} password.")
