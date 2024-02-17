import tkinter as tk

click_count_1 = 0
click_count_2 = 0

def change_text_1():
    global click_count_1
    if label.cget("text") == "Початковий текст":
        label.config(text="Новий текст 1")
    else:
        label.config(text="Початковий текст")
    click_count_1 += 1
    update_title()

def change_text_2():
    global click_count_2
    if label.cget("text") == "Початковий текст":
        label.config(text="Новий текст 2")
    else:
        label.config(text="Початковий текст")
    click_count_2 += 1
    update_title()

def update_title():
    root.title(f"Кількість клацань кнопки 1: {click_count_1}, Кількість клацань кнопки 2: {click_count_2}")

root = tk.Tk()
root.title("Змінюючийся текст")

label = tk.Label(root, text="Початковий текст")
label.pack(pady=10)  # Відступи від верхнього краю

button1 = tk.Button(root, text="Змінити текст 1", command=change_text_1)
button1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Відступи по краям

button2 = tk.Button(root, text="Змінити текст 2", command=change_text_2)
button2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Відступи по краям

update_title()

root.mainloop()

root.mainloop()