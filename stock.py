from tkinter import *
from tkinter import ttk
from product import Product

class Stock:
    def __init__(self, root, product):
        self.root = root
        self.root.title("Gestion de Stock")
        self.product = product

        self.create_widgets()
        self.refresh_product_list()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"))
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Nom")
        self.tree.heading("#3", text="Description")
        self.tree.heading("#4", text="Prix")
        self.tree.heading("#5", text="Quantité")
        self.tree.heading("#6", text="Catégorie")
        self.tree.pack(pady=10)

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.name_entry = Entry(self.root, width=30)
        self.description_entry = Entry(self.root, width=30)
        self.price_entry = Entry(self.root, width=10)
        self.quantity_entry = Entry(self.root, width=10)
        self.category_entry = Entry(self.root, width=15)

        self.name_entry.insert(0, "Nom du produit")
        self.description_entry.insert(0, "Description")
        self.price_entry.insert(0, "Prix")
        self.quantity_entry.insert(0, "Quantité")
        self.category_entry.insert(0, "ID Catégorie")

        self.name_entry.pack()
        self.description_entry.pack()
        self.price_entry.pack()
        self.quantity_entry.pack()
        self.category_entry.pack()

        self.add_button = Button(self.root, text="Ajouter un produit", command=self.add_product)
        self.add_button.pack()

        self.delete_button = Button(self.root, text="Supprimer le produit sélectionné", command=self.delete_product)
        self.delete_button.pack()

        self.update_button = Button(self.root, text="Modifier le produit sélectionné", command=self.update_product)
        self.update_button.pack()

        self.refresh_product_list()

    def refresh_product_list(self):
        self.tree.delete(*self.tree.get_children())
        products = self.product.get_products()
        for product in products:
            self.tree.insert("", "end", values=product)

    def add_product(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        category_id = self.category_entry.get()
        self.product.add_product(name, description, price, quantity, category_id)
        self.refresh_product_list()

    def delete_product(self):
        selected_item = self.tree.selection()[0]
        product_id = self.tree.item(selected_item, "values")[0]
        self.product.delete_product(product_id)
        self.refresh_product_list()

    def update_product(self):
        selected_item = self.tree.selection()[0]
        product_id = self.tree.item(selected_item, "values")[0]
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        self.product.update_product(product_id, quantity, price)
        self.refresh_product_list()
