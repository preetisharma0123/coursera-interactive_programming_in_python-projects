# each press of the up arrow increases the radius of the white ball centered in the middle of the canvas by a small fixed amount and each press 
#of the down arrow key decreases the radius of the ball by the same amount

import simplegui

WIDTH = 300
HEIGHT = 200
ball_radius = 50
BALL_RADIUS_INC = 3

# Handler for keydown
def keydown(key):
    global ball_radius
    if key == simplegui.KEY_MAP["up"]:
        ball_radius += BALL_RADIUS_INC
    elif key == simplegui.KEY_MAP["down"]:
        ball_radius -= BALL_RADIUS_INC

# Handler to draw on canvas
def draw(canvas):
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()