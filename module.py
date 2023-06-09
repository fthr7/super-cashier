# -*- coding: utf-8 -*-
# import menu



# pertama fungsi ini dilakukan untuk menginisialisasi variabel
# item yang akan digunakan oleh user
class Transaction:
    def __init__(self):
        self.items = []
        self.total = 0
# fungsi ini digunakan untuk menambahkan item ke dalam transaksi
    def add_item(self, item):
        self.items.append(item)
        self.total += item[1] * item[2]
# fungsi ini digunakan untuk mengubah nama item pada transaksi
    def update_item_name(self, old_name, new_name):
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name
# fungsi ini digunakan untuk mengubah jumlah item pada transaksi
    def update_item_qty(self, name, qty):
        for item in self.items:
            if item[0] == name:
                old_qty = item[1]
                item[1] = qty
                self.total += (qty - old_qty) * item[2]
# fungsi ini digunakan untuk mengubah harga per item               
    def update_item_price(self, name, price):
        for item in self.items:
            if item[0] == name:
                old_price = item[2]
                item[2] = price
                self.total += (price - old_price) * item[1]
# fungsi ini digunakan untuk menghapus item dari transaksi                
    def delete_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.total -= item[1] * item[2]
                self.items.remove(item)
# fungsi ini  digunakan untuk menghapus semua item dari transaksi 
# dan mengatur total harga menjadi 0              
    def reset_transaction(self):
        self.items = []
        self.total = 0
# fungsi ini digunakan untuk memeriksa apakah 
# data input item pada transaksi sudah benar
# dan kemudian memanggil fungsi show_transaction()     
    def check_order(self):
        for item in self.items:
            if len(item) != 3:
                print("Terdapat kesalahan input data")
                return
        print("Pemesanan sudah benar")
        self.show_transaction()
# fungsi ini digunakan untuk menampilkan seluruh item pada transaksi 
# beserta dengan nomor urut, nama item, jumlah item, harga per item, 
# dan total harga.        
    def show_transaction(self):
        print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        print("|----|-----------|-------------|------------|-------------|")
        for i, item in enumerate(self.items):
            print(f"| {i+1:<2} | {item[0]:<9} | {item[1]:^11} | {item[2]:^10} | {item[1]*item[2]:^11} |")
# fungsi ini digunakan untuk menghitung total harga belanjaan dari 
# transaksi, serta menampilkan diskon dan total yang harus dibayar 
# berdasarkan total harga yang telah dihitung           
    def total_price(self):
        if self.total >= 500000:
            discount = 0.1
        elif self.total >= 300000:
            discount = 0.08
        elif self.total >= 200000:
            discount = 0.05
        else:
            discount = 0
        discounted_total = self.total * (1 - discount)
        print(f"Total belanja: {self.total}")
        print(f"Diskon: {discount*100:.0f}%")
        print(f"Total yang harus dibayar: {discounted_total}")
