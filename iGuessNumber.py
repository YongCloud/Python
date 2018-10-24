# guess number game
import tkinter as tk
from random import randint

class GuessNumber(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
        self.__rand = randint(a,b)
        self.__window = tk.Tk()
        self.__window.title('iGuessNumber')
        self.__window.geometry("300x150")
        self.__window.wm_resizable(0, 0)
        self.createWidgets()
        self.__window.mainloop()

    def createWidgets(self):
        text = "please input a integer in [%s,%s]"%(self.__a,self.__b)
        self.__tipLabel = tk.Label(self.__window,text = text)
        self.__tipLabel.pack()
        self.__entry = tk.Entry(self.__window,width=30)
        self.__entry.pack()
        self.__resultLabel = tk.Label(self.__window)
        self.__resultLabel.pack()
        self.__button = tk.Button(self.__window,text = "guess")
        self.__button.pack()
        self.__button.bind('<Button-1>',self.clickHandler)

    def clickHandler(self,event):
        widget = event.widget
        text = widget['text']

        try:
            content = self.__entry.get()
            num = int(content)
            self.__entry.delete(0,tk.END)
            if num > self.__b or num < self.__a:
                self.__resultLabel['text'] = "input error!"
            elif num == self.__rand:
                self.__entry.insert(tk.END,content)
                self.__resultLabel['text'] = "congratulations!"
            elif num < self.__rand:
                self.__a = num
                self.__resultLabel['text'] = "guess wrong!"
            else:
                self.__b = num
                self.__resultLabel['text'] = "guess wrong!"
        except:
            self.__resultLabel['text'] = "input error!"
        else:
            text = "please input a integer in [%s,%s]"%(self.__a,self.__b)
            self.__tipLabel['text'] = text

# main
if __name__ == '__main__':
    GuessNumber(1,100)
