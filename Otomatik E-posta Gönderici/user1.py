from email.message import EmailMessage
class UserInfo:
    def __init__(self, gonderen_mail, gonderen_sifre, alici_mail, gonderen_konu, gonderen_mesaj):
        self.gonderen_mail = gonderen_mail
        self.gonderen_sifre = gonderen_sifre
        self.alici_mail = alici_mail
        self.gonderen_konu = gonderen_konu
        self.gonderen_mesaj = gonderen_mesaj
def user1():
    msg = EmailMessage()

    while True:
        print("Otomatik E-posta Gönderici'ye Hoş Geldin!")
        print("1. Çıkış yap")
        print("2. Devam et")
        num = input("[1-2]=> ")
        if num == "1":
            print("Çıkış yapılıyor..")
            return

        elif num == "2":
            def mailkontrol(email):
                return '@' in email and email.count('@') == 1

            print("Kendi mail adresinizi giriniz:")
            gonderen_mail = input()

            msg['From'] = gonderen_mail

            if mailkontrol(gonderen_mail):
                print('Gönderen Mail Adresi Formatı Doğru')

                print("Girdiğiniz kendi mail adresinizin şifresini giriniz:")
                gonderen_sifre = input()

                print("Alıcı mail adresini giriniz:")
                alici_mail = input()

                msg['To'] = alici_mail

                if mailkontrol(alici_mail):
                    print('Alıcı Mail Adresi Formatı Doğru')

                    print("Lütfen karşı tarafa göndermek istediğiniz mesajın konusunu yazın:")
                    gonderen_konu = input()

                    msg['Subject'] = gonderen_konu

                    print("Lütfen karşı tarafa göndermek istediğiniz mesajı yazın:")
                    gonderen_mesaj = input()

                    msg.set_content(gonderen_mesaj)
                    return UserInfo(gonderen_mail, gonderen_sifre, alici_mail, gonderen_konu, gonderen_mesaj)
            else:
                print('Geçersiz giriş. Tekrar deneyin!')
        else:
            print("Geçersiz giriş. Tekrar deneyin!")
