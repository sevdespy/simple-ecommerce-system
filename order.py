class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart
        self.total = cart.total_price()

    def checkout(self):
        if not self.cart.items:
            print("Sepetiniz boş, sipariş verilemez.")
        else:
            print(f"{self.customer} için sipariş oluşturuldu. Toplam Tutar: {self.total} TL")