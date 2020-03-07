from tkinter import *
from tkinter import messagebox

#konfigurasi Frame
master = Tk()
master.title("Daftar Harga Makanan & Minuman")
master.geometry('1280x720')
master.resizable(0, 0)
master.bg = PhotoImage(file ='img/background.gif')
bg = Label(image=master.bg)
master.wm_iconbitmap('img/icon.ico')
bg.place(x=0,y=0)

#list makanan
makanan = ['Nasi Goreng',"Bakmi Jawa","Nasi Tiwul","Gatot","Gudeg"]
makanan_harga = [10000, 10000, 10000,7000, 10000]

#konfigurasi nama makanan
#menu makanan, Harga & Qty
makanan_menu = Label(master,
                     font="times 17 bold",
                     text="Makanan\tHarga\t     Qty",
                     bg = 'sienna4' ,
                     fg = 'black')
makanan_menu.place(x=150, y=250)
#menu Jumlah
jumlah_menu = Label(master,
                    font="times 17 bold",
                    text="Jumlah",
                    bg = 'sienna4' ,
                    fg = 'black')
jumlah_menu.place(x=535, y=250)

#Nama Makanan, Harga & entry buat Qty
#nasi Goreng
nasi_goreng = Label(master,
                    font="times 12",
                    bg = 'sienna4' ,
                    text=makanan[0]+"\t\tRp 10.000       X")
nasi_goreng.place(x=150, y=295)
nasi_goreng_entry = Entry(master,
                          justify=CENTER,
                          bg = 'sienna4' ,
                          width =3)
nasi_goreng_entry.place(x=480, y=295)
#Bakmi jawa
bakmi_jawa = Label(master,
                   font="times 12",
                   bg = 'sienna4' ,
                   text=makanan[1]+"\t\tRp 10.000       X")
bakmi_jawa.place(x=150, y=325)
bakmi_jawa_entry= Entry(master,
                        justify=CENTER,
                        bg = 'sienna4' ,
                        width =3)
bakmi_jawa_entry.place(x=480, y=325)
#Nasi Tiwul
nasi_tiwul = Label(master,
                   font="times 12",
                   bg = 'sienna4' ,
                   text=makanan[2]+"\t\tRp 10.000       X")
nasi_tiwul.place(x=150, y=355)
nasi_tiwul_entry= Entry(master,
                        justify=CENTER,
                        bg = 'sienna4' ,
                        width =3)
nasi_tiwul_entry.place(x=480, y=355)
#Gatot
gatot = Label(master,
              font="times 12",
              bg = 'sienna4' ,
              text=makanan[3]+"\t\t\tRp 7.000         X")
gatot.place(x=150, y=385)
gatot_entry= Entry(master,
                   justify=CENTER,
                   bg = 'sienna4' ,
                   width =3,)
gatot_entry.place(x=480, y=385)
gudeg = Label(master,
              font="times 12",
              bg = 'sienna4' ,
              text=makanan[4]+"\t\t\tRp 10.000       X")
gudeg.place(x=150, y=415)
#Gudeg
gudeg_entry= Entry(master,
                   justify=CENTER,
                   bg = 'sienna4',
                   width =3)
gudeg_entry.place(x=480, y=415)
#Mengisi default Qty dengan 0
gudeg_entry.insert(END,'0')
gatot_entry.insert(END,'0')
nasi_tiwul_entry.insert(END,'0')
nasi_goreng_entry.insert(END,'0')
bakmi_jawa_entry.insert(END,'0')

#List Minuman
minuman = ["Es Tape","Es Teh","ES Jeruk","Es Campur","Kopi Jos"]
minuman_harga = [7000, 2000, 3000, 7000, 10000]

#Konfigurasi Nama Makanan
#Menu Minuman, Harga & Qty
minuman_menu = Label(master,
                     font="times 17 bold",
                     text="Minuman\tHarga\t     Qty",
                     bg = 'sienna4' ,
                     fg = 'black')
minuman_menu.place(x=150, y=455)
#menu Jumlah
jumlah_menu = Label(master,
                    font="times 17 bold",
                    text="Jumlah",
                    bg = 'sienna4' ,
                    fg = 'black')
jumlah_menu.place(x=535, y=455)
#Es Tape
tape = Label(master,
             font="times 12",
             bg = 'sienna4' ,
             text=minuman[0]+"\t\t\tRp 7000          X")
tape.place(x=150, y=500)
tape_entry = Entry(master,
                   justify=CENTER,
                   bg = 'sienna4' ,
                   width =3)
tape_entry.place(x=480, y=500)
#Es Teh
teh = Label(master,
            font="times 12",
            bg = 'sienna4' ,
            text=minuman[1]+"\t\t\tRp 2000          X")
teh.place(x=150, y=530)
teh_entry = Entry(master,
                  justify=CENTER,
                  bg = 'sienna4' ,
                  width =3)
teh_entry.place(x=480, y=530)
#Es Jeruk
jeruk = Label(master,
              font="times 12",
              bg = 'sienna4' ,
              text=minuman[2]+"\t\t\tRp 3000          X")
jeruk.place(x=150, y=560)
jeruk_entry = Entry(master,
                    justify=CENTER,
                    bg = 'sienna4' ,
                    width =3)
jeruk_entry.place(x=480, y=560)
#Es Campur
campur = Label(master,
               font="times 12",
               bg = 'sienna4' ,
               text=minuman[3]+"\t\tRp 7000          X")
campur.place(x=150, y=590)
campur_entry= Entry(master,
                    justify=CENTER,
                    bg = 'sienna4' ,
                    width =3)
campur_entry.place(x=480, y=590)
#Kopi Jos
kopi = Label(master,
             font="times 12",
             bg = 'sienna4' ,
             text=minuman[4]+"\t\t\tRp 10.000       X")
kopi.place(x=150, y=620)
kopi_entry= Entry(master,
                  justify=CENTER,
                  bg = 'sienna4' ,
                  width =3)
kopi_entry.place(x=480, y=620)
#Menigisi default Qty dengan 0
teh_entry.insert(END, 0)
tape_entry.insert(END, 0)
jeruk_entry.insert(END, 0)
campur_entry.insert(END, 0)
kopi_entry.insert(END, 0)

#konfigurasi total
def total_call():
    nasi_goreng_harga = int(nasi_goreng_entry.get())
    bakmi_jawa_harga = int(bakmi_jawa_entry.get())
    nasi_tiwul_harga = int(nasi_tiwul_entry.get())
    gatot_harga = int(gatot_entry.get())
    gudeg_harga = int(gudeg_entry.get())
    tape_harga = int(tape_entry.get())
    teh_harga = int(teh_entry.get())
    jeruk_harga = int(jeruk_entry.get())
    campur_harga = int(campur_entry.get())
    kopi_harga = int(kopi_entry.get())
    global total_harga
    total_harga = nasi_goreng_harga * makanan_harga[0] \
                  + bakmi_jawa_harga * makanan_harga[1] \
                  + nasi_tiwul_harga * makanan_harga[2] \
                  + gatot_harga * makanan_harga[3] \
                  + gudeg_harga * makanan_harga[4] \
                  + tape_harga * minuman_harga[0] \
                  + teh_harga * minuman_harga[1] \
                  + jeruk_harga * minuman_harga[2] \
                  + campur_harga * minuman_harga[3] \
                  + kopi_harga * minuman_harga[4]

    #konfigurasi untuk memanggil total biaya
    total_biaya.delete(first=0, last=1000)
    total_biaya.insert("end", "Rp ")
    total_biaya.insert("end", total_harga)

    nasi_goreng_jml = nasi_goreng_harga * makanan_harga[0]
    nasi_goreng_total.delete(first=0, last=1000)
    nasi_goreng_total.insert("end", "Rp ")
    nasi_goreng_total.insert("end", nasi_goreng_jml)

    bakmi_jawa_jml = bakmi_jawa_harga * makanan_harga[1]
    bakmi_jawa_total.delete(first=0, last=1000)
    bakmi_jawa_total.insert("end", "Rp ")
    bakmi_jawa_total.insert("end", bakmi_jawa_jml)

    nasi_tiwul_jml = nasi_tiwul_harga * makanan_harga[2]
    nasi_tiwul_total.delete(first=0, last=1000)
    nasi_tiwul_total.insert("end", "Rp ")
    nasi_tiwul_total.insert("end", nasi_tiwul_jml)

    gatot_jml = gatot_harga * makanan_harga[3]
    gatot_total.delete(first=0, last=1000)
    gatot_total.insert("end", "Rp ")
    gatot_total.insert("end", gatot_jml)

    gudeg_jml = gudeg_harga * makanan_harga[4]
    gudeg_total.delete(first=0, last=1000)
    gudeg_total.insert("end", "Rp ")
    gudeg_total.insert("end", gudeg_jml)

    tape_jml = tape_harga * minuman_harga[0]
    tape_total.delete(first=0, last=1000)
    tape_total.insert("end", "Rp ")
    tape_total.insert("end", tape_jml)

    teh_jml = teh_harga * minuman_harga[1]
    teh_total.delete(first=0, last=1000)
    teh_total.insert("end", "Rp ")
    teh_total.insert("end", teh_jml)

    jeruk_jml = jeruk_harga * minuman_harga[2]
    jeruk_total.delete(first=0, last=1000)
    jeruk_total.insert("end", "Rp ")
    jeruk_total.insert("end", jeruk_jml)

    campur_jml = campur_harga * minuman_harga[3]
    campur_total.delete(first=0, last=1000)
    campur_total.insert("end", "Rp ")
    campur_total.insert("end", campur_jml)

    kopi_jml = kopi_harga * minuman_harga[4]
    kopi_total.delete(first=0, last=1000)
    kopi_total.insert("end", "Rp ")
    kopi_total.insert("end", kopi_jml)
#Konfigurasi total Makanan dan Minuman
    total_makanan_jml = nasi_goreng_jml + bakmi_jawa_jml \
                       + nasi_tiwul_jml + gatot_jml + gudeg_jml
    total_makanan.delete(first=0, last=1000)
    total_makanan.insert("end", "Rp ")
    total_makanan.insert("end", total_makanan_jml)

    total_minuman_jml = tape_jml + teh_jml \
                        + jeruk_jml + campur_jml + kopi_jml 
    total_minuman.delete(first=0, last=1000)
    total_minuman.insert("end", "Rp ")
    total_minuman.insert("end", total_minuman_jml)
    
#konfigurasi untuk mereset semua data
def reset():
	total_makanan.delete(first=0, last=1000)
	total_minuman.delete(first=0, last=1000)
	total_biaya.delete(first=0, last=1000)
	gudeg_entry.delete(first=0, last=1000)
	gatot_entry.delete(first=0, last=1000)
	nasi_tiwul_entry.delete(first=0, last=1000)
	nasi_goreng_entry.delete(first=0, last=1000)
	bakmi_jawa_entry.delete(first=0, last=1000)
	teh_entry.delete(first=0, last=1000)
	tape_entry.delete(first=0, last=1000)
	jeruk_entry.delete(first=0, last=1000)
	campur_entry.delete(first=0, last=1000)
	kopi_entry.delete(first=0, last=1000)

	teh_entry.insert(END, 0)
	tape_entry.insert(END, 0)
	jeruk_entry.insert(END, 0)
	campur_entry.insert(END, 0)
	kopi_entry.insert(END, 0)
	gudeg_entry.insert(END, '0')
	gatot_entry.insert(END, '0')
	nasi_tiwul_entry.insert(END, '0')
	nasi_goreng_entry.insert(END, '0')
	bakmi_jawa_entry.insert(END, '0')

	gudeg_total.delete(first=0, last=1000)
	gatot_total.delete(first=0, last=1000)
	nasi_tiwul_total.delete(first=0, last=1000)
	nasi_goreng_total.delete(first=0, last=1000)
	bakmi_jawa_total.delete(first=0, last=1000)
	teh_total.delete(first=0, last=1000)
	tape_total.delete(first=0, last=1000)
	jeruk_total.delete(first=0, last=1000)
	campur_total.delete(first=0, last=1000)
	kopi_total.delete(first=0, last=1000)

#konfigurasi total button
total_button = Button(master,
                      text="Total",
                      font='Times 20 bold',
                      bg="sienna",
                      width=23,
                      relief=RAISED,
                      command=total_call, )
total_button.place(x=705, y=505)

#konfigurasi button reset
reset_button = Button(master,
                 text="Reset",
                 font='Times 20 bold',
                 bg="sienna",
                 width=23,
                 relief=RAISED,
                 command=reset)
reset_button.place(x=705, y=580)

#konfigurasi nama total
total_makanan_menu = Label(master,
                   font="times 17 bold",
                   text="Total Makanan : ",
                   bg='sienna4',
                   fg='black')
total_makanan_menu.place(x=700, y=300)

total_minuman_menu = Label(master,
                   font="times 17 bold",
                   text="Total Minuman : ",
                   bg='sienna4',
                   fg='black')
total_minuman_menu.place(x=700, y=370)

total_menu = Label(master,
                   font="times 17 bold",
                   text="Total Biaya        : ",
                   bg='sienna4',
                   fg='black')
total_menu.place(x=700, y=440)

#konfigurasi total semua makanan
total_makanan = Entry(master, font=("Helvetica 24 normal"))
total_makanan.configure(bg="sienna4",
                  fg="black",
                  relief=RAISED,
                  state="readonly",
                  width=10)
master.total_makanan = total_makanan
total_makanan.place(x=900, y=300)
master.total_makanan.configure(state="normal")

#konfiguri semua total minuman
total_minuman = Entry(master, font=("Helvetica 24 normal"))
total_minuman.configure(bg="sienna4",
                  fg="black",
                  relief=RAISED,
                  state="readonly",
                  width=10)
master.total_minuman = total_minuman
total_minuman.place(x=900, y=370)
master.total_minuman.configure(state="normal")

#konfigurasi total semua biaya
total_biaya = Entry(master, font=("Helvetica 24 normal"))
total_biaya.configure(bg="sienna4",
                  fg="black",
                  relief=RAISED,
                  state="readonly",
                  width=10)
master.total_biaya = total_biaya
total_biaya.place(x=900, y=440)
master.total_biaya.configure(state="normal")

#konfigurasi kolom total makanan
nasi_goreng_total = Entry(master, font=("Helvetica 12 normal"))
nasi_goreng_total.configure(bg="sienna4",
                            fg="black",
                            relief=RAISED,
                            state="readonly",
                            width=10)
master.nasi_goreng_total = nasi_goreng_total
nasi_goreng_total.place(x=530, y=295)
master.nasi_goreng_total.configure(state="normal")

bakmi_jawa_total = Entry(master, font=("Helvetica 12 normal"))
bakmi_jawa_total.configure(bg="sienna4",
                           fg="black",
                           relief=RAISED,
                           state="readonly",
                           width=10)
master.bakmi_jawa_total = bakmi_jawa_total
bakmi_jawa_total.place(x=530, y=325)
master.bakmi_jawa_total.configure(state="normal")

nasi_tiwul_total = Entry(master, font=("Helvetica 12 normal"))
nasi_tiwul_total.configure(bg="sienna4",
                           fg="black",
                           relief=RAISED,
                           state="readonly",
                           width=10)
master.nasi_tiwul_total = nasi_tiwul_total
nasi_tiwul_total.place(x=530, y=355)
master.nasi_tiwul_total.configure(state="normal")

gatot_total = Entry(master, font=("Helvetica 12 normal"))
gatot_total.configure(bg="sienna4",
                      fg="black",
                      relief=RAISED,
                      state="readonly",
                      width=10)
master.gatot_total = gatot_total
gatot_total.place(x=530, y=385)
master.gatot_total.configure(state="normal")

gudeg_total = Entry(master, font=("Helvetica 12 normal"))
gudeg_total.configure(bg="sienna4",
                      fg="black",
                      relief=RAISED,
                      state="readonly",
                      width=10)
master.gudeg_total = gudeg_total
gudeg_total.place(x=530, y=415)
master.gudeg_total.configure(state="normal")

tape_total = Entry(master, font=("Helvetica 12 normal"))
tape_total.configure(bg="sienna4",
                     fg="black",
                     relief=RAISED,
                     state="readonly",
                     width=10)
master.tape_total = tape_total
tape_total.place(x=530, y=500)
master.tape_total.configure(state="normal")

#konfigurasi kolom total minuman
teh_total = Entry(master, font=("Helvetica 12 normal"))
teh_total.configure(bg="sienna4",
                    fg="black",
                    relief=RAISED,
                    state="readonly",
                    width=10)
master.teh_total = teh_total
teh_total.place(x=530, y=530)
master.teh_total.configure(state="normal")

jeruk_total = Entry(master, font=("Helvetica 12 normal"))
jeruk_total.configure(bg="sienna4",
                      fg="black",
                      relief=RAISED,
                      state="readonly",
                      width=10)
master.jeruk_total = jeruk_total
jeruk_total.place(x=530, y=560)
master.jeruk_total.configure(state="normal")

campur_total = Entry(master, font=("Helvetica 12 normal"))
campur_total.configure(bg="sienna4",
                       fg="black",
                       relief=RAISED,
                       state="readonly",
                       width=10)
master.campur_total = campur_total
campur_total.place(x=530, y=590)
master.campur_total.configure(state="normal")

kopi_total = Entry(master, font=("Helvetica 12 normal"))
kopi_total.configure(bg="sienna4",
                     fg="black",
                     relief=RAISED,
                     state="readonly",
                     width=10)
master.kopi_total = kopi_total
kopi_total.place(x=530, y=620)
master.kopi_total.configure(state="normal")

master.mainloop()

