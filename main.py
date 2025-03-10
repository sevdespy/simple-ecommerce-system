from product import Product
from customer import Customer
from cart import Cart
from order import Order

def main():
    customer_name = input("Müşteri adınızı girin: ")
    customer = Customer(customer_name)
    cart = Cart()

    products = [
        Product("Laptop", 15000),
        Product("Telefon", 10000),
        Product("Kulaklık", 500),
        Product("Klavye", 800)
    ]

    while True:
        print("\n1. Ürünleri Listele")
        print("2. Sepete Ürün Ekle")
        print("3. Sepetten Ürün Çıkar")
        print("4. Sepeti Görüntüle")
        print("5. Sipariş Ver")
        print("6. Çıkış")
        
        choice = input("Seçiminizi yapın: ")
        
        if choice == "1":
            print("Mevcut Ürünler:")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product}")
        
        elif choice == "2":
            product_index = int(input("Eklemek istediğiniz ürünün numarasını girin: ")) - 1
            if 0 <= product_index < len(products):
                cart.add_product(products[product_index])
            else:
                print("Geçersiz ürün numarası!")
        
        elif choice == "3":
            product_name = input("Çıkarmak istediğiniz ürün adını girin: ")
            cart.remove_product(product_name)
        
        elif choice == "4":
            cart.show_cart()
        
        elif choice == "5":
            order = Order(customer, cart)
            order.checkout()
        
        elif choice == "6":
            print("Çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz seçenek, tekrar deneyin.")

if __name__ == "__main__":
    main()
