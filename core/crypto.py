from pathlib import Path
import pyAesCrypt
from utils.constants import BUFFER_SIZE

def encrypt_file(src: Path, password: str, delete_original=False):
    dst = src.with_suffix(src.suffix + ".aes")
    pyAesCrypt.encryptFile(str(src), str(dst), password, BUFFER_SIZE)

    if delete_original:
        src.unlink(missing_ok=True)

    return dst


def decrypt_file(src: Path, password: str, delete_encrypted=False):
    if src.suffix != ".aes":
        raise ValueError("File must end with .aes")

    dst = src.with_suffix("")
    pyAesCrypt.decryptFile(str(src), str(dst), password, BUFFER_SIZE)

    if delete_encrypted:
        src.unlink(missing_ok=True)

    return dst