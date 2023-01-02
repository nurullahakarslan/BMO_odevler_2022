
#ilk önce sizin yolladığınız tabloyu sinav_sonuc diye sözlük oluşturdum
sinav_sonuc ={'isimler':['Ayşe K.','ahmet m.','nuri c.','nawar t.','suzan t.','ala b.'],
'cinsiyet':['k','e','e','e','k','k'],
'türkçe':[90,50,53,100,98,66],
'matematik':[80,60,77,25,36,75]


}
#sonra ortalamaları hesaplamaları için değerler oluşturdum

kadinort=0
erkekort=0
erkek=[]
kadin=[]
erkekmat=0
erkekturk=0
kadinmat=0
kadinturk=0

for i in range(len(sinav_sonuc['cinsiyet'])):
    if(sinav_sonuc['cinsiyet'][i]=='e'):
      erkekort+=1
      erkekmat=erkekmat+sinav_sonuc['matematik'][i]
      erkekturk=erkekturk+sinav_sonuc['türkçe'][i]
      erkek.append(sinav_sonuc['türkçe'][i])


    else:
      kadinort+=1
      kadinmat=kadinmat+sinav_sonuc['matematik'][i]
      kadinturk=kadinturk+sinav_sonuc['türkçe'][i]
      kadin.append(sinav_sonuc['türkçe'][i])
    
#ortalama hesaplamayı ekrana yazdırmasını sağlıyoruz
print(f'erkeklerin matematik ortalaması: ',(erkekmat/erkekort))
print(f'kadınların matematik ortalaması: ',(kadinmat/kadinort))
print(f'kursun toplam türkçe ortalaması: ',(((erkekturk+kadinturk)/(kadinort+erkekort))))

#kadın ve erkeğin tükçede aldıkları en yüksek puanı ekrana yazdırmasını sağlıyoruz
print('türkçede erkeklerde en yüksek alınan puan: ',max(erkek))
print('türkçede kadınlarda en yüksek alınan puan: ',max(kadin))



