from tkinter import *
from koneksi_database_sql import *
import sqlite3


def get_last_id():
    conn = sqlite3.connect(r'D:\BELAJAR\Database\SQLlite\Latihan01.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM pelanggan')
    last_id = cursor.fetchone()
    cursor.close()
    return last_id[0] if last_id and last_id[0] is not None else "No ID found"



def label_id():
    L_id = Label(text='ID                           :', font='normal 12', background='light blue')
    L_id.place(x=10, y=10, height=50)

def label_nama():
    L_nama  = Label(text='Nama                    :',font='normal 12', background='light blue')
    L_nama.place(x=10, y=45, height=35)

def label_gender():
    jenkel = Label(text='Jenis-Kelamin      :', font='normal 12', background='light blue')
    jenkel.place(x=10, y=80, height=20)

def Label_alamat():
    alamat_v  = Label(text='Alamat                   :',font='normal 12', background='light blue')
    alamat_v.place(x=10, y=100, height=35)

def Label_telepon():
    tlp  = Label(text='Telefon                   :',font='normal 12', background='light blue')
    tlp.place(x=10, y=130, height=35)


def text_id():
    txt_id = Entry(font='normal 12', bd=2, width=15)
    txt_id.place(x=150, y=26, height=20)
    txt_id.insert(0,get_last_id())
    
    

def text_nama():
    txt_nama = Entry(font='normal 12', bd=2, width=15)
    txt_nama.place(x=150, y=53, height=20)

def text_gender():
    txt_gender = Entry(font='normal 12', bd=2, width=15)
    txt_gender.place(x=150, y=80, height=20)

def text_alamat():
    txt_alamat = Entry(font='normal 12', bd=2, width=15)
    txt_alamat.place(x=150, y=108, height=20)

def text_telepon():
    txt_tlp = Entry(font='normal 12', bd=2, width=15)
    txt_tlp.place(x=150, y=135, height=20)


def submit():
    btn_submit = Button(text='Simpan', font='normal 12', background='light blue', bd=1, activebackground='blue')
    btn_submit.place(x=30, y=180, height= 30)



