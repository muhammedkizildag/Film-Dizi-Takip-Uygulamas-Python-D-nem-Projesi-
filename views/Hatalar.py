import customtkinter as cTk

def basarili():
    msg_box = cTk.CTkToplevel()
    msg_box.geometry("300x150+600+450")
    msg_box.title("Basarili")
    msg_box.grab_set()
    cTk.CTkLabel(msg_box, text="Giris Basarali", font=("Roboto", 14), wraplength=280).pack(pady=20)
    cTk.CTkButton(msg_box, text="Tamam", command=msg_box.destroy).pack(pady=10)


def hatali():
    msg_box = cTk.CTkToplevel()
    msg_box.geometry("300x150+600+450")
    msg_box.title("Hatali Giris")
    msg_box.grab_set()
    cTk.CTkLabel(msg_box, text="Boyle Bir Hesap Bulunamadi", font=("Roboto", 14), wraplength=280).pack(pady=20)
    cTk.CTkButton(msg_box, text="Tamam", command=msg_box.destroy).pack(pady=10)


def hataliSifre():
    msg_box = cTk.CTkToplevel()
    msg_box.geometry("300x150+600+450")
    msg_box.title("Hatali Sifre")
    msg_box.grab_set()
    cTk.CTkLabel(msg_box, text="Sifre Yanlis", font=("Roboto", 14), wraplength=280).pack(pady=20)
    cTk.CTkButton(msg_box, text="Tamam", command=msg_box.destroy).pack(pady=10)

def hataliKayit():
    msg_box = cTk.CTkToplevel()
    msg_box.geometry("300x150+600+450")
    msg_box.title("Hatali Kayit")
    msg_box.grab_set()
    cTk.CTkLabel(msg_box, text="Bu kullanici adina sahip bir hesap zaten var", font=("Roboto", 14), wraplength=280).pack(pady=20)
    cTk.CTkButton(msg_box, text="Tamam", command=msg_box.destroy).pack(pady=10)

def basariliKayit():
    msg_box = cTk.CTkToplevel()
    msg_box.geometry("300x150+600+450")
    msg_box.title("Basarili Kayit")
    msg_box.grab_set()
    cTk.CTkLabel(msg_box, text="Kayit Basarili", font=("Roboto", 14), wraplength=280).pack(pady=20)
    cTk.CTkButton(msg_box, text="Tamam", command=msg_box.destroy).pack(pady=10)


def sifrelerUyusmuyor():
    msg_box = cTk.CTkToplevel()
    msg_box.geometry("300x150+600+450")
    msg_box.title("Sifreler Uyusmuyor")
    msg_box.grab_set()
    cTk.CTkLabel(msg_box, text="Sifreler Uyusmuyor Tekrar Deneyiniz", font=("Roboto", 14), wraplength=280).pack(pady=20)
    cTk.CTkButton(msg_box, text="Tamam", command=msg_box.destroy).pack(pady=10)