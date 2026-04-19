# 🔐 Lockbox

Lockbox is a lightweight Python tool to **encrypt and decrypt files & folders using AES-256 encryption**.  
It supports both **GUI (Tkinter)** and **CLI modes**, and is optimized for handling large files efficiently.

---

## 🚀 Features

- 🔒 AES-256 encryption (via pyAesCrypt)
- 📁 File-by-file folder encryption (no large zip files)
- 💻 Command Line Interface (CLI)
- 🖥️ Simple GUI (Tkinter)
- ⚡ Low memory usage (streaming encryption)
- 🗂️ Handles large files (30GB+)
- 🧠 SQLite database for operation history

---

## 🛠️ Tech Stack

- Python 3  
- pyAesCrypt  
- Tkinter  
- SQLite3  

---

## 📂 Project Structure

```bash
lockbox/
│
├── main.py
├── core/
│   ├── crypto.py
│   └── operations.py
├── db/
│   ├── database.py
│   └── models.py
├── ui/
│   └── app.py
├── cli/
│   └── cli.py
├── utils/
│   └── constants.py
├── requirements.txt
└── README.md

```
git clone https://github.com/Prathamesh15Patil/lockbox.git
cd lockbox
pip install -r requirements.txt
