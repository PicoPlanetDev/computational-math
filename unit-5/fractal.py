import math 
import tkinter as tk
import random

def fractal(x, y, side, a, b, depth, recursion):
    # Create four corners of next square
    angle_x = side * math.sin(a)
    angle_y = side * math.cos(a)

    x1 = x + angle_x
    y1 = y - angle_y

    x2 = x + angle_x-angle_y
    y2 = y - angle_y-angle_x

    x3 = x - angle_y
    y3 = y - angle_x

    x4 = x - angle_y + side * math.cos(b) * math.sin(a - b)
    y4 = y - angle_x - side * math.cos(b) * math.cos(a - b)
    
    # Random colors look pretty cool in this fractal
    # This randomizer creates colors in hex format
    # which looks like this #RRGGBB where R, G, and B are hex values
    # which can range from 00 to FF
    random_color = "#%06x" % random.randint(0, 0xFFFFFF)

    # Actually draw it
    canvas.create_polygon(x, y, x1, y1, x2, y2, x3, y3, fill=random_color)
    canvas.create_polygon(x3, y3, x2, y2, x4, y4, fill=random_color)
    
    # Recurse
    if depth >= 2:
        fractal(x4, y4, side*math.sin(b), a - b + (0.5*math.pi), b, depth-1,recursion+1)
        fractal(x3, y3, side*math.cos(b), a - b, b, depth-1,recursion+1)

print("Fractal... 20pts")
root=tk.Tk()
root.title("Fractal")
canvas = tk.Canvas(root, width = 800, height = 600)
canvas.pack()
# Right now the depth is set to 12. Pretty much everything over 12 is too slow.
curl = 1 # 0.5 curls it left, 1.0 curls it right, 0.75 is no curl, above 1 is unpredictable
fractal(330, 430, 75, 0.5*math.pi,curl*(math.pi/3), 12, 1) 
root.mainloop()