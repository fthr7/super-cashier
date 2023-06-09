import pandas as pd
import module

user_id = input("Mohon masukkan user ID Anda: ")
print(f'Hallo user {user_id}!\nSelamat datang di Super Mart!\n\n')
trnsct_123 = module.Transaction()

def add_item():
    item_name = input("Masukkan nama item: ")
    item_quantity = int(input("Masukkan jumlah item: "))
    item_price = int(input("Masukkan harga item: "))
    trnsct_123.add_item(item_name, item_quantity, item_price)
    menu()

def update_name_item():
    item_index = int(input("Masukkan nomor item yang akan diubah: "))
    new_name = input("Masukkan nama item baru: ")
    trnsct_123.update_name_item(item_index, new_name)
    menu()

def update_quantity_item():
    item_index = int(input("Masukkan nomor item yang akan diubah: "))
    new_quantity = int(input("Masukkan jumlah item baru: "))
    trnsct_123.update_quantity_item(item_index, new_quantity)
    menu()

def update_price_item():
    item_index = int(input("Masukkan nomor item yang akan diubah: "))
    new_price = int(input("Masukkan harga item baru: "))
    trnsct_123.update_price_item(item_index, new_price)
    menu()

def delete_item():
    item_index = int(input("Masukkan nomor item yang akan dihapus: "))
    trnsct_123.delete_item(item_index)
    menu()

def reset_order():
    trnsct_123.reset_order()
    print("Transaksi berhasil direset!")
    menu()

def list_order():
    trnsct_123.list_order()
    menu()

def total_price():
    trnsct_123.total_price()
    menu()

def exit_program():
    print("Terima kasih telah menggunakan program ini!")
    exit()

def menu():
    print("\n------------ Super Cashier -------------")
    print("\n-------------- App Menu ----------------")
    print("""
    1. Add Item
    2. Update Item Name
    3. Update Item Quantity
    4. Update Item Price
    5. Delete Item
    6. Reset Transaction
    7. Check Order
    8. Total Price
    9. Exit
    """)
    print("----------------------------------------\n")

    while True:
        fitur = input("Pilih menu yang ingin dipilih: ")
        if fitur.isdigit() and 1 <= int(fitur) <= 9:
            fitur = int(fitur)
            break
        print("Masukkan angka dari 1 hingga 9")
    
    if fitur == 1:
        add_item()

    elif fitur == 2:
        update_name_item()

    elif fitur == 3:
        update_quantity_item()
    
    elif fitur == 4: 
        update_price_item()

    elif fitur == 5: 
        delete_item()

    elif fitur == 6: 
        reset_order()

    elif fitur == 7: 
        list_order()

    elif fitur == 8: 
        total_price()

    elif fitur == 9: 
        exit_program()

menu()
