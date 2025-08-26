import psycopg2

connection = psycopg2.connect(
        host="localhost",
        database="restaurant",
        user="postgres",
        password="postgres"  
    )
cursor = connection.cursor()

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price  
    def save(self):
       query = f''' 
       INSERT INTO menu_item (item_name, item_price) VALUES (%s, %s) RETURNING item_id;
       '''
       cursor.execute(query, (self.item_name, self.item_price))
       self.item_id = cursor.fetchone()[0]
       connection.commit()
    def update(self, new_name, new_price):
       
        cursor.execute(
            "UPDATE menu_item SET item_name = %s, item_price = %s WHERE item_id = %s;",
            (new_name, new_price, self.item_id)
        )
        connection.commit()
        self.item_name = new_name
        self.item_price = new_price
    def delete(self):
        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s;", (self.name,))
        connection.commit()

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = " SELECT * FROM menu_item WHERE item_name = %s"
        cursor.execute(query,(name,))
        item = cursor.fetchone()
        if item:
            menu_item = MenuItem(item[1], item[2])
            menu_item.item_id = item[0]
            return menu_item
        return None
    @classmethod
    def all_items(cls):
        cursor.execute("SELECT * FROM Menu_Items;")
        items = cursor.fetchall()
        return [MenuItem(item[1], item[2]) for item in items]


item = MenuItem("burger", 40)
item2 = MenuManager.get_by_name("tacos")
