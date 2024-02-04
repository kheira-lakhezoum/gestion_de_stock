class Product:
    def __init__(self, database):
        self.db = database

    def get_products(self):
        query = "SELECT id, name, description, price, quantity, id_category FROM product"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    def add_product(self, name, description, price, quantity, id_category):
        query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        values = (name, description, price, quantity, id_category)
        self.db.cursor.execute(query, values)
        self.db.conn.commit()

    def delete_product(self, product_id):
        query = "DELETE FROM product WHERE id = %s"
        self.db.cursor.execute(query, (product_id,))
        self.db.conn.commit()

    def update_product(self, product_id, quantity, price):
        query = "UPDATE product SET quantity = %s, price = %s WHERE id = %s"
        self.db.cursor.execute(query, (quantity, price, product_id))
        self.db.conn.commit()
