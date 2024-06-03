from tkinter import ttk
import defs
import tkinter as tk


class Admin:
    def __init__(self, ANO):
        self.ANO = ANO
        self.root = tk.Tk()
        self.root.config(background="white")
        self.root.title(ANO)
        self.root.geometry("600x370+300+100")
        self.root.resizable(0, 0)
        self.weapon_label = tk.Label(
            self.root, text="装备名", bg="#7e0c6e", fg="white", font=("黑体", 12))
        self.player_label = tk.Label(
            self.root, text="已购买此装备的玩家", bg="#7e0c6e", fg="white", font=("黑体", 12))

        self.lb = tk.Listbox(self.root, width=20, height=10)
        columns = ('PNO', 'PNAME', 'VALUE')
        self.player_text = ttk.Treeview(
            self.root, height=8, columns=columns, show="headings")
        self.player_text.bind('<<TreeviewSelect>>', self.on_select)
        for col in columns:
            self.player_text.heading(col, text=col)
            self.player_text.column(col, width=80, anchor=tk.CENTER)
        self.sb = tk.Scrollbar(self.root, orient=tk.VERTICAL,
                               command=self.player_text.yview)
        self.player_text.config(yscrollcommand=self.sb.set)

        tk.Label(self.root, text="玩家号：", bg="#7e0c6e",
                 fg="white", font=("黑体", 12)).grid(row=3, column=0, pady=10)
        tk.Label(self.root, text="价值：", bg="#7e0c6e",
                 fg="white", font=("黑体", 12)).grid(row=5, column=0, pady=10)

        self.player_id_entry = tk.Entry(
            self.root, text="玩家号", width=8, bg='#7e0c6e', fg='white', insertbackground='white')
        self.player_value_entry = tk.Entry(
            self.root, text="价值", width=8, bg='#7e0c6e', fg='white', insertbackground='white')

        self.player_button = tk.Button(
            self.root, text="查询", command=self.find_value, bg="cadetblue", fg="white", font=("黑体", 12))
        self.value_button = tk.Button(
            self.root, text="修改价值", command=self.change_value, bg="cadetblue", fg="white", font=("黑体", 12))

    def inilize(self):
        self.weapon_label.grid(row=1, column=0)
        self.player_label.grid(row=1, column=2)

        self.player_text.grid(row=2, column=2, sticky='news', padx=20)
        self.sb.place(x=522, y=22, height=187)

        var = tk.StringVar()
        for item in defs.find_admin_weapon(self.ANO):
            self.lb.insert(tk.END, item)
        self.lb.grid(row=2, column=0, padx=20)
        self.player_id_entry.grid(row=4, column=0)
        self.player_value_entry.grid(row=6, column=0)
        # 查询
        self.player_button.grid(row=2, column=1)
        # 输入价值
        self.value_button.grid(row=5, column=1)

    # 查询选了该管理者管理的武器的价值
    def find_value(self):
        WNAME = self.lb.get(self.lb.curselection())[0]
        for row in self.player_text.get_children():
            self.player_text.delete(row)
        defs.find_player_value(self.player_text, WNAME, self.ANO)

    # 修改价值
    def change_value(self):
        PNO = self.player_id_entry.get()
        VALUE = self.player_value_entry.get()
        WNAME = self.lb.get(self.lb.curselection())[0]
        defs.change_value(PNO, VALUE, WNAME)
        self.find_value()

    def start(self):
        self.inilize()
        self.root.mainloop()

    # 选择表格自动输入效果
    def on_select(self, event):
        tree = event.widget
        selected_item = tree.selection()[0]
        value = tree.item(selected_item, 'values')[0]
        self.player_id_entry.delete(0, tk.END)
        self.player_id_entry.insert(tk.END, value)



if __name__ == '__main__':
    w = Admin('zmxy')
    w.start()
