# Лабораторная работа №3
# Вариант 3
# Вводная часть ключа - число в HEX (5 знаков)
# Формат ключа: XXXXX-XXXXX-XXXXX XX
import tkinter as tk
from tkinter import messagebox
import random

HEX_DIGITS = "0123456789ABCDEF"
KEY_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def generate_key():
    hex_value = entry_hex.get().strip().upper()

    if len(hex_value) != 5 or any(c not in HEX_DIGITS for c in hex_value):
        messagebox.showerror("Ошибка", "Введите 5-значное HEX-число (0-9, A-F)")
        return

    dec_value = str(int(hex_value, 16)).zfill(5)
    first_three = dec_value[:3]
    last_two = dec_value[-2:]

    blocks = []
    for digit in first_three:
        block = [random.choice(KEY_CHARS) for _ in range(5)]
        pos = random.randint(0, 4)
        block[pos] = digit
        blocks.append("".join(block))

    key = "-".join(blocks) + " " + last_two
    result_var.set(key)


window = tk.Tk()
window.title("Raid Access Keygen")
window.geometry("560x400")
window.resizable(False, False)

bg_img = tk.PhotoImage(file="background.png")
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

label_title = tk.Label(
    window, text="RAID ACCESS KEYGEN",
    background="#0a0d08", foreground="#8fbf5a",
    font=("Consolas", 20, "bold")
)
label_title.pack(pady=(30, 10))

label_hex = tk.Label(
    window, text="Введите HEX-код доступа (5 знаков):",
    background="#0a0d08", foreground="#d7e6c3",
    font=("Consolas", 12)
)
label_hex.pack(pady=(10, 5))

entry_hex = tk.Entry(window, width=10, font=("Consolas", 16), justify="center")
entry_hex.insert(0, "54CD1")
entry_hex.pack()

btn_generate = tk.Button(
    window, text="Сгенерировать ключ",
    font=("Consolas", 12, "bold"),
    command=generate_key
)
btn_generate.pack(pady=20)

result_var = tk.StringVar()
label_result = tk.Label(
    window, textvariable=result_var,
    background="#0a0d08", foreground="#00ff66",
    font=("Consolas", 18, "bold")
)
label_result.pack(pady=10)

window.mainloop()