# a program that draws a polyline (an open polygon) based on a sequence of mouse clicks. The first click creates a point. Subsequent clicks add a new segment to the polyline


import simplegui
import math

polyline = []


# define mouseclick handler
def click(pos):
    polyline.append(pos)
          
# button to clear canvas
def clear():
    global polyline
    polyline = []

# define draw
def draw(canvas):
    if len(polyline) > 0:
        canvas.draw_circle(polyline[0], 1, 1, "White", "White")
        canvas.draw_polyline(polyline, 2, "White")
                    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()

