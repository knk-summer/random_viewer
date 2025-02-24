# ライブラリのインポート（asで別名をつけてる）
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageFilter
import os

# tkオブジェクトの作成
root = tk.Tk()

# ウィンドウのタイトル
root.title('random_slideshow')
# ウィンドウのサイズと出現位置
root.geometry('800x600+200+50')
# ウィンドウのサイズ変更の可否
root.resizable(True, True)

# ウィンドウの最大サイズ
# root.maxsize(1000, 800)
# ウィンドウの最小サイズ
# root.minsize(width, height)

# ウィンドウの属性（背景色やウィンドウサイズ、タイトルが設定できる）
root.configure(bg='#333')

# ウィジェットの配置（place()：ウィジェットを座標で配置）
label1 = tk.Label(root, text='ラベル1')
label1.place(x=100, y=50)

btn1 = tk.Button(root, text='テストボタン1')
btn1.place(relx=0.1, rely=0.1)

btn2 = tk.Button(root, text='テストボタン2')
btn2.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

# メインループの実行
root.mainloop()
