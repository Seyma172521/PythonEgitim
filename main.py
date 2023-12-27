def armstrongSayi(sayi) :
     string = str(sayi)
     total = 0
     for i in range(len(string)) :
         basamak = int(string[i])
         total = total + (basamak ** (len(string)))

     if total == sayi :
         print("Armstrong sayı")

     else :
         print("Armstrong sayı değil")

sayi = int(input("Bir sayı girin :"))
armstrongSayi(sayi)