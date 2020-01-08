import random#pada match = random......(untuk input mangacak)
print("===Selamat Datang, Mohon Daftarkan Nama Keluarga===")

loop = True
while loop:
    cowok = input("masukkan Nama cowok: ")
    cewek = input("masukkan Nama cewek: ")
    print("==============================")
    print("nama cowok : ",cowok)
    print ("nama cewek : ",cewek)
    confirm = input("Apakah nama yang dimasukkan benar ? y/n : ")
    if confirm=='y':
        print ('Semoga berhasil')
        loop = False
meramal= input("Apakah anda ingin diramal kecocokannya? y/n : ")
if meramal=='y':
    match = random.randrange(0,100)
    print("Match meter",match,"%")
    if match > 80 :
        print("Sangat cocok")
        print("Semoga Beruntung")
    elif match > 60 :
        print("Cukup cocok")
        print("Semoga Beruntung")
    elif match > 40 :
        print("Cocok")
        print("Semoga Beruntung")
    elif match > 20 :
        print("Kurang cocock")
        print("Semoga Beruntung")
    elif match > 0 :
        print("Tidak cocok")
        print("Semoga Beruntung")
  
elif meramal=='n':
    bonus=input("Apakah mau bonus , clue cara jitu ? y/n: ")
    if bonus=='y':
        print("Bonus clue cara jitu")
        clue = ["pdkt","lebih dekati","kode-kode","beri hadiah","beri support"]
        for a in range (len (clue)):
            random.shuffle(clue)
            print (clue[a])

        print("====semoga beruntung====")
       
    elif bonus=='n':
        print("=====semoga beruntung====")