# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
num_range = 100
global secret_number 
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global remaining
    secret_number = random.randrange(0, num_range)
    if num_range == 100 : 	
        remaining = 7
    elif num_range == 1000 :
        remaining = 10
    print "New game. The range is from 0 to", num_range, ". Good luck!"
    print "Number of remaining guesses is ", remaining, "\n"
    


  
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100 
    
    new_game()    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000    
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global remaining
    global secret_number
    remaining -=1 
    if remaining >=0 :    
        print " Guess was ", int(guess)
              
        print remaining, "guesses remaining"
        guess = int(guess)
    # remove this when you add your code
        
        if guess>secret_number:
            print " lower!"
        elif guess<secret_number:
            print "Higher!"
        else: 
            print "Correct! Congratulations" "/n"
            new_game()

    else:         
        print " You ran out of guesses. Better luck next time!  The number was",secret_number 
        
        new_game()
# create frame
frame = simplegui.create_frame("frame",200, 200)


# register event handlers for control elements and start frame
frame.add_input("enter here", input_guess, 100)
frame.add_button("Range is (0,100)", range100, 100)
frame.add_button("Range is (0,1000)", range1000, 100)

# call new_game 
new_game()
frame.start()