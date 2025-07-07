from inventory_utils import restock_quantity

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        value = super().total_value()
        if self.expiry_days < 5:
            return round(value * 0.8, 2)  # 20% discount
        return value

class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_inventory(self):
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name} | Qty: {product.quantity} | Value: {product.total_value()}")

    def search_by_name(self, term):
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.products))
        return results

    def restock_all(self):
        for product in self.products:
            product.quantity = restock_quantity(product.quantity)

    def export_summary(self, filename="inventory_report.txt"):
        summary = {
            product.name: {
                "Price": product.price,
                "Quantity": product.quantity,
                "Total Value": product.total_value()
            }
            for product in self.products
        }
        with open(filename, "w") as file:
            for name, info in summary.items():
                file.write(f"{name} → {info}\n")

# Example Usage
manager = InventoryManager()
manager.add_product(Product("Book", 300, 5))
manager.add_product(PerishableProduct("Milk", 120, 10, 3))
manager.add_product(PerishableProduct("Cheese", 200, 7, 10))

print("🔹 Inventory:")
manager.list_inventory()

print("\n🔍 Search Results for 'milk':")
for p in manager.search_by_name("milk"):
    print(f"- {p.name}: {p.quantity} units")

print("\n📦 Restocking...")
manager.restock_all()
manager.list_inventory()

print("\n📝 Exporting summary to file...")
manager.export_summary()
