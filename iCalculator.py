'''
A simple calculator powered by Python tkinter.
author: Xingjian
date: 2018/10/16
'''
import tkinter as tk

class Calculator(object):
    def __init__(self):
        '''constructor'''
        # private attribute
        self.__window = tk.Tk() # 生成窗口
        self.__window.title('iCalculator') # 设置窗口标题
        self.__window.geometry('317x340')  # 设置窗口大小
        self.__window.wm_resizable(0, 0)  # 窗口大小不可调节
        self.createWidgets()
        self.__window.mainloop()

    def createWidgets(self):
        self.__entry = tk.Entry(self.__window,width=45)
        self.__entry.grid(row=0, columnspan=4)  # 文本框
        # 第二行
        second = 1
        self.createButton(second,('AC','+/-','%','÷'))
        # 第三行
        third = 2
        self.createButton(third, ('7', '8', '9', '×'))
        # 第四行
        forth = 3
        self.createButton(forth, ('4', '5', '6', '-'))
        # 第五行
        fifth = 4
        self.createButton(fifth, ('1', '2', '3', '+'))
        # 第六行
        sixth = 5
        self.createButton(sixth, ('0', '.', '='))

    def createButton(self,row,textTuple,btn_height = 3,bg_color = 'orange',sticky = tk.W+tk.E+tk.N+tk.S):
        col = 0
        for x in textTuple:
            button = tk.Button(self.__window,text=x,height=btn_height,bg=bg_color)
            if x == '0':
                button.grid(row=row, column=col,columnspan=2,sticky=sticky)
                col += 1
            else:
                button.grid(row=row,column=col,sticky=sticky)
            # bind event
            button.bind('<Button-1>',self.clickHandler)
            col += 1

    def clickHandler(self,event):
        widget = event.widget
        text = widget['text']
        print(text)

        if text == 'AC':
            self.__entry.delete(0,tk.END)
        elif text == '+/-':
            try:
                num = eval(self.__entry.get())
            except:
                self.__display("Error")
            else:
                self.__display(str(-num))
        elif text == '%':
            try:
                num = eval(self.__entry.get())
            except:
                self.__display("Error")
            else:
                self.__display(str(num/100))
        elif text == '=':
            try:
                old = self.__entry.get()
                temp = old.replace('÷','/')
                temp = temp.replace('×','*')
                result = eval(temp)
            except:
                self.__display("Error")
            else:
                self.__display(str(result))
        else:
            self.__entry.insert(tk.END,text)

    def __display(self,content):
        '''private method'''
        self.__entry.delete(0, tk.END) # delete before
        self.__entry.insert(tk.END, content)

# main
if __name__ == '__main__':
    Calculator()
