# ライブラリのインポート（asで別名をつけてる）
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import random
import os

# 【作業】以下をRandomViewerAppクラスとしてまとめる（裏側の処理はここにまとめたい）
# 【メモ】全画像パス、ランダムで選出した画像パスの２つクラス変数が必要？初期値は空文字で
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
        self.random_select_images(self.all_images_paths)
        # print(self.folder_name)       
        # print(self.random_image)
        # img = Image.open(self.random_image)

    # 選択したフォルダ内の全画像ファイルの絶対パスを取得
    def load_images(self):
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
        # self.display_image()

        
        # ※確認用なので後で消す            
        # print(paths)
        # print(random.choice(paths))
        
        # 【作業】取得したパスをランダムに選出する用の関数を用意する
        # 【作業】random.choiceの引数はクラス変数を使用する
        # 【作業】クラス変数が格納されているかで分岐（フォルダ選択前にNEXTを押された時用）
    def random_select_images(self, paths):
        self.random_image = random.choice(paths)
        self.random_image = self.random_image.replace('\\','/')
        self.random_image = self.random_image.replace('/','//')
        self.display_image()

    def display_image(self):
        img = Image.open(self.random_image)

        # 画像のサイズを取得
        w = img.width
        h = img.height

        # 画像の縦幅がcanvasの縦幅より大きい場合リサイズ
        if w > self.canvas_w:
            img = img.resize((int(w * (self.canvas_w / w)), int(h * (self.canvas_w / w))))
            
        # 画像の横幅がcanvasの横幅より大きい場合リサイズ
        if h > self.canvas_h:
            img = img.resize((int(w * (self.canvas_h / h)), int(h * (self.canvas_h / h))))

        # 画像を表示

        self.display_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.display_img, anchor=tk.NW)

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
        self.canvas = tk.Canvas(root, width=self.canvas_w, height=self.canvas_h,bg='blue')
        self.canvas.place(x=0, y=0)

        # if self.random_image:
        #     label1['text'] = self.random_image
        #     label1.update()

        # label1 = tk.Label(root, text='ラベル１')
        # label1.place(x=100, y=50)

        # img = Image.open('\\Users\\hydra\\Documents\\★好きなもの（Twitterアーカイブ）\\写真\\ふりーな_kan_me.png')
   

        # self.display_image(app)
        # if self.app.random_image:
        #     label1.update()
        #     label1['text'] = self.app.random_image
        # global img
        # img = Image.open('fuyo.png')
        # img = ImageTk.PhotoImage(img)
        # canvas.create_image(0, 0, image=img, anchor=tk.NW)

        # print(self.app.random_image)
        # self.display_image(root,self.app)

        # 【作業】ランダムで1つ画像を選んで変数に格納→Image.openの引数に
# 【作業】RandomViewerクラスのオブジェクトを作成して変数を使用する
    # def display_image(self,root):
        # print(self.app.random_image)
        # current_img = relative_to(self.app.random_image)
        # img = Image.open('C:\\Users\\hydra\\Documents\\★好きなもの（Twitterアーカイブ）\\写真\\fuyo.png')

        # # 画像のサイズを取得
        # w = img.width
        # h = img.height

        # # 画像の縦幅がcanvasの縦幅より大きい場合リサイズ
        # if w > self.canvas_w:
        #     img = img.resize((int(w * (self.canvas_w / w)), int(h * (self.canvas_w / w))))
            
        # # 画像の横幅がcanvasの横幅より大きい場合リサイズ
        # if h > self.canvas_h:
        #     img = img.resize((int(w * (self.canvas_h / h)), int(h * (self.canvas_h / h))))

        # # 画像を表示

        # display_img = ImageTk.PhotoImage(img)
        # self.canvas.create_image(0, 0, image=display_img, anchor=tk.NW)


# tkオブジェクトの作成
root = tk.Tk()
# ウィンドウのサイズと出現位置
root.geometry('1000x600+200+50')

# クラスの呼び出し？
RandomViewerApp(root)

# メインループの実行
root.mainloop()
