# ライブラリのインポート（asで別名をつけてる）
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import os

# フォルダの選択
def filedialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    # 選択したフォルダの絶対パスを取得
    folder_name = tk.filedialog.askdirectory(initialdir=iDir)
    # ※確認用なので後で消す
    print(folder_name)

    load_images(folder_name)

# 選択したフォルダ内の画像ファイルのみ絶対パスを取得
def load_images(folder_name):
    # 取得したパスを格納するために空のリストを作成
    images_paths = []
    # 画像ファイルかの判断に使う
    exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    # 選択したフォルダの中身を取得
    for root, dirs, files in os.walk(folder_name):
        for name in files + dirs:
            image_path = os.path.join(root, name)
            # パスの末尾の文字列（拡張子）を見て画像ファイルの場合のみリストに追加
            if image_path.endswith(exts):
                images_paths.append(image_path)
    print(images_paths)

# 【作業】取得したパスをランダムに選出する用の関数を用意する

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
# 【作業】ランダムで1つ画像を選んで変数に格納→Image.openの引数に
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

# クラスの呼び出し？
Window(root)

# メインループの実行
root.mainloop()
