from card_game import *
from text_color import *

'''''
Game will start if the user/player activated the game through main_cards.py

test_the_card = draw_cards(partial_deck_drawn)
print('You have draw a :', test_the_card.card_value,test_the_card.card_suit)
'''''

player0_card = []
player1_card = []

# Deal x amount of players for deal of war gameplay
def deal_war():
    while(len(partial_deck_drawn) > 0):
        player0_card.append(draw_cards(partial_deck_drawn))
        player1_card.append(draw_cards(partial_deck_drawn))
deal_war()


# Now to let the game compare each player's card
# & check for info
count_player0 = 0
count_player1 = 0

def space():
    print('\n')
def line_space():
    print('------- ------- ------- -------')

for index in range(0,len(player0_card)):
    if (player0_card[index].card_value > player1_card[index].card_value):
        count_player0 += 1
        print(player0_color +'Player 0' + end + win_score + ' wins' + end +' the hand with: ' + card_color , player0_card[index].card_value)
        print(player1_color +'Player 1' + end + lose_score + ' loses' + end + ' with card: ' + card_color , player1_card[index].card_value)
        print(player0_color +'Player 0' + end + total_score +' Total Score: ' + end + str(count_player0))
        space()
        line_space()
    if (player0_card[index].card_value < player1_card[index].card_value):
        count_player1 += 1
        print(player1_color + 'Player 1' + end + win_score + ' wins' + end + ' the hand with: ' + card_color , player1_card[index].card_value)
        print(player0_color +'Player 0 ' + end +  lose_score + 'loses' + end + ' with card: ' + card_color , player0_card[index].card_value)
        print(player1_color + 'Player 1 ' + end + total_score + 'Total Score: ' + end + str(count_player1))
        space()
        line_space()
    else:
        print(war_color +'War! Both Player\'s take losses!!' + end)
        count_player0 -= 1
        count_player1 -= 1
        space()
        print(player0_color +'Player0\'s Score: ' + total_score + str(count_player0))
        print(player1_color + 'Player1\'s Score: ' + total_score + str(count_player1))
        space()

    player_0_win_margin = count_player0 - count_player1
    player_1_win_margin = count_player1 - count_player0
    if count_player0 > count_player1:
        print(player0_color +'Player0\'s wins by a margin of ' + war_player_score + str(player_0_win_margin))
        print(player0_color +'Player0\'s orignal score was: ' + war_player_score +  str(count_player0))
        print(player1_color + 'Player1\'s orignal score was: ' + war_player_score + str(count_player1))
        print(winner_text + '---------- ---------- ---------- WINNER' + player0_color + ' Player0 '
                          + end + winner_text + '---------- ---------- ----------')
    elif count_player1 > count_player0:
        print(player1_color +'Player\'s 1 wins by a margin of ' + war_player_score +  str(player_1_win_margin))
        print(player1_color +'Player1\'s orignal score was: ' + war_player_score + str(count_player1))
        print(player0_color +'Player0\'s orignal score was: ' + war_player_score + str(count_player0))
        print(winner_text +'---------- ---------- ---------- WINNER' + player1_color + ' Player1 '
              + end + winner_text + '---------- ---------- ----------')
    else:
        print(game_over + 'Both players lose!!' + end)
        print(player0_color + 'Player0 Score: ' + war_player_score + str(count_player0))
        print(player1_color + 'Player1 Score: ' + war_player_score + str(count_player1))
        print(game_over + '---------- ---------- ---------- GAME OVER- NOBODY WINS ---------- ---------- ----------')