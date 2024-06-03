from tkinter import *
import tkinter as tk
import pymysql
from PIL import Image, ImageTk
import weapon_class
import admin_class


def judge():
    login = user_entry.get()
    password = password_entry.get()
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT P.PNO FROM P where P.PNO='%s' and P.PSWD='%s'" % (
        login, password)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        cursor = db.cursor()
        sql = "SELECT A.ANAME FROM A where A.ANO='%s' and A.PSWD='%s'" % (
            login, password)
        cursor.execute(sql)
        result = cursor.fetchall()
    else:
        return result
    return result


def start():
    result = judge()
    if len(result) != 0:
        root.destroy()
        if result[0][0][0] == 'P':
            w = weapon_class.weapon(result[0][0])
            w.start()
        else:
            a = admin_class.Admin(result[0][0])
            a.start()
    else:
        Label(root, text="用户名或密码错误，请重新输入").place(x=100, y=400)


def viewswitch():
    global flag_pic
    flag_pic = not flag_pic
    if flag_pic:
        pswd_view_button['image'] = imgview
        password_entry.config(show="*")
    else:
        pswd_view_button['image'] = imgviewoff
        password_entry.config(show="")
    root.update()


root = Tk()
root.title("玩家登录界面")

# 背景图
photo = Image.open("pic/game.jpg")
photo = photo.resize((400, 200))  # 规定图片大小
img0 = ImageTk.PhotoImage(photo)
img1 = tk.Label(image=img0).place(x=-2, y=0)

root.config(background="white")
root.geometry("400x500+300+100")
root.resizable(0, 0)

Label(root, text="玩家名", fg="#f7c22a", bg="white",
      font=("黑体", 12)).place(x=70, y=250)
user_entry = Entry(root, width=15, bg='#1e0c6e',
                   fg='white', insertbackground='white')
user_entry.insert(0, 'P2211105')
user_entry.place(x=150, y=250)
Label(root, text=" 密码 ", fg="#f7c22a", bg="white",
      font=("黑体", 12)).place(x=70, y=300)
password_entry = Entry(root, width=15, bg='#1e0c6e',
                       fg='white', insertbackground='white', show='*')
password_entry.insert(0, '123456')
password_entry.place(x=150, y=300)

star_button = Button(root, text="登录", bg="#7e9cbe", fg="white", font=(
    "黑体", 12), height=2, width=8, command=start)
star_button.place(x=160, y=350)

pic_view = Image.open("pic/view.png").resize((15, 15))
imgview = ImageTk.PhotoImage(pic_view)

pic_viewoff = Image.open("pic/view_off.png").resize((15, 15))
imgviewoff = ImageTk.PhotoImage(pic_viewoff)
flag_pic = True
pswd_view_button = Button(root, bg='#ffffff', image=imgview,
                          height=15, width=15, relief="flat", command=viewswitch)
pswd_view_button.place(x=280, y=300)

root.mainloop()
