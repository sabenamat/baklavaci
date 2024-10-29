import time
import os


ürünler = {"Fıstıklıbaklava":["1000","100"]}
yönetici= {"fahri":"1234"}
sorumlu={}
kullanıcı={}
sepet={}


def ürünekle(ürün,fiyat,stok):
    ürünler[ürün] = fiyat,stok
def ürünsil(ürün):
    del ürünler[ürün]
def sorumluekle(isim,sifre):
    sorumlu[isim] = sifre
def sorumlusil(isim):
    del sorumlu[isim]
def kullanıcıekle(isim,sifre):
    kullanıcı[isim] = sifre
def kullanıcısil(isim):
    del kullanıcı[isim]
def sepetekle(ürün,fiyat,adet):
    sepet[ürün] = fiyat, adet
def sepetsil(ürün,adet):
    if adet>sepet[ürün][1]:
        del sepet[ürün]
    else:
        sepet[ürün][1]-= adet

def program():
    while True:
        secim=int(input("...Baklavacıoğlu Dessert'e Hoşgeldiniz...\n1-Admin Girişi\n2-Yetkili Girişi\n3-Kullanıcı Girişi\nGiriş İşleminizi Seçiniz:\t"))
        sayac = 0
        if secim==1:
            while True:
                k_ad=str(input("Kullanıcı Adı:\t"))
                sifre=str(input("Şifre:\t"))
                if k_ad in yönetici:
                    if sifre==yönetici[k_ad]:
                        print("Giriş Başarılı. Admin Ekranına yönlendiriliyorsunuz..")
                        time.sleep(2)
                        while True:
                            adminsecim=int(input("1-Mağaza Sorumlu Ekle\n2-Mağaza Sorumlu Sil\n3-Çıkış\nYapmak İstediğiniz İşlemi Seçiniz:\t"))
                            if adminsecim==1:
                                sorumluad=str(input("Sorumlu İsmi Giriniz:\t"))
                                sorumlusifre=str(input("Sorumlu Sifre Giriniz:\t"))
                                if sorumluad in sorumlu:
                                    print("Sorumlu adı, sisteme kayıtlı lütfen geçerli bir ad giriniz...")
                                else:
                                    print("Sorumlu Kayıt İşlemi Başarıyla Tamamlandı")
                                    sorumluekle(sorumluad,sorumlusifre)
                                    time.sleep(2)
                                    continue
                            elif adminsecim==2:
                                if len(sorumlu)==0:
                                    print("Sistemde kayıtlı sorumlu bulunmamaktadır. Admin ekranına yönlendiriliyorsunuz..")
                                    time.sleep(2)
                                    continue
                                else:
                                    sorumluad = str(input("Sorumlu İsmi Giriniz:\t"))
                                    sorumlusil(sorumluad)
                                    print("Sorumlu silme işlemi başarıyla tamamlandı")
                                    time.sleep(2)
                            elif adminsecim==3:
                                print("Çıkış Yapılıyor...")
                                time.sleep(2)
                                break

                        break
                        break
                    else:
                        sayac+=1
                        print("Kullanıcı adı veya şifre yanlış! Lütfen tekrar deneyiniz...")
                        if sayac==3:
                            print("Tekrar Hakkınız Doldu. Ana ekrana yönlendiriliyorsunuz...")
                            break
        elif secim==2:
            while True:
                k_ad=str(input("Kullanıcı Adı:\t"))
                sifre=str(input("Şifre:\t"))
                if k_ad in sorumlu:
                    if sifre==sorumlu[k_ad]:
                        print("Giriş Başarılı. Yetkili Ekranına yönlendiriliyorsunuz..")
                        time.sleep(2)
                        while True:
                            sorumlusecim=int(input("1-Ürün Ekle\n2-Ürün Sil\n3-Fiyat Güncelle\n4-Çıkış"))
                            if sorumlusecim==1:
                                ürün_adı=str(input("Ürün Adını Giriniz:\t"))
                                ürün_fiyat=int(input("Ürün Fiyatı Giriniz:\t"))
                                ürün_stok=int(input("Ürün Stoğunu Giriniz:\t"))
                                if ürün_adı in ürünler:
                                    print("Ürün Sistemde Kayıtlı. Lütfen Güncellemeyi Deneyin.")
                                else:
                                    ürünekle(ürün_adı,ürün_fiyat,ürün_stok)
                                    print("Ürün Ekleme Başarıyla Tamamlandı.")
                                    time.sleep(2)
                            elif sorumlusecim==2:
                                
                                if len(ürünler)==0:
                                    print("Sistemde Kayıtlı Ürün bulunmamaktadır. Silme İşlemi Başarısız...")
                                else:
                                    ürün_adı=str(input("Ürün Adını Giriniz:\t"))
                                    if ürün_adı in ürünler:
                                        ürünsil(ürün_adı)
                                        print("ürün silme işlemi başarıyla tamamlandı.")
                                        time.sleep(2)
                                    else:
                                        print("Ürün Adı Sistemde Bulunamadı. Lütfen Tekrar Deneyiniz.")
                                        time.sleep(2)
                                
                            elif sorumlusecim==3:
                                ürün_adı=str(input("Ürün Adını Giriniz:\t"))
                                if ürün_adı in ürünler:
                                    ürün_fiyat=int(input("Yeni Ürün Fiyatı Giriniz:\t"))
                                    ürün_stok=int(input("Yeni Ürün Stoğunu Giriniz:\t"))
                                    ürünsil(ürün_adı)
                                    ürünekle(ürün_adı,ürün_fiyat,ürün_stok)
                                else:
                                    print("Ürün Sistemde Bulunamadı...")
                                    
                                
                            elif sorumlusecim==4:
                                print("Çıkış Yapılıyor...")
                                time.sleep(2)
                                break
                            else:
                                print("Lütfen Geçerli Bir Seçim Yapınız...")
                                
                        break

        elif secim==3:
            sayac=0
            while True:
                kullanıcısecim=int(input("Kullanıcı Ekranına Hoşgeldiniz...\n1-Kullanıcı kaydı\n2-Kullanıcı Girişi\nİşleminizi Seçiniz:\t"))
                if kullanıcısecim==1:
                    while True:
                        if sayac==5:
                            print("5 defa hatalı giriş yapıldı. Lütfen 10 saniye bekleyiniz")
                            time.sleep(10)
                            sayac=0
                        kullanıcıad=str(input("Lütfen Kullanıcı Adınızı Giriniz:\t"))
                        for i in range(len(kullanıcıad)):
                            if i == kullanıcıad[i]:
                                print("Kullanıcı İsimlerinde Rakam Kullanılamaz")
                                sayac+=1
                                break
                            elif "@" not in kullanıcıad:
                                print("Mail Adresinde Hata Var Lütfen Tekrar Deneyiniz.")
                                sayac+=1
                                break
                            elif kullanıcıad[-4]!=".":
                                print("Lütfen Geçerli Bir Mail Adresi Giriniz.")
                                sayac += 1
                                break
                            elif kullanıcıad in kullanıcı:
                                print("Girilen Mail Sistemimizde Kayıtlıdır. Lütfen Başka Bir Mail Adresi Giriniz..")
                                sayac += 1
                                break
                            else:
                                sifre=str(input("Lütfen Şifrenizi Giriniz:\t"))
                                if len(sifre)<8:
                                    print("Min. Şifre Uzunluğu 8 Karakter Olmalıdır.")
                                    sayac += 1
                                    continue
                                kullanıcıekle(kullanıcıad,sifre)
                                print("Kullanıcı Kaydı Başarıyla Oluşturuldu. Ana Ekrana Yönlendiriliyorsunuz...")
                                time.sleep(2)
                                break
                        break




                            
program()
                        
                


