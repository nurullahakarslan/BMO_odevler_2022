#kisiler adli bos bir liste olusturalim
kisiler=[]
#listeye uc kisi ekleyelim
a=input("ilk ismi giriniz: ")
kisiler.append(a)
print (kisiler)
b=input("ikinci ismi giriniz: ")
kisiler.append(b)
print (kisiler)
c=input("ucuncu ismi giriniz: ")
kisiler.append(c)
print (kisiler)
#listeyi yazdiralim
print (kisiler)
#listenin uzunlugunu bulalim
uzunluk=len(kisiler)
print("listenin uzunlugu:",uzunluk)
#listenin 2. elmanini yazdiralim
print ("ikinci elemanin ismi: ",kisiler [1])
#listenin son elemainin silelim
kisiler.pop(2)
#listeyi tekrar yazdiralim
print (kisiler)