import os

def load_file(filepath):
    """Carica il file di username e restituisce una lista di username."""
    with open(filepath, 'r') as file:
        return file.read().splitlines()

def save_file(filepath, usernames):
    """Salva la lista filtrata di username in un nuovo file."""
    with open(filepath, 'w') as file:
        file.write("\n".join(usernames))

def filter_usernames(usernames):
    """Filtra gli username rimuovendo quelli che iniziano con parole specifiche o che contengono altre parole chiave."""
    filtered = []
    
    # Lista di parole che determinano l'inizio della stringa
    start_words_to_remove = ['the', 'mr', 'iam', 'good', 'welcome', 'my', 'password', 'name', 'surname', 'example']
    
    # Lista di parole chiave che devono essere contenute
    contains_words_to_remove = ['king', 'Name', 'Test', 'Admin', 'User', 'Account', 'Password', 'America', 'Example', 'test', 'user', 'admin', 'orange', 'lemon', 
                                'dog', 'cat', 'america', 'pizza', 'account', 'banana', 'work', 
                                'password', 'name', 'surname', 'example']
    
    for username in usernames:
        # Rimuove username di tre lettere o composti solo da numeri
        if len(username) == 3 or username.isdigit():
            continue
        
        # Rimuove username che iniziano con le parole specificate (case-insensitive)
        if any(username.lower().startswith(word) for word in start_words_to_remove):
            continue

        # Rimuove username che contengono le parole chiave specificate
        if any(word in username.lower() for word in contains_words_to_remove):
            continue
        
        filtered.append(username)
    return filtered

# Percorso del Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Nome del file (senza estensione) che si trova sul Desktop
input_filename = ""  # nome del file senza estensione

# Percorso completo del file di input (aggiungiamo ".txt" se non c'è)
input_file = os.path.join(desktop_path, input_filename + ".txt")

# Percorso per salvare il file filtrato sul Desktop
output_file = os.path.join(desktop_path, "filtered_username_list.txt")

# Stampa il percorso per il debug
print(f"Sto cercando il file di input in: {input_file}")
print(f"Il file filtrato sarà salvato in: {output_file}")

# Controlla se il file di input esiste
if not os.path.exists(input_file):
    print(f"Errore: il file {input_file} non esiste sul Desktop.")
else:
    # Carica la lista originale di username
    usernames = load_file(input_file)

    # Filtra la lista
    filtered_usernames = filter_usernames(usernames)

    # Salva la lista filtrata
    save_file(output_file, filtered_usernames)

    # Mostra il numero di username prima e dopo il filtraggio
    print(f"Lista sfoltita è di {len(filtered_usernames)} username.")
