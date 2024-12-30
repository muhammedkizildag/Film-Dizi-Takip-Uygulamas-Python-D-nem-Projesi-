import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as cTk
import json
import Hatalar

JSON_KULLANICI = "KullaniciDataBase.json"

Kayitli_Hesaplar = {}

aktif_kullanici = None

def verileri_yukle():
    global Kayitli_Hesaplar
    try:
        with open(JSON_KULLANICI, "r") as jkul:
            Kayitli_Hesaplar = json.load(jkul)
    except FileNotFoundError:
        Kayitli_Hesaplar = {}

def kullanici_Kaydet():
    with open(JSON_KULLANICI, "w") as jkul:
        json.dump(Kayitli_Hesaplar, jkul, indent=4)


def giris():
    global aktif_kullanici
    name = kullanici_entry.get()
    password = sifre_entry.get()

    if name in Kayitli_Hesaplar and Kayitli_Hesaplar[name] == password:
        aktif_kullanici = name
        Hatalar.basarili()
        ana_ekran()
    else:
        if name in Kayitli_Hesaplar and Kayitli_Hesaplar[name] != password:
            Hatalar.hataliSifre()
            sifre_entry.delete(0, tk.END)
        else:
            Hatalar.hatali()
            kullanici_entry.delete(0, tk.END)
            sifre_entry.delete(0, tk.END)

def kayitOl(kayit, kullanici_adi_entry, ksifre_entry, ksifreTekrar_entry):
    kullanici_adi = kullanici_adi_entry.get()
    sifre = ksifre_entry.get()
    sifreTekrar = ksifreTekrar_entry.get()

    if kullanici_adi in Kayitli_Hesaplar:
        Hatalar.hataliKayit()
    else:
        if sifre == sifreTekrar:
            Kayitli_Hesaplar[kullanici_adi] = sifre
            Hatalar.basariliKayit()
            kullanici_Kaydet()
            kayit.destroy()
        else:
            Hatalar.sifrelerUyusmuyor()


def kayitEkran():
    kayit = cTk.CTkToplevel(form)
    kayit.title("Kayit Ol")
    kayit.geometry("400x350+600+350")
    kayit.config(bg="#101014")
    kayit.iconbitmap("moovie3.ico")
    kayit.resizable(width=False, height=False)
    kayit.grab_set()

    def hover_in3(event):
        kayitOl_button.configure(text="MoOoOo")

    def hover_out3(event):
        kayitOl_button.configure(text="Kayit Ol")

    cTk.CTkLabel(kayit, text="Kayit Ol", bg_color="#101014", font=font).pack(pady=20)

    cTk.CTkLabel(kayit, text="Kullanıcı Adı: ", bg_color="#101014", font=("Roboto", 12)).place(x=100, y=70)

    kullanici_adi_entry = cTk.CTkEntry(kayit)
    kullanici_adi_entry.place(x=180, y=70)

    cTk.CTkLabel(kayit, text="Sifre Olusturun: ", bg_color="#101014", font=("Roboto", 12)).place(x=85, y=120)

    ksifre_entry = cTk.CTkEntry(kayit, show="*")
    ksifre_entry.place(x=180, y=120)

    cTk.CTkLabel(kayit, text="Sifrenizi Dogrulayin: ", bg_color="#101014", font=("Roboto", 12)).place(x=63, y=170)

    ksifreTekrar_entry = cTk.CTkEntry(kayit, show="*")
    ksifreTekrar_entry.place(x=180, y=170)

    kayitOl_button = cTk.CTkButton(kayit, text="Kayit Ol", fg_color= "white", hover_color="grey", text_color="black", command=lambda: kayitOl(kayit, kullanici_adi_entry, ksifre_entry, ksifreTekrar_entry))
    kayitOl_button.place(x=165, y=220)

    kayitOl_button.bind("<Enter>", hover_in3)
    kayitOl_button.bind("<Leave>", hover_out3)

    kayit.mainloop()


def ana_ekran():
    global aktif_kullanici
    form.destroy()

    mainS = cTk.CTk()
    mainS.title("Ana Ekran")
    mainS.geometry("950x600+500+200")
    mainS.iconbitmap("moovie3.ico")

    bilgi_label = cTk.CTkLabel(mainS, text=f"{aktif_kullanici} HOS GELDINIZ")
    bilgi_label.pack(pady=10)

    cikis_button = cTk.CTkButton(mainS, text="Cikis", fg_color= "white", hover_color="grey", text_color="black", command=mainS.quit)
    cikis_button.pack(side = tk.BOTTOM)

    oturum_kapat = cTk.CTkButton(mainS, text="Oturumu Kapat", fg_color= "white", hover_color="grey", text_color="black", command=mainS.quit)
    oturum_kapat.pack(side=tk.BOTTOM)

    mainS.mainloop()

form = cTk.CTk()
verileri_yukle()
form.title("Giriş")
form.config(bg="#101014")
form.geometry("450x550+500+250")
form.resizable(width=False, height=False)

font = ("Roboto", 16)

image = Image.open("../database/pics/moovie3.png")
image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)
photo_label = cTk.CTkLabel(form, image=photo, text="")
photo_label.place(x=126, y=40)
form.iconbitmap("../database/pics/moovie3.ico")

def hover_in(event):
    giris_button.configure(text="MoOoOo")

def hover_out(event):
    giris_button.configure(text="Giris")

def hover_in2(event):
    kayit_buton.configure(text="MoOoOo")

def hover_out2(event):
    kayit_buton.configure(text="Kayit Ol")


cTk.CTkLabel(form, text="Kullanıcı Adı", bg_color="#101014",font=font).place(x=150, y=250)

kullanici_entry = cTk.CTkEntry(form, width=150, font=("Roboto", 12))
kullanici_entry.place(x=150, y=282)

cTk.CTkLabel(form, text="Sifre", bg_color="#101014",font=font).place(x=150, y=325)

sifre_entry = cTk.CTkEntry(form, show="*", width=150, font=("Roboto", 12))
sifre_entry.place(x=150, y=357)

giris_button = cTk.CTkButton(form, text="Giris",width = 100, height = 30, fg_color= "white", hover_color="grey", text_color="black", command=giris)
giris_button.place(x=170, y=410)

giris_button.bind("<Enter>", hover_in)
giris_button.bind("<Leave>", hover_out)

kayit_buton = cTk.CTkButton(form, text="Kayit Ol",width = 100, height = 30, fg_color= "white", hover_color="grey", text_color="black", command=kayitEkran)
kayit_buton.place(x=170, y=450)

kayit_buton.bind("<Enter>", hover_in2)
kayit_buton.bind("<Leave>", hover_out2)

form.mainloop()

