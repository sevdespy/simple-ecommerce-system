class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} sepete eklendi.")

    def remove_product(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"{product.name} sepetten çıkarıldı.")
                return
        print("Ürün sepette bulunamadı.")

    def show_cart(self):
        if not self.items:
            print("Sepetiniz boş.")
        else:
            print("Sepetiniz:")
            for product in self.items:
                print(product)

    def total_price(self):
        return sum(product.price for product in self.items)