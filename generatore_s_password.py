import os

def load_passwords(filepath):
    """Carica il file di password e restituisce una lista di password."""
    with open(filepath, 'r') as file:
        return file.read().splitlines()

def save_sublist(filepath, passwords):
    """Salva una sottolista di password in un file di testo."""
    with open(filepath, 'w') as file:
        file.write("\n".join(passwords))

# Percorso del Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Nome del file di password sul Desktop
input_filename = "filtered_password_list.txt"  # Modifica il nome con quello del file esatto

# Percorso completo del file di input
input_file = os.path.join(desktop_path, input_filename)

# Carica le password dal file e calcola il totale
passwords = load_passwords(input_file)
total_passwords = len(passwords)

# Calcola il numero di password per ciascuna sottolista
sublist_size = total_passwords // 2
remainder = total_passwords % 2

# Crea e salva le due sottoliste
for i in range(2):
    start_index = i * sublist_size
    end_index = start_index + sublist_size

    # Aggiunge il resto alla seconda sottolista, se esiste
    if i == 1:
        end_index += remainder
    
    # Sottolista corrente
    sublist = passwords[start_index:end_index]

    # Percorso del file della sottolista corrente
    sublist_filename = f"s_password{i + 1}.txt"
    sublist_filepath = os.path.join(desktop_path, sublist_filename)

    # Salva la sottolista
    save_sublist(sublist_filepath, sublist)

print(f"Creati 2 file di sottoliste sul Desktop, ciascuno con una parte delle password.")
