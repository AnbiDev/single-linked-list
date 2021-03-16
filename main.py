import os 
# Membuat class untuk node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.wisata = data['wisata']
        self.harga = data['harga']
        self.alamat = data['alamat']
        self.next_node = next_node

    def get_next(self):
        return self.next_node
   
    # Menentukan node berikutnya
    def set_next(self, new_next):
        self.next_node = new_next
       
# Membuat class untuk linked list
class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail= tail
            
    def tambahbelakang(self, data):
        # Inisialisasi node baru
        new_node = Node(data)
        # jika head masih kosong
        if (self.head is None):
            self.head=new_node
            self.tail=new_node
        else :
            self.tail.next_node=new_node
            self.tail=new_node

    # Menampilkan isi dari list
    def showData(self):
        print ("Tampilkan list data:")
        print ("Node -> Next Node")
        current_node = self.head
        if (self.head is None):
            print("Data masih Kosong")
        else:    
            while current_node is not None:
                print ("Wisata: {}  |  Harga: Rp.{}  |  Alamat: {}".format(current_node.wisata, current_node.harga, current_node.alamat), end="")
                if(current_node.next_node is not None) :
                  print (" -> ", end="")
                  print ("Wisata: {}  |  Harga: Rp.{}  |  Alamat: {}".format(current_node.next_node.wisata, current_node.next_node.harga, current_node.next_node.alamat, end=""))
                current_node = current_node.next_node
    def delMid(self):
        if(self.head is None or self.head.next_node is None):
            return
        slow_point=self.head
        fast_point=self.head
        prev=None
        while(fast_point is not None and fast_point.next_node is not None):
            fast_point=fast_point.next.next
            prev=slow_point
            slow_point=slow_point.next
        prev.next=slow_point.next
    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            # os.system("clear")
            print("===============================")
            print("|  Menu aplikasi linked list  |")
            print("===============================")
            print("1. Tambah Belakang")
            print("2. Tampil Data")
            print("3. Delete tengah")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("cls")
                wisata = str(input("Masukan Nama Wisata yang ingin anda tambahkan: "))
                harga = str(input("Masukan Harga tiket masuk wisata tersebut Rp.: "))
                alamat = str(input("Masukan Alamat Wisata: "))
                self.tambahbelakang({
                  "wisata": wisata,
                  "harga": harga,
                  "alamat": alamat
                })
            elif(pilihan=="2"):
                os.system("cls")
                self.showData()
                x = input("")
            elif(pilihan=="3"):
                self.delMid()
            else:
                pilih="n"
				
if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.mainmenu()
