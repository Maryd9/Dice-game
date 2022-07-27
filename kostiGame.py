from tkinter import *
from PIL import Image, ImageTk
import random, time

def game():
    x = random.choice(['1.png','2.png','3.png','4.png','5.png','6.png'])
    return x

def img(event):
    global img1, img2
    #Создание эффекта перемешивания
    for i in range(20):
        img1 = ImageTk.PhotoImage(file=(game()))
        img2 = ImageTk.PhotoImage(file=(game()))
        lab1['image'] = img1
        lab2['image'] = img2
        #Обновление экрана при перемешивании
        root.update()
        time.sleep(0.0012)

root = Tk()
root.geometry('400x200')
root.title('Игра в кости 🎲')

#Запрет на изменение размера окна
root.resizable(height=False, width=False)

#Уставновка фона
background = ImageTk.PhotoImage(Image.open("holst.png"))
Label(root, image=background).pack()

#Уставновка расположения для первого кубика
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)

#Уставновка расположения для второго кубика
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

#Смена костей нажатием
root.bind('<1>', img)

img('event')

root.mainloop()
