# ライブラリのインポート（asで別名をつけてる）
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import os

def filedialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    folder_name = tk.filedialog.askdirectory(initialdir=iDir)

class Window:
    def __init__(self,root):
    # ウィンドウのタイトル
        root.title('random_slideshow')

        # ウィンドウのサイズ変更の可否
        root.resizable(False, False)

        # ウィンドウの属性（背景色やウィンドウサイズ、タイトルが設定できる）
        root.configure(bg='#DBDBDB')

        # ウィジェットの配置（place()：ウィジェットを座標で配置）
        label1 = tk.Label(root, text='ラベル1')
        label1.place(x=100, y=50)

        # tk.SE：座標の基準位置をボタン右下に
        next_btn = tk.Button(root, text='NEXT', font=('', 20))
        next_btn.place(relx=0.9, rely=0.9, anchor=tk.SE, width=200, height=40)
        # tk.NE：座標の基準位置をボタン右上に
        folder_btn = tk.Button(root, text='フォルダ選択', command=filedialog_clicked)
        folder_btn.place(relx=0.9, rely=0.1, anchor=tk.NE, width=200, height=40)



# tkオブジェクトの作成
root = tk.Tk()
# ウィンドウのサイズと出現位置
root.geometry('1000x600+200+50')

# canvas（画像表示範囲）の作成
canvas_w = 600
canvas_h = 600
canvas = tk.Canvas(root, width=canvas_w, height=canvas_h)
canvas.place(x=0, y=0)

# 画像の取得
img = Image.open('hoge.jpg')

# 画像のサイズを取得
w = img.width
h = img.height

# 画像の縦幅がcanvasの縦幅より大きい場合リサイズ
if w > canvas_w:
    img = img.resize((int(w * (canvas_w / w)), int(h * (canvas_w / w))))
    
# 画像の横幅がcanvasの横幅より大きい場合リサイズ
if h > canvas_h:
    img = img.resize((int(w * (canvas_h / h)), int(h * (canvas_h / h))))

# 画像を表示
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=tk.NW)

Window(root)

# メインループの実行
root.mainloop()
