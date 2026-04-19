import os
from pathlib import Path
from core.crypto import encrypt_file, decrypt_file
from db.models import log_operation

class Lockbox:

    @staticmethod
    def encrypt_path(path: Path, password: str, delete_original=False):
        path = path.resolve()

        if path.is_dir():
            for root, _, files in os.walk(path):
                for f in files:
                    file_path = Path(root) / f
                    if file_path.suffix == ".aes":
                        continue

                    out = encrypt_file(file_path, password, delete_original)
                    log_operation(str(out), "ENCRYPT")

            return path

        else:
            out = encrypt_file(path, password, delete_original)
            log_operation(str(out), "ENCRYPT")
            return out


    @staticmethod
    def decrypt_path(path: Path, password: str, delete_encrypted=False):
        path = path.resolve()

        if path.is_dir():
            for root, _, files in os.walk(path):
                for f in files:
                    file_path = Path(root) / f
                    if file_path.suffix == ".aes":
                        out = decrypt_file(file_path, password, delete_encrypted)
                        log_operation(str(out), "DECRYPT")

            return path

        else:
            out = decrypt_file(path, password, delete_encrypted)
            log_operation(str(out), "DECRYPT")
            return out