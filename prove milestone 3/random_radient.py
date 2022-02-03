
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500     

    canvas = start_drawing("Scene", scene_width, scene_height)
    
    half_height = round(scene_height / 2)
    min_diam = 200
    max_diam = 600
    for i in range(100):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y. x + diameter, y + diameter, fill="lightgray")


def draw_sky(canvas):
    draw_rectangle(canvas, 0, 150, 800, 500, outline="", fill="skyblue")

def draw_sun(canvas):
    draw_oval(canvas, 350, 400, 450, 500, outline="", fill="yellow")

def draw_ground(canvas):
    draw_rectangle(canvas, 0, 0, 800, 150, outline="", fill="green")

main()