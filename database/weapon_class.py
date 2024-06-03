from tkinter import ttk
import tkinter as tk
import defs
import value_class


class weapon:
    def __init__(self, PNO):
        self.root = tk.Tk()
        self.root.config(background="grey")
        self.root.wm_title(PNO)
        self.root.geometry("1190x500+300+100")
        self.root.resizable(0, 0)
        self.PNO = PNO

        self.weapon_label = tk.Label(
            self.root, text="商铺装备", bg="#d5c74a", fg="white", font=("黑体", 12))
        self.choose_weapon_label = tk.Label(
            self.root, text="个人仓库", bg="#d5c74a", fg="white", font=("黑体", 12))
        self.weapon_entry_label = tk.Label(
            self.root, text="输入您想要交易的装备号：", bg="#7e0c6e", fg="white", font=("黑体", 12))

        columns_player_text = ('PNO', 'PNAME', 'SEX', 'AGE', 'ELEMENT')
        self.player_text = ttk.Treeview(
            self.root, height=1, columns=columns_player_text, show='headings')
        for col in columns_player_text:
            self.player_text.heading(col, text=col)
            self.player_text.column(col, width=80, anchor=tk.CENTER)

        columns_weapon_text = ('WNO', 'WNAME', 'LEVEL', 'ELEMENT', 'ANAME')
        self.weapon_text = ttk.Treeview(
            self.root, height=9, columns=columns_weapon_text, show='headings')
        self.weapon_text.bind('<<TreeviewSelect>>', self.on_select)
        for col in columns_weapon_text:
            self.weapon_text.heading(col, text=col)
            self.weapon_text.column(col, width=80, anchor=tk.CENTER)

        columns_choose_weapon_text = (
            'WNO', 'WNAME', 'LEVEL', 'ELEMENT', 'ANAME')
        self.choose_weapon_text = ttk.Treeview(
            self.root, height=9, columns=columns_choose_weapon_text, show='headings')
        self.choose_weapon_text.bind('<<TreeviewSelect>>', self.on_select)
        for col in columns_choose_weapon_text:
            self.choose_weapon_text.heading(col, text=col)
            self.choose_weapon_text.column(col, width=80, anchor=tk.CENTER)

        self.weapon_entry = tk.Entry(
            self.root, width=5, bg='#7e0c6e', fg='white', insertbackground='white')

        self.weapon_button = tk.Button(self.root, text="购买", bg="cadetblue", fg="white", font=(
            "黑体", 12), command=self.choose_weapon)
        self.weapon_button2 = tk.Button(self.root, text="出售", bg="cadetblue", fg="white", font=(
            "黑体", 12), command=self.delete_weapon)
        self.weapon_button3 = tk.Button(self.root, text="关闭", bg="cadetblue", fg="white", font=(
            "黑体", 12), command=self.root.destroy)
        self.weapon_button4 = tk.Button(self.root, text="查看个人仓库", bg="cadetblue", fg="white", font=(
            "黑体", 12), command=self.intovalue(PNO))

    def inilize(self):
        self.player_text.place(x=295, y=400)

        self.weapon_label.grid(row=3, column=0, sticky=(tk.N, tk.S))
        self.weapon_text.grid(row=4, column=0, sticky='news', padx=35)

        self.choose_weapon_label.grid(row=3, column=2, sticky=(tk.N, tk.S))
        self.choose_weapon_text.grid(row=4, column=2, sticky='news', padx=35)

        self.weapon_entry_label.grid(row=6, column=1, pady=20)
        self.weapon_entry.grid(row=7, column=1)
        self.weapon_button.grid(row=9, column=1)
        self.weapon_button2.grid(row=10, column=1)
        self.weapon_button3.grid(row=10, column=3)
        self.weapon_button4.grid(row=7, column=2, pady=10)

    # 选课
    def choose_weapon(self):
        weapon_number = self.weapon_entry.get()
        defs.purchase_weapon(self.PNO, str(weapon_number), 0)
        self.update_ui()

    # 退课
    def delete_weapon(self):
        weapon_number = self.weapon_entry.get()
        defs.sell_weapon(self.PNO, str(weapon_number))
        self.update_ui()

    # 更新ui
    def update_ui(self):
        for row in self.player_text.get_children():
            self.player_text.delete(row)

        for row in self.weapon_text.get_children():
            self.weapon_text.delete(row)

        for row in self.choose_weapon_text.get_children():
            self.choose_weapon_text.delete(row)

        defs.display_player(self.player_text, self.PNO)
        defs.display_weapon(self.weapon_text, self.PNO)
        defs.display_purchase_weapon(self.choose_weapon_text, self.PNO)

    def start(self):
        self.inilize()
        self.update_ui()
        self.root.mainloop()

    def intovalue(self, PNO):
        def inner():
            self.root.destroy()
            p = value_class.value(PNO)
            p.start()
        return inner

    def on_select(self, event):
        tree = event.widget
        selected_item = tree.selection()[0]
        value = tree.item(selected_item, 'values')[0]
        self.weapon_entry.delete(0, tk.END)
        self.weapon_entry.insert(tk.END, value)


if __name__ == '__main__':
    w = weapon('P2211105')
    w.start()
