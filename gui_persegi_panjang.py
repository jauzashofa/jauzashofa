import tkinter as tk

def hitung():
    try:
        panjang = float(e1.get())
        lebar = float(e2.get())

        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        hasil_luas.config(text=f"Luas Persegi Panjang: {luas:.2f}")
        hasil_keliling.config(text=f"Keliling Persegi Panjang: {keliling:.2f}")

    except ValueError:
        hasil_luas.config(text="Masukan angka yang valid!")
        hasil_keliling.config(text="")


master = tk.Tk()
master.title("Program Persegi Panjang")

tk.Label(master,text="Masukan Panjang").grid(row=0)
tk.Label(master,text="Masukan Lebar").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

hasil_luas = tk.Label(master)
hasil_keliling = tk.Label(master)
hasil_luas.grid(row=2, column=1)
hasil_keliling.grid(row=3, column=1)

    
bt_hitung=tk.Button(master, text='Hitung', command=hitung)
bt_hitung.grid(row=3, column=0, sticky=tk.W, pady=4)

tk.mainloop()