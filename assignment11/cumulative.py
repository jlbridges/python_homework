import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with sqlite3.connect("../db/lesson.db") as conn:
    query = """
        SELECT orders.order_id, SUM(products.price * line_items.quantity) AS total_price
        FROM orders
        JOIN line_items ON orders.order_id = line_items.order_id
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id;
    """
    df = pd.read_sql_query(query, conn)

df['cumulative'] = df['total_price'].cumsum()

print(df)

df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    title="Cumulative Revenue Over Time",
    xlabel="Order ID",
    ylabel="Cumulative Revenue ($)",
    legend=False,
)
plt.show()