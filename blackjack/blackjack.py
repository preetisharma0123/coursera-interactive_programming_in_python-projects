# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
wins = 0
losses = 0
score = wins - losses
hand_value = 0
player_hand = [] 
dealer_hand = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = [] # create Hand object

    def __str__(self):
        ans = "hand contains "
        for i in range(len(self.cards)):
            ans += str(self.cards[i])+" "
        return ans  # return a string representation of a hand

    def add_card(self, card):
       
        return self.cards.append(card)  # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        global hand_value,in_play
        hand_value = 0
        for i in self.cards:           
            hand_value += VALUES[i.get_rank()]
            
        for i in self.cards:
            if i.get_rank() != "A":
                return hand_value
            elif hand_value +10 <=21:
                return hand_value + 10
            else:
                return hand_value
        return hand_value
   
    def draw(self, canvas, pos):
        
        for c in self.cards:
            c.draw(canvas, pos) # draw a hand on the canvas, use the draw method for cards
            pos[0] +=  100
            
# define deck class 
class Deck:
    def __init__(self):
        self.Card1 = [] # create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.Card1.append(Card(i, j))
                    
    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.Card1)    # use random.shuffle()

    def deal_card(self):
        return random.choice(self.Card1)    # deal a card object from the deck
    
    def __str__(self):
                # return a string representing the deck
        deck = "Deck contains "
        for i in range(len(self.Card1)):
            deck += str(self.Card1[i]) + " "
        return deck 
     
#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, my_deck, losses,hand_value   
        
    # your code goes here
    if in_play == True:
        outcome = "Player lost the round! New game?"
        losses +=1
        in_play = False
    else: 
        hand_value = 0
        player_hand = Hand()
        dealer_hand = Hand()
        my_deck = Deck()
        my_deck.shuffle()
        player_hand.add_card(my_deck.deal_card())
        player_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        print "player_hand: ",player_hand,player_hand.get_value()
        print "dealer_hand: ",dealer_hand,dealer_hand.get_value()
        in_play = True
        outcome = "Hit or stand?"
    return losses
    
def hit():
    # replace with your code below
    global outcome, in_play,losses
    # if the hand is in play, hit the player
    if in_play == False:
        return
    elif player_hand.get_value() <21:
        player_hand.add_card(my_deck.deal_card())
    elif player_hand.get_value() == 21:        
        stand()
        Message = "You have reached limit of 21. Your only option is to stand"
    else:           
        outcome = "You have busted. New deal??"
        player_hand.add_card(my_deck.deal_card())
        in_play = False
        losses +=1
        return losses
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global in_play,outcome,losses,wins
    if in_play == False:
        return
    while (dealer_hand.get_value() <=17):
        dealer_hand.add_card(my_deck.deal_card())
        
    if player_hand.get_value() >21:
        outcome = "You have busted. New deal??"
        losses +=1    
        in_play = False
        return losses
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if dealer_hand.get_value() >21:
        outcome = "Dealer has busted. New deal??"
        wins += 1  
        in_play = False
        return wins
        
    elif dealer_hand.get_value() >=player_hand.get_value():
        outcome = "Dealer wins. New deal??"
        losses +=1
        in_play = False
        return losses
        
    else: 
        outcome = "Player wins!! Congrats!!. New deal?"
        wins += 1
        in_play = False
        return wins
        
    # assign a message to outcome, update in_play and score
   
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text("Blackjack",(250,50),25, 'yellow')
    canvas.draw_text(outcome,(50,150),22, 'orange')
    canvas.draw_text(("Score- "+str(wins-losses)),(480,80),25, 'Black')
    player_hand.draw(canvas, [50, 450])
    dealer_hand.draw(canvas, [50, 195])
    
    if in_play == True:
        canvas.draw_image(card_back, (CARD_BACK_CENTER), (CARD_BACK_SIZE), (50+CARD_BACK_SIZE[0]/2, 195+CARD_BACK_SIZE[1]/2), (CARD_SIZE), 0)
    if in_play == False:
        canvas.draw_text('Dealer hand = ' + str(dealer_hand.get_value()), [100, 350], 20, 'pink')        
        canvas.draw_text('Player hand = ' + str(player_hand.get_value()), [100, 400], 20, 'pink')
        

    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric