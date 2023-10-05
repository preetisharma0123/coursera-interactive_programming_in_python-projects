# implementation of card game - Memory

import simplegui
import random

list1 = range(0,8)
list2 = range(0,8)
State = 0
cards = list1+list2
random.shuffle(cards)
card_pos = [0,80]
exposed = [ False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
turns = 0

# helper function to initialize globals
def new_game():     
    global state,exposed,turns,cards
    state = 0
    turns = 0
    exposed = [ False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    random.shuffle(cards)
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card_pos,cards,state,card_index1,card_index2,turns
   
    if state == 0:
        state = 1 
        turns += 1
        card_index1 = pos[0] // 50
        if not(exposed[card_index1]):
            exposed[card_index1] = True
        print "card_index1: ",card_index1
        
    elif state == 1:
        state = 2
        card_index2 = pos[0] // 50
        if not(exposed[card_index2]):
            exposed[card_index2] = True
        print "card_index2: ",card_index2
         
    elif state ==2:
        if cards[card_index1] != cards[card_index2]:
                exposed[card_index1] =  False
                exposed[card_index2] =  False
                    
        state = 1
        turns +=1
        card_index1 = pos[0] // 50
        if not(exposed[card_index1]):
            exposed[card_index1] = True
        print "card_index1: ", card_index1
    

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global position,cards,card_pos,exposed
    
    for card_index in range(len(cards)):   
        card_pos[0] =50*card_index
        if exposed[card_index]:
            canvas.draw_text(str(cards[card_index]),card_pos,80,"white")                
        else:
            canvas.draw_polygon([[card_pos[0],card_pos[1]-100],[card_pos[0]+50, card_pos[1]-100],[card_pos[0]+50,card_pos[1]+100],[card_pos[0],card_pos[1]+50]],1, 'black', 'green')
    label.set_text('"Turns = '+str(turns)+'"')          
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

