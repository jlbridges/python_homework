import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, magazine_name, publisher_name):
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
    result = cursor.fetchone()
    if result is None:
        print(f"No publisher named '{publisher_name}' found. Cannot add magazine '{magazine_name}'.")
        return
    publisher_id = result[0]

    try:
        cursor.execute(
            "INSERT INTO magazines (magazine_name, publisher_id) VALUES (?, ?)",
            (magazine_name, publisher_id)
        )
    except sqlite3.IntegrityError:
        print(f"Magazine '{magazine_name}' already exists.")

def add_subscriber(cursor, name, address):
    cursor.execute(
        "SELECT * FROM subscribers WHERE subscriber_name = ? AND address = ?",
        (name, address)
    )
    if cursor.fetchone() is not None:
        print(f"Subscriber '{name}' at '{address}' already exists.")
        return

    try:
        cursor.execute(
            "INSERT INTO subscribers (subscriber_name, address) VALUES (?, ?)",
            (name, address)
        )
    except sqlite3.IntegrityError as e:
        print(f"Error adding subscriber '{name}': {e}")

def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    cursor.execute(
        "SELECT subscriber_id FROM subscribers WHERE subscriber_name = ? AND address = ?",
        (subscriber_name, subscriber_address)
    )
    result = cursor.fetchone()
    if result is None:
        print(f"No subscriber named '{subscriber_name}' at '{subscriber_address}' found.")
        return
    subscriber_id = result[0]

    cursor.execute("SELECT magazine_id FROM magazines WHERE magazine_name = ?", (magazine_name,))
    result = cursor.fetchone()
    if result is None:
        print(f"No magazine named '{magazine_name}' found.")
        return
    magazine_id = result[0]

    cursor.execute(
        "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
        (subscriber_id, magazine_id)
    )
    if cursor.fetchone() is not None:
        print(f"'{subscriber_name}' is already subscribed to '{magazine_name}'.")
        return

    try:
        cursor.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
        )
    except sqlite3.IntegrityError as e:
        print(f"Error adding subscription: {e}")


with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    try:
        cursor = conn.cursor()

        # Task 2: Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                magazine_name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            )
            """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                subscriber_name TEXT NOT NULL,
                address TEXT NOT NULL
            )
            """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
            )
            """)

        print("Tables created successfully.")

        # Task 3: Populate tables
        add_publisher(cursor, "Conde Nast")
        add_publisher(cursor, "Hearst")
        add_publisher(cursor, "Meredith")

        add_magazine(cursor, "Vogue", "Conde Nast")
        add_magazine(cursor, "Wired", "Conde Nast")
        add_magazine(cursor, "Cosmopolitan", "Hearst")
        add_magazine(cursor, "Good Housekeeping", "Hearst")
        add_magazine(cursor, "People", "Meredith")

        add_subscriber(cursor, "Alice Smith", "123 Main St")
        add_subscriber(cursor, "Bob Jones", "456 Oak Ave")
        add_subscriber(cursor, "Carla Diaz", "789 Pine Rd")

        add_subscription(cursor, "Alice Smith", "123 Main St", "Vogue", "2027-01-15")
        add_subscription(cursor, "Alice Smith", "123 Main St", "Wired", "2027-03-01")
        add_subscription(cursor, "Bob Jones", "456 Oak Ave", "Cosmopolitan", "2026-12-31")
        add_subscription(cursor, "Carla Diaz", "789 Pine Rd", "People", "2027-06-30")

        conn.commit()
        print("Sample data inserted successfully.")

        # Task 4: Queries
        print("\nAll subscribers:")
        cursor.execute("SELECT * FROM subscribers")
        for row in cursor.fetchall():
            print(row)

        print("\nAll magazines, sorted by name:")
        cursor.execute("SELECT * FROM magazines ORDER BY magazine_name")
        for row in cursor.fetchall():
            print(row)

        print("\nMagazines published by Conde Nast:")
        cursor.execute("""
            SELECT magazines.magazine_name
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.publisher_id
            WHERE publishers.name = 'Conde Nast'
        """)
        for row in cursor.fetchall():
            print(row)

    except sqlite3.Error as e:
        print(f"Error: {e}")