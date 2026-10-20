import os
import sqlite3

def init_database():
    db_dir = os.path.join("data", "db")
    os.makedirs(db_dir, exist_ok=True)
    
    db_path = os.path.join(db_dir, "regulations.db")
    print(f"Initializing database at: {db_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table for regulatory status
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS regulations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scientific_name TEXT NOT NULL,
            common_name TEXT NOT NULL,
            state_code TEXT NOT NULL,
            is_invasive BOOLEAN NOT NULL,
            regulatory_status TEXT NOT NULL,
            ecological_risk TEXT NOT NULL
        )
    """)
    
    # Seed sample invasive and native plant data
    sample_data = [
        ("celastrus orbiculatus", "Oriental Bittersweet", "PA", True, "Invasive - Class B", "High"),
        ("rosa multiflora", "Multiflora Rose", "PA", True, "Noxious Weed", "High"),
        ("lythrum salicaria", "Purple Loosestrife", "PA", True, "Invasive", "Medium"),
        ("acer rubrum", "Red Maple", "PA", False, "Native / Non-Regulated", "Low"),
    ]
    
    cursor.execute("DELETE FROM regulations")  # Clear existing records on re-run
    cursor.executemany("""
        INSERT INTO regulations (scientific_name, common_name, state_code, is_invasive, regulatory_status, ecological_risk)
        VALUES (?, ?, ?, ?, ?, ?)
    """, sample_data)
    
    conn.commit()
    conn.close()
    print("Database initialized and seeded successfully!")

if __name__ == "__main__":
    init_database()