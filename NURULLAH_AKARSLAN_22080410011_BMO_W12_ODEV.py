"""hocam olabildiğince farklı ve bilerekten uzun bir kod yazdım.
 
umarım önceki gibi ödevden 30 almam çünkü bunun için çok uğraştım.

eğer bu sefer kime benzediyse lütfen söyleyiniz"""


#ödevdeki tabloyu bahsedildiği gibi sinav_sonuc sözlüğe yerleştiriyoruz 
sinav_sonuc = {
    'isim': ['Ayşe K.', 'Ahmet M.', 'Nuri C.', 'Nawar T.', 'Suzan T.', 'Ala B.'],
    'cinsiyet': ['K', 'E', 'E', 'E', 'K', 'K'],
    'vize': [80, 60, 77, 25, 36, 75],
    'final': [90, 50, 53, 100, 98, 66]
}
# sonrasında vize ve final hesaplaması için  gecme_notu diye fonksiyon yaratıyoruz
def gecme_notu(vize, final):
  try:
      vize = int(vize)
      final = int(final)
  except ValueError:
      return None
  return (vize*30/100)+(final*70/100)

# Geçme notlarını hesaplayıp sözlükteki verilere ekleyelim
sinav_sonuc['gecme_notu'] = [gecme_notu(vize, final) for vize, final in zip(sinav_sonuc['vize'], sinav_sonuc['final'])]
# sonrasında ise isim, cinsiyet, vize, final ve geçme notunu kaydeden bir kaydet fonksiyonu oluşturuyoruz 
def kaydet(isim, cinsiyet, vize, final):
  sinav_sonuc['isim'].append(isim)
  sinav_sonuc['cinsiyet'].append(cinsiyet)
  sinav_sonuc['vize'].append(int(vize))
  sinav_sonuc['final'].append(int(final))
  sinav_sonuc['gecme_notu'].append(gecme_notu(vize, final))

# Kullanıcıdan 2 yeni kayıt almasını istiyoruz. eğer kulllanıcı hatalı girerse uyarı verecek şekilde bir döngü yaratıyoruz.
for i in range(2):
  
  isim = input("\nÖğrencinin ismi: ")
  cinsiyet = input("\nÖğrencinin cinsiyeti (K/E): ")
  while cinsiyet.upper() != 'E' and cinsiyet.upper() != 'K':
    cinsiyet = input("\nLütfen doğru cinsiyetini giriniz K/E: ")

  vize = input("\nÖğrencinin vize notu: ")
  while not isinstance(vize, int):
    try:
        vize = int(vize)
    except ValueError:
        vize = input("\nLütfen düzgün vize notu giriniz: ")

  final = input("\nÖğrencinin final notu: ")
  while not isinstance(final, int):
    try:
        final = int(final)
    except ValueError:
        final = input("\nLütfen düzgün final notu giriniz: ")
# kullanıcıdan aldığımız verileri kaydet fonksiyonuna gönderiyoruz
  kaydet(isim, cinsiyet.upper(), vize, final)


# sinav_sonuc sözlüğündeki verileri kullanarak bir tablo oluşturuyoruz
def print_table(data):
  # Sütun başlıklarını ekrana yazdırıyoruz
  print("\nIsim".ljust(20) + "Cinsiyet".ljust(10) + "Vize".ljust(10) + "Final".ljust(10) + "Geçme Notu".ljust(10))
  print("-" * 60)
  
  # Verileri ekrana yazdırıyoruz
  for i in range(len(data['isim'])):
    print(data['isim'][i].ljust(20) + data['cinsiyet'][i].ljust(10) + str(data['vize'][i]).ljust(10) + str(data['final'][i]).ljust(10) + str(data['gecme_notu'][i]).ljust(10))

# Tabloyu ekrana yazdırın
print_table(sinav_sonuc)

