import json
import sys

def read_dfa_from_file(filename):
    """Membaca DFA dari file JSON eksternal."""
    try:
        with open(filename, 'r') as file:
            dfa = json.load(file)
        return dfa
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' memiliki format JSON yang tidak valid.")
        return None

def simulate_dfa(dfa, test_string):
    """Mensimulasikan DFA berdasarkan string input."""
    current_state = dfa["start_state"]
    path = [current_state]

    for symbol in test_string:
        if symbol not in dfa["alphabet"]:
            return f"Error: Symbol '{symbol}' tidak ada dalam alfabet DFA"
        
        if current_state not in dfa["transitions"] or symbol not in dfa["transitions"][current_state]:
            return f"Error: Tidak ada transisi dari state '{current_state}' dengan simbol '{symbol}'"
        
        next_state = dfa["transitions"][current_state][symbol]
        path.append(next_state)
        current_state = next_state

    status = "ACCEPTED" if current_state in dfa["accept_states"] else "REJECTED"
    return f"Path: {' → '.join(path)}\nStatus: {status}"

# Cek apakah argumen command line telah diberikan
if len(sys.argv) < 2:
    print("Usage: python script.py <nama_file_json>")
    sys.exit(1)

filename = sys.argv[1]
dfa = read_dfa_from_file(filename)

# Jalankan simulasi jika file berhasil dibaca
if dfa:
    print("\n=== SIMULASI DFA ===")
    print(f"String yang diuji: {dfa['test_string']}")
    result = simulate_dfa(dfa, dfa["test_string"])
    print(result)
