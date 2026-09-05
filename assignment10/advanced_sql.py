import sqlite3

# connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Task 1: total price of the first 5 orders
query = """
SELECT orders.order_id, SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items ON orders.order_id = line_items.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
LIMIT 5;
"""
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)

# Task 3: Insert transaction for a new order
conn.execute("PRAGMA foreign_keys = 1")

try:
    # get customer_id for Perez and Sons
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
    customer_id = cursor.fetchone()[0]

    # get employee_id for Miranda Harris
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
    employee_id = cursor.fetchone()[0]

    # get the 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
    product_ids = [row[0] for row in cursor.fetchall()]

    # insert the new order and get its order_id
    cursor.execute(
        "INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, date('now')) RETURNING order_id;",
        (customer_id, employee_id)
    )
    order_id = cursor.fetchone()[0]

    # insert a line_item for each of the 5 products, quantity 10
    for product_id in product_ids:
        cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);",
            (order_id, product_id, 10)
        )

    conn.commit()  # commit the whole transaction
except Exception as e:
    conn.rollback()
    print("Error:", e)

# print the line_items for the new order
query3 = """
SELECT line_items.line_item_id, line_items.quantity, products.product_name
FROM line_items
JOIN products ON line_items.product_id = products.product_id
WHERE line_items.order_id = ?;
"""
cursor.execute(query3, (order_id,))
for row in cursor.fetchall():
    print(row)




# Task 4: employees with more than 5 orders
query4 = """
SELECT employees.employee_id, employees.first_name, employees.last_name, COUNT(orders.order_id) AS order_count
FROM employees
JOIN orders ON employees.employee_id = orders.employee_id
GROUP BY employees.employee_id
HAVING COUNT(orders.order_id) > 5;
"""
cursor.execute(query4)
for row in cursor.fetchall():
    print(row)
conn.close()