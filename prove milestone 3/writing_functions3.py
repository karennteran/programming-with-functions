# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky, draw_clouds and draw_ground here.
    draw_sky(canvas)
    draw_clouds(canvas, 50, 350, 350, 400)
    draw_clouds(canvas, 100, 375, 320, 420)
    draw_clouds(canvas, 450, 400, 750, 450)
    draw_clouds(canvas, 520, 375, 755, 415)
    
    
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#


# trying to do snow flakes
    half_height = round(scene_height / 1.5 + 25)
    min_diam = 5
    max_diam = 20
    for i in range(350):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="", fill="white")
        # draw_oval(canvas, x, y, x + min_diam, y + min_diam, fill="black")



#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#


# bottom circle of the snowman
    #  firts number is the left side, second number is the bottom side, third number is the top side, and fourth number is the top side.
    draw_snowman(canvas, 235, 100, 365, 220)

# tope circle of teh snowman
    #  firts number is the left side, second number is the bottom side, third number is the top side, and fourth number is the top side.
    draw_snowman(canvas, 250, 200, 350, 285)



# ***********************************************************************************************#
# ***********************************************************************************************#
    draw_sun(canvas)
    draw_ground(canvas)
    # calling the function to draw the grids
    # draw_grid(canvas, scene_width, scene_height, 50)

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
            
    # draw another pine tree on the right side
    tree_center_x = 450
    tree_bottom = 130
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    tree_center_x = 650
    tree_bottom = 50
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas):
    draw_rectangle(canvas, 0, 150, 800, 500, outline="", fill="skyblue")

def draw_clouds(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, outline="", fill="white")
    draw_oval(canvas, x0, y0, x1, y1, outline="", fill="white")

def draw_sun(canvas):
    draw_oval(canvas, 350, 400, 450, 500, outline="", fill="yellow")

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="white", width=1, fill="snow1")   
    
def draw_ground(canvas):
    draw_rectangle(canvas, 0, 0, 800, 150, outline="", fill="white")
    draw_line(canvas, 0, 30, 800, 0, width=55, fill="dodgerblue3")
    
    for x in range(0, 800, 10):
        draw_line(canvas, x, 0, 5, 55, width=1, fill="royalBlue4")

# drawing the grid
def draw_grid(canvas, width, height, interval):
    # draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
        
    # draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}") 

#  drawing a snowman
def draw_snowman(canvas, x0, y0, x1, y1):
    # drawing ovals for the snowballs of the snowman
    draw_oval(canvas, x0, y0, x1, y1, outline="", fill="white")
    # drawing rectangles for the snowman's hat
    draw_rectangle(canvas, 250, 270, 350, 280, outline="", fill="black")
    draw_rectangle(canvas, 265, 280, 335, 325, outline="", fill="black")
    # drawing ovals for the eyes
    draw_oval(canvas, 275, 250, 285, 260, outline="", fill="black")
    draw_oval(canvas, 325, 250, 335, 260, outline="", fill="black")
    # drawing ovals for the buttons
    draw_oval(canvas, 295, 190, 305, 200, outline="", fill="black")
    draw_oval(canvas, 295, 160, 305, 170, outline="", fill="black")
    # drawing lines for the hands
    # the first tow lines of draw lines is the right hand the other two is the left hand
    draw_line(canvas, 350, 200, 370, 220,  width=5, fill="tan3")
    draw_line(canvas, 360, 210, 360, 240, width=5, fill="tan3")
    draw_line(canvas, 250, 200, 230, 220,  width=5, fill="tan3")
    draw_line(canvas, 240, 210, 240, 240, width=5, fill="tan3")
    #drawing the snowman's nose
    # draw_polygon(canvas, 300, 240, 300, 220, width=1, fill="darkOrangee")
    draw_polygon(canvas,
        300, 245, 300, 230, 320, 230, outline="", fill="darkOrange")
    


# Call the main function so that
# this program will start executing.
main()