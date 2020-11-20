def kasir():
    print("List Kue yang tersedia di Toko Sule:")
    print("Harga 1 kue keju = Rp.6000")
    print("Harga 1 kue coklat = Rp.3500")
    print("Setiap Hari, Kami hanya memproduksi 25 kue keju")
    print("Setiap Hari, Kami hanya memproduksi 35 kue coklat")
    print("\nKami Punya Promo Menarik Untukmu:")
    print("Kalo Kamu beli 5 kue coklat hingga 20, Kamu mendapat diskon 7%")
    print("Jika Kamu membeli 21 kue coklat hingga 35, Kamu mendapat diskon 12%")
    print("Kalo Kamu membeli 4 kue keju hingga 15, Kamu mendapat diskon 10%")
    print("Jika Kamu membeli 16 kue keju hingga 25 maka Kamu mendapat diskon 25%")
    total_kue_coklat = int(input("Mau beli berapa kue coklat? "))
    total_kue_keju = int(input("Mau beli berapa kue keju? "))
    print("\n")
    if(total_kue_coklat >= 1 and total_kue_coklat <= 4):
        harga_kue_coklat = 3500 * total_kue_coklat
        print("Total pembelian kue coklat: %d" % (total_kue_coklat))
        print("Total harga kue coklat: Rp. %d" % (harga_kue_coklat))
    elif(total_kue_coklat >= 5 and total_kue_coklat <= 20):
        harga_kue_coklat = 3500 * total_kue_coklat
        diskon_kue_coklat = harga_kue_coklat*7/100
        total_harga_kue_coklat = harga_kue_coklat-diskon_kue_coklat
        print("Total pembelian kue coklat: %d" % (total_kue_coklat))
        print("Total harga kue coklat: Rp. %d" % (harga_kue_coklat))
        print("Potongan diskon kue coklat: Rp. %d" % (diskon_kue_coklat))
        print("Total harga setelah diskon: Rp. %d" % (total_harga_kue_coklat))
    elif(total_kue_coklat >= 21 and total_kue_coklat <= 35):
        harga_kue_coklat = 3500 * total_kue_coklat
        diskon_kue_coklat = harga_kue_coklat*12/100
        total_harga_kue_coklat = harga_kue_coklat-diskon_kue_coklat
        print("total pembelian kue coklat: %d" % (total_kue_coklat))
        print("total harga kue coklat: Rp. %d" % (harga_kue_coklat))
        print("potongan diskon kue coklat: Rp. %d" % (diskon_kue_coklat))
        print("total harga setelah potongan diskon kue coklat; Rp. %d" % (total_harga_kue_coklat))
    elif(total_kue_coklat == 0):
        total_harga_kue_coklat = 0
        print("tidak membeli kue coklat")    
    else:
        print("jumlah kue tidak tersedia")
        kasir()

    if(total_kue_keju >= 1 and total_kue_keju <= 3):
        harga_kue_keju = 6000 * total_kue_keju
        print("total pembelian kue keju: %d" % (total_kue_keju))
        print("total harga kue keju: Rp. %d" % (harga_kue_keju))
    
    elif(total_kue_keju >= 4 and total_kue_keju <= 15):
        harga_kue_keju = 6000 * total_kue_keju
        diskon_kue_keju = harga_kue_keju*10/100
        total_harga_kue_keju = harga_kue_keju-diskon_kue_keju
        print("total pembelian kue keju: %d" % (total_kue_keju))
        print("total harga kue keju: Rp. %d" % (harga_kue_keju))
        print("potongan diskon kue keju: Rp. %d" % (diskon_kue_keju))
        print("total harga setelah potongan diskon kue keju: Rp. %d" % (total_harga_kue_keju))
    
    elif(total_kue_keju >= 16 and total_kue_keju <= 25):
        harga_kue_keju = 6000 * total_kue_keju
        diskon_kue_keju = harga_kue_keju*25/100
        total_harga_kue_keju = harga_kue_keju-diskon_kue_keju
        print("total pembelian kue keju: %d" % (total_kue_keju))
        print("total harga kue keju: Rp. %d" % (harga_kue_keju))
        print("potongan diskon kue keju: Rp. %d" % (diskon_kue_keju))
        print("total harga setelah potongan diskon kue keju; Rp. %d" % (total_harga_kue_keju))
    
    elif(total_kue_keju == 0):
        total_harga_kue_keju = 0
        print("tidak membeli kue keju")
    
    else:
        print("jumlah kue tidak tersedia")
        kasir()
    total_semua_kue = total_harga_kue_coklat + total_harga_kue_keju
    print("Jumlah total harga semua kue: Rp. %d" % (total_semua_kue)) 
    bayar = float(input("Total Bayar> "))
    kembalian = bayar-total_semua_kue
    
    if(bayar >= total_semua_kue):
        print("Kembalian: Rp. %d" % (kembalian))
        print("Terima kasih telah membeli kue kami")
kasir()
