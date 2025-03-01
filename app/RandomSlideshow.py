# ライブラリのインポート（asで別名をつけてる）
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import random
import os

class RandomViewerApp:
    def __init__(self,root):
        folder_name = ''
        self.all_images_paths = ''
        self.random_image = ''
        self.wedget(root)

    # フォルダの選択
    def filedialog_clicked(self):
        iDir = os.path.abspath(os.path.dirname(__file__))
        # 選択したフォルダの絶対パスを取得
        global folder_name
        folder_name = tk.filedialog.askdirectory(initialdir=iDir)
        self.load_images()

    # 選択したフォルダ内の全画像ファイルの絶対パスを取得
    def load_images(self):
        if folder_name:
            # 取得したパスを格納するために空のリストを作成
            paths = []
            # 画像ファイルかの判断に使う
            exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

            # 選択したフォルダの中身を取得
            for root, dirs, files in os.walk(folder_name):
                for name in files + dirs:
                    image_path = os.path.join(root, name)
                    # パスの末尾の文字列（拡張子）を見て画像ファイルの場合のみリストに追加
                    if image_path.endswith(exts):
                        paths.append(image_path)
            self.all_images_paths = paths
            self.random_select_images(self.all_images_paths)
        # フォルダ未選択時にエラーメッセージボックス表示
        else:
            messagebox.showerror('エラー','フォルダを選択してください')

    # 格納した絶対パスからランダムで１つ取り出す      
    def random_select_images(self, paths):
        self.random_image = random.choice(paths)
        self.display_image()

    # 選出した画像を表示
    def display_image(self):
        # Image.openで開ける形になるように文字列を置換
        self.random_image = self.random_image.replace('\\','/')
        self.random_image = self.random_image.replace('/','//')
        self.op_img = Image.open(self.random_image)

        # 画像のサイズを取得
        w = self.op_img.width
        h = self.op_img.height
        print(str(self.op_img.width) + '×' + str(self.op_img.height))

        # 画像の横幅がcanvasの横幅より大きい場合リサイズ
        if w > self.canvas_w:
            self.resize_img = self.op_img.resize((int(w * (self.canvas_w / w)), int(h * (self.canvas_w / w))))
            w = self.resize_img.width
            h = self.resize_img.height
            print('画像の横幅がcanvasの横幅より大きい場合リサイズ')
            print(str(self.resize_img.width) + '×' + str(self.resize_img.width))
            
        # 画像の縦幅がcanvasの縦幅より大きい場合リサイズ
        if h > self.canvas_h:
            self.resize_img = self.op_img.resize((int(w * (self.canvas_h / h)), int(h * (self.canvas_h / h))))
            w = self.resize_img.width
            h = self.resize_img.height
            print('画像の縦幅がcanvasの縦幅より大きい場合リサイズ')
        
        print(str(self.resize_img.width) + '×' + str(self.resize_img.height))

        # 画像を表示

        self.display_img = ImageTk.PhotoImage(self.resize_img)
        self.canvas.create_image((self.canvas_w - w) / 2, (self.canvas_h - h) / 2, image=self.display_img, anchor=tk.NW)
        self.canvas.bind('<Button-1>',self.image_clicked)
    
    # 画像クリック時の処理（引数にevent必須！）※
    def image_clicked(self,event):
        self.op_img.show()

    def wedget(self,root):
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
        next_btn = tk.Button(root, text='NEXT', font=('', 20), command=self.load_images)
        next_btn.place(relx=0.9, rely=0.9, anchor=tk.SE, width=200, height=40)
        # tk.NE：座標の基準位置をボタン右上に
        folder_btn = tk.Button(root, text='フォルダ選択', command=self.filedialog_clicked)
        folder_btn.place(relx=0.9, rely=0.1, anchor=tk.NE, width=200, height=40)

        # canvas（画像表示範囲）の作成
        self.canvas_w = 600
        self.canvas_h = 600
        self.canvas = tk.Canvas(root, width=self.canvas_w, height=self.canvas_h, bg='#E7E7E7', cursor='hand2')
        self.canvas.place(x=0, y=0)

# tkオブジェクトの作成
root = tk.Tk()
# ウィンドウのサイズと出現位置
root.geometry('1000x600+200+50')

# クラスの呼び出し？
RandomViewerApp(root)

# メインループの実行
root.mainloop()
