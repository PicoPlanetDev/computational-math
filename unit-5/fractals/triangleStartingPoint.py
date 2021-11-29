from tkinter import *

def drawTriangle(canvas,x,y,length,level,color):
    return None


def run():
    root = Tk()
    canvas = Canvas(root, width=800, height=650)
    canvas.pack()
    level=0
    canvas.create_polygon(100,600,700,600,700,100,100,100,fill='red')
    root.mainloop()
run()
