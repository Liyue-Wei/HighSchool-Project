import tkinter as tk
import ttkbootstrap as ttk

win = ttk.Window(themename="cosmo")
win.geometry("1300x360")
win.title("Genetic Translator")
     
def translation():  
    untranslated_dna = []
    translating = []
    translated_mrna = []
    
    untranslated_dna = dna_input.get()
    count = len(untranslated_dna)

    for num in range(0, count, 1):
        translating.append(untranslated_dna[num])

    for num in range(0, count, 1):
        if translating[num] == "A":
            translated_mrna.append("U")

        elif translating[num] == "T":
            translated_mrna.append("A")

        elif translating[num] == "C":
            translated_mrna.append("G")

        elif translating[num] == "G":
            translated_mrna.append("C")

        else:
            translated_mrna.append("False")

        rna_output.set(translated_mrna)

class GUI_interface():
    global dna_input, rna_output
    dna_input = tk.StringVar()
    rna_output = tk.StringVar()
    label_1 = ttk.Label(win, text="輸入未轉譯之DNA序列", bootstyle="cosmo", font=("微軟正黑體", 18)).place(x=10, y=10)
    entry_1 = ttk.Entry(win, width=36, bootstyle="cosmo", font=("微軟正黑體", 20), textvariable=dna_input).place(x=10, y=90)
    label_2 = ttk.Label(win, text="轉譯完成之mRNA序列", bootstyle="cosmo", font=("微軟正黑體", 18)).place(x=10, y=185)
    entry_2 = ttk.Label(win, bootstyle="cosmo", font=("微軟正黑體", 20), textvariable=rna_output).place(x=10, y=260)
    button_1 = tk.Button(win, text="Enter", font=("微軟正黑體", 14), command=translation).place(x=1160, y=90)

win.mainloop()