import os

def load_usernames(filepath):
    """Carica il file di username e restituisce una lista di username."""
    with open(filepath, 'r') as file:
        return file.read().splitlines()

def save_sublist(filepath, usernames):
    """Salva una sottolista di username in un file di testo."""
    with open(filepath, 'w') as file:
        file.write("\n".join(usernames))

# Percorso del Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Nome del file di username sul Desktop (senza estensione)
input_filename = "filtered_username_list.txt"  # Modifica il nome con quello del file esatto

# Percorso completo del file di input
input_file = os.path.join(desktop_path, input_filename)

# Carica gli username dal file e calcola il totale
usernames = load_usernames(input_file)
total_usernames = len(usernames)

# Calcola il numero di username per ogni sottolista
sublist_size = total_usernames // 10
remainder = total_usernames % 10

# Crea le sottoliste e salva ciascuna come file separato
for i in range(10):
    start_index = i * sublist_size
    end_index = start_index + sublist_size

    # Aggiunge il resto alla decima sottolista, se esiste
    if i == 9:
        end_index += remainder
    
    # Sottolista corrente
    sublist = usernames[start_index:end_index]

    # Percorso del file della sottolista corrente
    sublist_filename = f"s_username{i + 1}.txt"
    sublist_filepath = os.path.join(desktop_path, sublist_filename)

    # Salva la sottolista
    save_sublist(sublist_filepath, sublist)

print(f"Creati {10} file di sottoliste sul Desktop, ciascuno con una parte degli username.")
