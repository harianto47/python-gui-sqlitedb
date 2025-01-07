import sqlite3
#import os

#os.system("cls")

# koneksi ke database sqlite

def koneksi_sqlite(): 
    global cursor
    conn = sqlite3.connect(r'D:\BELAJAR\Database\SQLlite\Latihan01.sqlite')
    cursor = conn.cursor()






