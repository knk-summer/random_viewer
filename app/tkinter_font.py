import tkinter as tk
import tkinter.font as tkFont

def show_font_popup(font_family):
    popup = tk.Toplevel()
    popup.title(font_family)
    label = tk.Label(popup, text=font_family, font=(font_family, 100))
    label.pack(padx=10, pady=10)

def on_mouse_wheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, 'units')
    elif event.delta < 0:
        canvas.yview_scroll(1, 'units')

root = tk.Tk()
root.title("Available Fonts")

# フォントファミリーを取得
font_families = tkFont.families()

# キャンバスウィジェットを作成してスクロール可能にする
canvas = tk.Canvas(root, borderwidth=0)
frame = tk.Frame(canvas)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

frame.bind("<Map>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# ラベルの幅と高さを設定
button_width = 20  # 文字数での幅
button_height = 1  # 行数での高さ

# ウィンドウのサイズ
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# 1行あたりのラベル数を計算
num_columns = window_width // (button_width * 10)
num_rows = (len(font_families) + num_columns - 1) // num_columns

# グリッド配置
for index, font_family in enumerate(font_families):
    row = index // num_columns
    column = index % num_columns

    button = tk.Button(frame, text=font_family, font=(font_family, 8), width=button_width, height=button_height, anchor="w")
    button.grid(row=row, column=column, padx=5, pady=2, sticky="nsew")
    button.bind("<Button-1>", lambda e, font_family=font_family: show_font_popup(font_family))

root.mainloop()