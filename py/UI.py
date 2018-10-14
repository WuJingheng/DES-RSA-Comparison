# coding:UTF-8

# 导入tkinter库
from Tkinter import *

# 创建窗口
window = Tk()

# 窗口标题
window.title("Performance Comparison Between DES and RSA Algorithm")

# 窗口大小
window.geometry("800x500")

# 窗口内标题
labelTitle = Label(window,
                   text="Performance Comparison Between DES and RSA Algorithm",
                   font=("Arial", 22),
                   height=4
                   ).grid(row=0, column=0, columnspan=8, sticky=W)

# 明/密文输入标签
labelInput = Label(window, text="Input:").grid(row=1, column=0, sticky=W)

# 密码输入标签
labelPassword = Label(window, text="Password:").grid(row=1, column=5, sticky=W)

# 明/密文输入框
entryInput = Entry(window).grid(row=1, column=1, sticky=W)

# 密码输入框
entryPassword = Entry(window, show="#").grid(row=1, column=6, sticky=W)

# 加密或是解密
var = IntVar()
var.set(1)
radioButtonEncrypt = Radiobutton(window, text="Encrypt", variable=var, value=1).grid(row=2, column=5, sticky=W)
radioButtonDecrypt = Radiobutton(window, text="Decrypt", variable=var, value=2).grid(row=3, column=5, sticky=W)

# 窗口循环
window.mainloop()
