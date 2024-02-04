from tkinter import Tk
from database import Database
from product import Product
from stock import Stock
import getpass

if __name__ == "__main__":
    mdp = getpass.getpass("Mot de passe: ")
    db = Database(host="localhost", user="root", password=mdp, database="store")
    product = Product(db)

    root = Tk()
    app = Stock(root, product)
    root.mainloop()
