#"Stopwatch: The Game"


import simplegui
# define global variables
WIDTH = 200
HEIGHT = 200
time = 0
x = 0
y = 0
z = str(x)+"/"+str(y)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    A= time//600
    B= (time%600)//100
    C= ((time%600)//10)%10
    D= (time%600)%10
    
    text1= str(A)+":"+str(B)+str(C)+"."+str(D)
   
    return text1
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    
    if timer.is_running():
        
        timer.stop()
        
        global x, y,z
        if((time%600)%10) ==0:
            x+=1
            y+=1
        else:
            y +=1
    
        z = str(x)+"/"+str(y)
        return z
        
    
def reset():
    global time,x,y,z
    time = 0
    x= 0
    y = 0
    z = str(x)+"/"+str(y)
    timer.stop()
    
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time +=1
    return time

# define draw handler
def draw_handler( canvas):
    canvas.draw_text(format(time),(WIDTH/3, HEIGHT/2),35,"white")
    canvas.draw_text(z,(WIDTH-35,20),25,"red")
                     
    
# create frame
frame = simplegui.create_frame("frame", WIDTH,HEIGHT)
frame.set_draw_handler(draw_handler)

# register event handlers
timer = simplegui.create_timer(100,tick)

frame.add_button("Start",start)
frame.add_button("Stop",stop)
frame.add_button("reset",reset)

# start frame
frame.start()


