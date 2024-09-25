import schedule
import time
from datetime import datetime, timedelta
from user1 import user1
import smtplib

def send_email(gonderen_mail, gonderen_sifre, alici_mail, gonderen_konu, gonderen_mesaj):
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(gonderen_mail, gonderen_sifre)
        print("Gönderici mailine giriş başarılı.")
        message = f"Subject: {gonderen_konu}\n\n{gonderen_mesaj}"
        smtp_server.sendmail(gonderen_mail, alici_mail, message.encode('utf-8'))
        print("Mesajınız gönderildi.")
        smtp_server.quit()
    except smtplib.SMTPAuthenticationError:
        print("Mail giriş bilgileriniz hatalı. Lütfen kontrol edin.")

def zaman():
    tarih = input("E-postayı göndermek için tarihi belirtin (YYYY-AA-GG formatında): ")
    start_time = datetime.strptime(tarih, "%Y-%m-%d")
    return start_time

def planlama(start_time):
    user_info = user1()
    if user_info is None:
        return

    print("Tekrarlama seçenekleri:")
    print("1. Tekrarlama")
    print("2. Haftada bir")
    print("3. Ayda bir")
    print("4. Yılda bir")
    tekrar_secenegi = int(input("Seçiminizi yapın (1-4): "))

    def plan_send_email():
        print(f"E-posta gönderiliyor: {datetime.now()}")
        send_email(user_info.gonderen_mail, user_info.gonderen_sifre, user_info.alici_mail, user_info.gonderen_konu, user_info.gonderen_mesaj)

    if tekrar_secenegi == 1:
        plan_send_email()

    elif tekrar_secenegi == 2:
        tekrar = int(input("E-postanın kaç hafta boyunca gönderileceğini belirtin: "))
        gun_dict = {
            1: "monday",
            2: "tuesday",
            3: "wednesday",
            4: "thursday",
            5: "friday",
            6: "saturday",
            7: "sunday"
        }
        gun = int(input("E-postanın gönderileceği günü belirtin (Pazartesi için 1, Salı için 2, ...): "))
        gun_str = gun_dict.get(gun, "monday")
        for i in range(tekrar):
            schedule_time = start_time + timedelta(weeks=i)
            schedule.every().week.do(plan_send_email).tag(gun_str)
        print(f"E-postalar her hafta {gun_str.capitalize()} günü gönderilecek...")

    elif tekrar_secenegi == 3:
        tekrar = int(input("E-postanın kaç ay boyunca gönderileceğini belirtin: "))
        gun = int(input("E-postanın her ayın hangi gününde gönderileceğini belirtin: "))
        for i in range(tekrar):
            schedule_time = start_time.replace(day=gun) + timedelta(days=i*30)
            schedule.every().month.do(plan_send_email).tag(f"{gun}")
        print(f"E-postalar her ayın {gun}. günü gönderilecek...")

    elif tekrar_secenegi == 4:
        tekrar = int(input("E-postanın kaç yıl boyunca gönderileceğini belirtin: "))
        gun = int(input("E-postanın her yılın hangi gününde gönderileceğini belirtin (Gün): "))
        ay = int(input("E-postanın her yılın hangi ayında gönderileceğini belirtin (Ay): "))
        for i in range(tekrar):
            schedule_time = start_time.replace(month=ay, day=gun) + timedelta(days=i*365)
            schedule.every().year.do(plan_send_email).tag(f"{gun}-{ay}")
        print(f"E-postalar her yılın {gun}/{ay} tarihinde gönderilecek...")

    while True:
        schedule.run_pending()
        time.sleep(1)
