# DFA Simulator


| Nama                             | NRP        | Kelas     |
| -------------------------------- | ---------- | --------- |
| Alvin Zanua Putra                | 5025231064 | Otomata E |
| Pramudtya Faiz Ardiansyah        | 5025231108 | Otomata E |
| Christoforus Indra Bagus Pratama | 5025231124 | Otomata E |
| Muhammad Azhar Aziz              | 5025231131 | Otomata E |


## Pengaplikasian
Proyek ini dibuat oleh tim yang terdiri dari **4 orang** untuk mengembangkan **Simulator Deterministic Finite Automaton (DFA)** yang dapat menguji apakah sebuah string diterima atau ditolak berdasarkan aturan DFA yang diberikan dalam format **JSON**.

Simulator ini akan membaca **file JSON eksternal** yang berisi konfigurasi DFA, kemudian memproses string uji dan menentukan jalur transisi serta status akhir (ACCEPTED atau REJECTED).

---

## Struktur Proyek
```
/dfa-simulator
│── dfa_simulator.py            # Program utama untuk simulasi DFA
│── dfa_config.json             # File konfigurasi DFA dalam format JSON
│── dfa_rejected_config.json    # Contoh File konfigurasi DFA yang Rejected
│── README.md                   # Dokumentasi proyek
```

---

## Persyaratan
- **Python 3.x**
- **File konfigurasi DFA dalam format JSON** (`dfa_config.json`)

---

## Instalasi & Menjalankan Program
### 1. Clone atau Unduh Proyek
```bash
git clone https://github.com/alvinzanuaputra/dfa-simulator.git
cd dfa-simulator
```

### 2. Jalankan Program
```bash
python dfa_simulator.py dfa_config.json
```

---

## Format Input (JSON)
File **`dfa_config.json`** berisi konfigurasi DFA. Contoh:
```json
{
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b"],
    "start_state": "q0",
    "accept_states": ["q2", "q3"],
    "transitions": {
        "q0": { "a": "q1", "b": "q3" },
        "q1": { "a": "q1", "b": "q2" },
        "q2": { "a": "q1", "b": "q3" },
        "q3": { "a": "q2", "b": "q3" }
    },
    "test_string": "ab"
}
```
**Keterangan:**
- **states**: Daftar semua state dalam DFA.
- **alphabet**: Alfabet (simbol) yang dikenali DFA.
- **start_state**: State awal DFA.
- **accept_states**: State yang menerima input sebagai valid.
- **transitions**: Aturan transisi berdasarkan simbol yang diberikan.
- **test_string**: String yang akan diuji pada DFA.

---

## Kode Program
### `dfa_simulator.py`
```python
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
```

---

## Contoh Output
### **Kasus 1: `test_string = "ab"`**
#### **Input JSON:**
```json
{
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b"],
    "start_state": "q0",
    "accept_states": ["q2", "q3"],
    "transitions": {
        "q0": { "a": "q1", "b": "q3" },
        "q1": { "a": "q1", "b": "q2" },
        "q2": { "a": "q1", "b": "q3" },
        "q3": { "a": "q2", "b": "q3" }
    },
    "test_string": "ab"
}
```
#### **Input:**
```console
python dfa_simulator.py dfa_config.json  
```
#### **Output:**
```
=== SIMULASI DFA ===
String yang diuji: ab
Path: q0 → q1 → q2
Status: ACCEPTED
```

### **Kasus 2: `test_string = "aa"`**
#### **Input JSON:**
```json
{
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b"],
    "start_state": "q0",
    "accept_states": ["q2", "q3"],
    "transitions": {
        "q0": { "a": "q1", "b": "q3" },
        "q1": { "a": "q1", "b": "q2" },
        "q2": { "a": "q1", "b": "q3" },
        "q3": { "a": "q2", "b": "q3" }
    },
    "test_string": "aa"
}
```
#### **Input:**
```console
python dfa_simulator.py dfa_rejected_config.json 
```
#### **Output:**
```
=== SIMULASI DFA ===
String yang diuji: aa
Path: q0 → q1 → q1
Status: REJECTED
```

---

## Overview Output

```bash
PS D:\Tugas\26. Otomata E\dfa-simulator> python dfa_simulator.py dfa_config.json

=== SIMULASI DFA ===
String yang diuji: ab
Path: q0 → q1 → q2
Status: ACCEPTED

PS D:\Tugas\26. Otomata E\dfa-simulator> python dfa_simulator.py dfa_rejected_config.json  

=== SIMULASI DFA ===
String yang diuji: aa
Path: q0 → q1 → q1
Status: REJECTED
```

---
# Terima Kasih 🤝🤝
