from tkinter import *

root = Tk()
root.geometry("400x300")

def f_event(event, key):
    print(event, key)

c_label = Label(root, bg="#fff")
c_label.pack( pady=10, fill=X,)

# создаем словарь 
colors = {
    "#FE080D" : "Красный",
    "#FE9307" : "Оранжевый",
    "#FEF506" : "Желтый",
    "#41C903" : "Зеленый",
    "#2AC3FC" : "Голубой",
    "#0225F3" : "Синий",
    "#5630C3" : "Фиолетовый",
}

class MyButtonsColor:
    def __init__(self, master, color):
        self.color = color
        self.squad_color = Label(master, bg=color, width=4, height=2)
        self.squad_color.pack(side=LEFT, padx=1)
        self.squad_color.bind("<Button-1>", lambda event, key="lk": self.get_color(event, key))
        self.squad_color.bind("<Button-3>", lambda event, key="rk": self.get_color(event, key))
        
    def get_color(self, event, key):
        if key == "lk":
            c_label["bg"] = self.color
        elif key == "rk":
            c_label["bg"] = "#fff"

for k, v in colors.items():
    MyButtonsColor(root, k)

root.mainloop()