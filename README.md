# 🔬 Primer Toolbox

A simple Python-based toolkit for designing PCR primers from DNA sequences.

## 📦 Features

- Calculate **GC content** and **melting temperature (Tm)**
- Generate **forward and reverse primers** of user-defined length
- Return **reverse complement** of DNA
- Export primer data to CSV (optional)

## 🧬 Example Usage

```bash
python3 main.py ATGCGTATCGGACTAGC 10

```
## 🔁 Example Output
```
Forward primer: ATGCGTATCG
 GC%: 50.0  Tm: 30°C
Reverse primer: GCTAGTCCGA
 GC%: 60.0  Tm: 34°C
```
## 📁 Project Structure
```
primer_toolbox/
├── main.py            # User interface / CLI
├── primer_tools.py    # Core bio functions (GC, Tm, rev comp)
├── export.py          # CSV export (optional)
└── README.md
```

## 💻 Requirements
```
Python 3.x
(No external libraries needed — standard Python only)
```

## 📤 Exporting to CSV
```
from export import export_to_csv

primer_data = [
    ("Forward", "ATGCGTATCG", 50.0, 30),
    ("Reverse", "GCTAGTCCGA", 60.0, 34),
]
export_to_csv("primers.csv", primer_data)

primer_data = [
    ("Forward", "ATGCGTATCG", 50.0, 30),
    ("Reverse", "GCTAGTCCGA", 60.0, 34),
]
export_to_csv("primers.csv", primer_data)

```

## 📜 License
```
MIT License — free to use, modify, and share.

