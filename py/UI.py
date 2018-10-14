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
labelTitle = Label(window, text="Performance Comparison Between DES and RSA Algorithm", font=("Arial", 22), height=4)
labelTitle.grid(row=0, column=0, columnspan=8, sticky=W)

# 明/密文输入标签
labelInput = Label(window, text="Input:").grid(row=1, column=0, sticky=W)

# 密码输入标签
labelPassword = Label(window, text="Password:").grid(row=1, column=2, sticky=W)

# 明/密文输入框
entryInput = Entry(window).grid(row=1, column=1, sticky=W)

# 密码输入框
entryPassword = Entry(window, show="#").grid(row=1, column=3, sticky=W)

# 加密或是解密
var = IntVar()
var.set(1)
radioButtonEncrypt = Radiobutton(window, text="Encrypt", variable=var, value=1).grid(row=2, column=2, sticky=W)
radioButtonDecrypt = Radiobutton(window, text="Decrypt", variable=var, value=2).grid(row=3, column=2, sticky=W)

# 提交按钮
submitButton = Button(window, text="Submit").grid(row=4, column=0, sticky=E)

# 界面控制
Label(window, text="======== Result ========").grid(row=5, column=0, columnspan=2, sticky=W)

# DES结果标签
outputLabel_DES = Label(window, text="Output From DES:").grid(row=6, column=0, sticky=W)

# DES结果显示框
outputText_DES = Entry(window).grid(row=6, column=1, sticky=W)

# RSA结果标签
outputLabel_RSA = Label(window, text="Output From RSA:").grid(row=7, column=0, sticky=W)

# RSA结果显示框
outputText_RSA = Entry(window).grid(row=7, column=1, sticky=W)


# 窗口循环
window.mainloop()
