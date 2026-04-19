from db.database import get_connection

def log_operation(file_path: str, operation: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (file_path, operation) VALUES (?, ?)",
        (file_path, operation)
    )

    conn.commit()
    conn.close()