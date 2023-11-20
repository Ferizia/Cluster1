import os
import random
import time
#fungsi ascending
def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a(j+1):
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)
    #fungsi Descending
def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)

while True:
    ur_angka = []    

    print("selamat datang ke dalam persortir angka")
    #how_much = int(input("berapa banyak angka yang ingin dibuat"))
    #ur_angka = [how_much]

    choice = str(input("apakah anda ingin membuat sendiri atau random (S/R)")).lower()
    
    print()
    #PILIHAN RANDOM ATAU BUAT SENDIRI
    if choice == "R" or choice == "r" or choice == "random":
        numeric=random.randint(1,5)
        print("please keep in mind the number probality is only from 1-100")
        if numeric == 1:
            num1=random.randint(1,100)
            ur_angka = [num1]
            print(ur_angka)
        elif numeric == 2:
            num1=random.randint(1,100)
            num2=random.randint(1,100)
            ur_angka = [num1,num2,]
            print(ur_angka)
        elif numeric == 3:
            num1=random.randint(1,100)
            num2=random.randint(1,100)
            num3=random.randint(1,100)
            ur_angka = [num1,num2,num3,]
            print(ur_angka)
        elif numeric == 5:
            num1=random.randint(1,100)
            num2=random.randint(1,100)
            num3=random.randint(1,100)
            num4=random.randint(1,100)
            num5=random.randint(1,100)
            ur_angka = [num1,num2,num3,num4,num5]
            print(ur_angka)
        elif numeric == 4:
            num1=random.randint(1,100)
            num2=random.randint(1,100)
            num3=random.randint(1,100)
            num4=random.randint(1,100)
            num5=random.randint(1,100)
            ur_angka = [num1,num2,num3,num4]
            print(ur_angka)

    elif choice == "S" or choice == "s" or choice == "sendiri":
        a = int(input("masukan angka pertama : "))
        b = int(input("masukan angka kedua : "))
        c = int(input("masukan angka ketiga : "))
        d = int(input("masukan angka keempat : "))
        e = int(input("masukan angka kelima : "))
        ur_angka = [a,b,c,d,e]
    else:
        print("maaf program error")
        break
    assorted = input("Apakah Anda ingin pengurutan Ascending/Descending (A/D) atau keduanya (B): ").lower()
    if assorted == "a" or assorted == "ascending":
        print("sebelum pengururutan",ur_angka)
        print("Sorted array in ascending order:")
        urutdesc(ur_angka)
        minimum = min(ur_angka)
        maximum = max(ur_angka)
        summary = sum(ur_angka)
        print("nilai minimum dari pengurutan :",minimum)
        print("nilai maximum dari pengurutan",maximum)
        print("nilai rata-rata dari pengurutan",summary)
    elif assorted == "d" or assorted == "descending":
        print("sebelum pengururutan",ur_angka)
        urutasc("Sorted array in descending order:" +ur_angka)
        ur_angka.reverse()
        
        minimum = min(ur_angka)
        maximum = max(ur_angka)
        summary = sum(ur_angka)/len(ur_angka)
        print("nilai minimumnya",minimum)
        print("nilai maximumnya",maximum) 
        print("nilai rata-rata",summary)
    elif assorted == "b":
        n = len (ur_angka)
        for i in range(n):
        # Last i elements are already in place, so we don't need to check them
            for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
                if ur_angka[j] > ur_angka[j + 1]:
                    ur_angka[j], ur_angka[j + 1] = ur_angka[j + 1], ur_angka[j]
        print("Sorted array in ascending order:", ur_angka)
        ur_angka.reverse()
        print("Sorted array in descending order:", ur_angka)
        minimum = min(ur_angka)
        maximum = max(ur_angka)
        summary = sum(ur_angka)
        print("ini nilai minimumnya",minimum)
        print("ini nilai maximumnya",maximum)
        print("ini nilai rata-rata",summary)

    #program akan di clear setiap retry (jika tidak ingin hilangkan clear)
    retry = str(input("ingin mengulang(Y/N)?"))
    if retry == "Y":
        print("data will be reset in 3 second")
        time.sleep(3)
        os.system("cls")
        continue
    elif retry == "N":
        print("Thank you for starting the program")
        break