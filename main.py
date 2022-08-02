import functions

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]        
user_cards_list = []
computer_cards_list = []
user_score = 0
computer_score = 0

def main():
    from art import logo
    play_another_game = True
    #New Game 
    start = input("Press enter to start: ")
    while play_another_game == True:
        print(logo)
        print("Welcome to Blackjack 21!")
        initialize()
        blackjack()
        choice = input("Do you wanna play again? \'y\' or \'n\': ")
        if choice == 'y':
            play_another_game = True
        elif choice == 'n':
            play_another_game = False
        else:
            # User entered an invalid choice so continue
            pass
    return
        
def blackjack():   
    while True:
        print("Shuffling......")
        draw_cards = input("Press enter to draw your initial 2 cards...")
        user_cards_list = functions.draw_two_cards(cards)
        computer_cards_list = functions.draw_two_cards(cards)
        functions.display_user_cards(user_cards_list)
        computer_first_card = computer_cards_list[0]
        print(f"Computer\'s cards: [{computer_first_card}, X]")
        user_choice = input("STAND or HIT?: ").lower()
        
        if user_choice == 'stand':
            user_score = functions.score(user_cards_list)
            while True:
                computer_score = functions.score(computer_cards_list)
                if computer_score > 21:
                    functions.computer_bust(computer_cards_list)
                    break
                elif computer_score >= 17:
                    #Computer STANDS
                    functions.computer_stands(user_cards_list, computer_cards_list)
                    break
                else: 
                    #Computer HITS
                    new_card = functions.draw_card(cards)
                    computer_cards_list.append(new_card)
            print("GAME OVER")
            break
                
        elif user_choice == 'hit':
            new_card = functions.draw_card(cards)
            user_cards_list.append(new_card)
            user_score = functions.score(user_cards_list)
            if user_score > 21:
                functions.user_bust(user_cards_list)
                print("GAME OVER")
                break
        else:
            #Continue as the user entered an invalid choice
            pass
    return #End of 1 blackjack game

def initialize():
    global user_cards_list
    user_cards_list = []
    global computer_cards_list
    computer_cards_list = []
    return

# Calling main() at last to follow python program flow
main()
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

