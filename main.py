from cli.cli import parse_args
from core.operations import Lockbox
from db.database import init_db
from ui.app import App
from pathlib import Path
import sys
import getpass

def main():
    init_db()

    args = parse_args()

    if not args.encrypt and not args.decrypt and not args.path:
        app = App()
        app.mainloop()
        return

    if not args.path:
        print("Path required")
        sys.exit(2)

    pwd = args.password or getpass.getpass("Enter password: ")

    target = Path(args.path)

    if args.encrypt:
        Lockbox.encrypt_path(target, pwd, delete_original=args.delete)

    elif args.decrypt:
        Lockbox.decrypt_path(target, pwd, delete_encrypted=args.delete)


if __name__ == "__main__":
    main()