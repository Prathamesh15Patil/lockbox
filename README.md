🔐 Lockbox

Lockbox is a lightweight Python tool to encrypt and decrypt files & folders using AES-256 encryption.
It supports both GUI (Tkinter) and CLI modes, and is optimized for handling large files efficiently.

🚀 Features
🔒 AES-256 encryption (via pyAesCrypt)
📁 File-by-file folder encryption (no large zip files)
💻 Command Line Interface (CLI)
🖥️ Simple GUI (Tkinter)
⚡ Low memory usage (streaming encryption)
🗂️ Handles large files (30GB+)
🧠 SQLite database for operation history
🛠️ Tech Stack
Python 3
pyAesCrypt
Tkinter
SQLite3
📂 Project Structure
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
⚙️ Installation
git clone https://github.com/your-username/lockbox.git
cd lockbox
pip install -r requirements.txt
▶️ Usage
🖥️ GUI Mode
python main.py
💻 CLI Mode
Encrypt
python main.py --encrypt --path file.txt
Decrypt
python main.py --decrypt --path file.txt.aes
With password (optional)
python main.py --encrypt --path file.txt --password mypass
🧠 How it Works
Each file is encrypted individually using AES-256
Encrypted files are saved with .aes extension
Folder encryption processes all files recursively
SQLite database logs all operations (encrypt/decrypt)
⚠️ Notes
If you lose your password, files cannot be recovered
Do not modify .aes files manually
Make sure you have enough disk space before encryption
📌 Future Improvements
📊 GUI history dashboard (from SQLite)
🔐 Password strength meter
📈 Real progress tracking
📦 Executable build (.exe)
