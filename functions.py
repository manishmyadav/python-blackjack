

#Draw random card function
def draw_card(cards):
    import random
    card = random.choice(cards)
    return card

#Ensures that first 2 cards drawn each player aren't a winning combination
def draw_two_cards(cards): 
    while True:
        card1 = draw_card(cards)
        card2 = draw_card(cards)
        sum_of_cards = card1 + card2
        if sum_of_cards != 21:
            break
    two_cards = []
    two_cards.append(card1)
    two_cards.append(card2)
    return two_cards
    

#Calculate scores based on cards list
def score(cards_list):
    score = sum(cards_list)
    return score

#Displays all user cards
def display_user_cards(user_cards_list):
    print("Your cards:", user_cards_list)
    
#Display all computers cards
def display_computer_cards(computer_cards_list):
    print("Computer cards:", computer_cards_list)
    
def print_winner(user_cards_list, computer_cards_list):
    user_score = score(user_cards_list)
    computer_score = score(computer_cards_list)
    print("Your Score:", user_score)
    print("Computer's Score:", computer_score)
    if user_score > computer_score:
        print("You Win")
    elif user_score < computer_score:
        print("Computer Win")
    else:
        print("Draw")
        
def computer_bust(computer_cards_list):
    print("Computer BUST!")
    print("Computer passes over 21! ")
    print("Computer's cards:", computer_cards_list)
    computer_score = score(computer_cards_list)
    print("Computer's score:", computer_score)
    print("You win!")
    
    
def computer_stands(user_cards_list, computer_cards_list):
    print("Your Cards:", user_cards_list)
    print("Computer's Cards:", computer_cards_list)
    print_winner(user_cards_list, computer_cards_list)

def user_bust(user_cards_list):
    print("BUST!")
    print("You pass over 21!")
    print("Your cards:", user_cards_list)
    user_score = score(user_cards_list)
    print("Your Score:", user_score)
    print("You LOSE!")
    
    






































































