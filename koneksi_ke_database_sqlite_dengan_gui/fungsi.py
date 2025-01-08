from tkinter import *
from koneksi_database_sql import *
from tkinter import *
from tkinter import messagebox
#from tkinter import Entry, Button, messagebox
import sqlite3


    
def increase_last_id():
    conn = sqlite3.connect(r'D:\BELAJAR\Database\SQLlite\Latihan01.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM pelanggan')
    max_id = cursor.fetchone()[0]
    return (max_id + 1) if max_id is not None else 1  # Increment by 1


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
    global txt_id
    txt_id = Entry(font='normal 12', bd=2, width=15)
    txt_id.place(x=150, y=26, height=20)
    txt_id.insert(0,increase_last_id())
    
    
def text_nama():
    global txt_nama
    txt_nama = Entry(font='normal 12', bd=2, width=15)
    txt_nama.place(x=150, y=53, height=20)

def text_gender():
    global txt_gender
    txt_gender = Entry(font='normal 12', bd=2, width=15)
    txt_gender.place(x=150, y=80, height=20)

def text_alamat():
    global txt_alamat
    txt_alamat = Entry(font='normal 12', bd=2, width=15)
    txt_alamat.place(x=150, y=108, height=20)

def text_telepon():
    global txt_tlp
    txt_tlp = Entry(font='normal 12', bd=2, width=15)
    txt_tlp.place(x=150, y=135, height=20)

def field_bersih():
    txt_id.delete(0, END)
    txt_nama.delete(0, END)
    txt_alamat.delete(0, END)
    txt_gender.delete(0, END)
    txt_tlp.delete(0, END)

def submit():
    def submit_action():
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(r'D:\BELAJAR\Database\SQLlite\Latihan01.sqlite')
            cursor = conn.cursor()
            
            # Insert the data into the pelanggan table
            cursor.execute('''
                INSERT INTO pelanggan (id, name, gender, alamat, telp)
                VALUES (?, ?, ?, ?, ?)
            ''', (txt_id.get(), txt_nama.get(), txt_gender.get(), txt_alamat.get(), txt_tlp.get()))
            
            # Commit the transaction and close the connection
            conn.commit()
            conn.close()
            
            # Show success message
            messagebox.showinfo("Sukses", "Sukses menambah data")
            field_bersih()
            txt_id.insert(0,increase_last_id())
        
        except Exception as e:
            # Show error message if something goes wrong
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    # Create the submit button
    btn_submit = Button(text='Simpan', font='normal 12', background='light blue', bd=1, activebackground='green', command=submit_action)
    btn_submit.place(x=30, y=180, height=30)







