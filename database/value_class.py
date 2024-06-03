from tkinter import ttk
import tkinter as tk
import defs
import weapon_class


class value:
    def __init__(self, PNO):
        self.root = tk.Tk()
        self.root.config(background="white")
        self.root.wm_title(PNO)
        self.root.geometry("400x500+300+100")
        self.root.resizable(0, 0)
        self.PNO = PNO

        self.value_label = tk.Label(
            self.root, text="仓库装备价值", bg="#7e0c6e", fg="white", font=("黑体", 12))

        columns_value_text = ('WNO', 'WNAME', 'VALUE')
        self.value_text = ttk.Treeview(
            self.root, height=14, columns=columns_value_text, show='headings')
        for col in columns_value_text:
            self.value_text.heading(col, text=col)
            self.value_text.column(col, width=135, anchor=tk.CENTER)

        self.weapon_button = tk.Button(self.root, text="关闭", bg="cadetblue", fg="white", font=(
            "黑体", 12), command=self.root.destroy)
        self.weapon_button2 = tk.Button(self.root, text="返回", bg="cadetblue", fg="white", font=(
            "黑体", 12), command=self.back(PNO))

    def update_ui(self):
        defs.display_value(self.value_text, self.PNO)

    def inilize(self):
        self.value_label.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.value_text.grid(row=1, column=1, sticky='news')
        self.weapon_button.grid(row=3, column=1)
        self.weapon_button2.grid(row=2, column=1, pady=30)

    def start(self):
        self.inilize()
        self.update_ui()
        self.root.mainloop()

    def back(self, PNO):
        def inner():
            self.root.destroy()
            w = weapon_class.weapon(PNO)
            w.start()
        return inner


if __name__ == '__main__':
    w = value('P2211105')
    w.start()
