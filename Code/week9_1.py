import tkinter as tk
from tkinter import ttk
from random import randint
import simpleaudio as sa
import os
import simpleaudio as sa

class KidsGame(tk.Tk):

    def __init__(self):
        super().__init__()

        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()

        self.count = 0

        # Creating window
        self.title('Math game')
        self.resizable(0, 0)
        self.geometry('315x130')
        self['bg'] = 'lightblue'

        # Creating num1 label
        self.labelNum1 = ttk.Label(
            self,
            text=self.get_Num1(),
            font = ('Digital-7', 40))
            
        self.labelNum1.place(x=15, y=20)

        # Styling labels
        self.styleLabel = ttk.Style(self)
        self.styleLabel.configure(
            'TLabel',
            background = 'lightblue',
            foreground = 'black')

        self.labelPlus = ttk.Label(
            self,
            text='+',
            font=('Digital', 35))

        # Creating num2 label
        self.labelNum2 = ttk.Label(
            self,
            text=self.get_Num2(),
            font = ('Digital-7', 40))

        self.labelNum2.place(x=117, y=20)

        self.labelEquals = ttk.Label(
            self,
            text='=',
            font=('Digital', 35))

        self.entrySum = ttk.Entry(
            self,
            font=('Digital', 40))
            
        self.entrySum.place(x=235, y=25, width=65, height=50)

        # Creating a button to start timer with
        self.checkAnswer = ttk.Button(
            self,
            text='Check answer',
            command=lambda:self.check_Sum(self.entrySum))

        self.checkAnswer.place(x=175, y=90)

        # Creating button for refreshing numbers
        self.refreshNums = ttk.Button(
            self,
            text='Refresh',
            command=lambda:self.call_Both()) # Calling 2 functions at once

        self.counterLabel = ttk.Label(
            self,
            text=self.count
        )
        
        self.counterLabel.place(x=5, y=5)

        self.refreshNums.place(x=55, y=90)

        self.get_Places()

    def get_Num1(self):
        self.randomNum1 = randint(1, 50)

        return self.randomNum1

    def get_Num2(self):
        self.randomNum2 = randint(1, 50)

        return self.randomNum2

    def check_Sum(self, entrySum):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        correctSoundFilePath = dir_path + '\\correctSound.wav'
        incorrectSoundFilePath = dir_path + '\\incorrectSound.wav'
        correctSound = sa.WaveObject.from_wave_file(correctSoundFilePath)
        incorrectSound = sa.WaveObject.from_wave_file(incorrectSoundFilePath)
    
        sum = self.randomNum1 + self.randomNum2
        
        if entrySum.get() == str(sum):
            print('Correct result')
            self.count += 1
            self.get_Count()
            correctSound.play()
            self.entrySum.delete(0, 'end')
            self.update_Nums()
        else:
            print('Incorrect result')
            incorrectSound.play()
            self.count = 0
            self.entrySum.delete(0, 'end')
            self.get_Count()


    def update_Nums(self):
        self.labelNum1.config(text=self.get_Num1())
        self.labelNum2.config(text=self.get_Num2())

        self.get_Places()

        self.entrySum.delete(0, 'end') # Clearing entry box

    def get_Places(self):
        self.get_current_Nums()

        # Setting conditions for placing '=' sign
        if self.curNum1 > 9 and self.curNum2 < 10:
            self.labelEquals.place(x=188, y=22)
            self.labelNum2.place(x=133, y=20)
        if  self.curNum1 <= 9 and self.curNum2 >= 10:
            self.labelEquals.place(x=192, y=22)
            self.labelNum2.place(x=122, y=20)
        if self.curNum1 > 9 and self.curNum2 >= 10:
            self.labelEquals.place(x=193, y=22)
            self.labelNum2.place(x=118, y=20)
        if self.curNum1 <= 9 and self.curNum2 < 10:
            self.labelEquals.place(x=187, y=22)
            self.labelNum2.place(x=136, y=20)

        # Setting conditions for placing '+' sign
        if self.curNum1 > 9 and self.curNum2 < 10:
            self.labelPlus.place(x=85, y=22)
        if self.curNum1 > 9 and self.curNum2 >= 10:
            self.labelPlus.place(x=84, y=22)
        if self.curNum1 <= 9 and self.curNum2 >= 10:
            self.labelPlus.place(x=72, y=22)
        if self.curNum1 <= 9 and self.curNum2 < 10:
            self.labelPlus.place(x=72, y=22)

    def get_current_Nums(self):
        self.curNum1 = self.randomNum1
        self.curNum2 = self.randomNum2

        return self.curNum1, self.curNum2

    def get_Count(self):
        self.counterLabel.config(text=self.count)

    def minus_One(self):
        if self.count != 0:
            self.count -= 1
        self.update_Nums()
        self.get_Count()

    def call_Both(self):
        self.update_Nums()
        self.minus_One()

        
if __name__ == "__main__":
    game = KidsGame()
    game.mainloop()