import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the 'products' table
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                )''')

# Insert some product records
products = [
    ('Laptop', 999.99),
    ('Mouse', 49.99),
    ('Keyboard', 149.99)
]
cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', products)

# Commit the changes
conn.commit()

# Query products with price > 100
cursor.execute('SELECT * FROM products WHERE price > 100')
rows = cursor.fetchall()

# Print the products
for row in rows:
    print(row)

# Close the connection
conn.close()
