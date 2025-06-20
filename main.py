import tkinter as tk
import uuid
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
txt_edit = Text(root, height = 5, width = 52)

def main():
    # specify size of window.
    root.geometry("250x170")
    root.title("Dedup v1.0")

    # Create button for next text.
    b1 = Button(root, text = "Desduplicar!", command = deduplicate)
     
    # Create an Exit button.
    b2 = Button(root, text = "Sair", command = root.destroy)

    # File dialog
    filepath = askopenfilename(filetypes=[("Text Files", "*.csv")])
    if not filepath:
        return

    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
     
    txt_edit.pack()
    b1.pack()
    b2.pack()
     
    tk.mainloop()

def deduplicate():
    original = txt_edit.get("1.0", tk.END)
    lines = original.splitlines()

    map = dict()

    for idx, line in enumerate(lines):
        map[line] = line

    tmp = str()

    for key in map:
        if is_valid_uuid(key):
            tmp += key + "\n"
        else:
            print('not valid uuid: '+key)

    txt_edit.delete("1.0", tk.END)
    txt_edit.insert(tk.END, tmp)

    f = open("result.csv", "a")
    f.write(tmp)
    f.close()

def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))

        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
