# ライブラリのインポート（asで別名をつけてる）
import tkinter as tk
import customtkinter

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

# ウィジェットの配置（pack()：ウィジェットを順番に配置）
# btn1 = tk.Button(root, text='テストボタン1')
# btn1.pack(side=tk.RIGHT, fill=tk.Y)

# btn2 = tk.Button(root, text='テストボタン2')
# btn2.pack(side=tk.TOP, fill=tk.X)

# btn3 = tk.Button(root, text='テストボタン3')
# btn3.pack(side=tk.LEFT, fill=tk.X, expand=True)

# ウィジェットの配置（grid()：ウィジェットを行列形式で配置）
# label1 = tk.Label(root, text='ラベル1')
# label1.grid(row=0, column=0)

# btn1 = tk.Button(root, text='テストボタン1')
# btn1.grid(row=1, column=0)

# btn2 = tk.Button(root, text='テストボタン2')
# btn2.grid(row=1, column=1)

# btn3 = tk.Button(root, text='テストボタン3')
# btn3.grid(row=2, column=0, columnspan=2)

# btn4 = tk.Button(root, text='テストボタン4')
# btn4.grid(row=3, column=0, columnspan=3, sticky=tk.W+tk.E)

# ウィジェットの配置（place()：ウィジェットを座標で配置）
label1 = tk.Label(root, text='ラベル1')
label1.place(x=100, y=50)

btn1 = tk.Button(root, text='テストボタン1')
btn1.place(relx=0.1, rely=0.1)

btn2 = tk.Button(root, text='テストボタン2')
btn2.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

# メインループの実行
root.mainloop()