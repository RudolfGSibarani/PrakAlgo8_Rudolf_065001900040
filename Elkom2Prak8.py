# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:23:53 2021

@author: Rudolf
"""


jumlah = 0

pertama = int(input("PROGRAM MENGHITUNG JUMLAH RANGE\nMasukkan angka pertama: "))
kedua = int(input("Masukkan angka kedua: "))

while pertama <= kedua:
    jumlah += pertama
    pertama += 1

print("Jumlah range adalah:", jumlah, "\n")
