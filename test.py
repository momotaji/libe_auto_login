class Product:
    def __init__(self,name,stock):
        self.name = name
        self.stock = stock

    def add_stock(self,amount):
        self.stock +=amount

    def show_stock(self):
        print(f"{self.name}の在庫は{self.stock}です")

item = Product('りんご',5)
item.add_stock(5)
item.show_stock()