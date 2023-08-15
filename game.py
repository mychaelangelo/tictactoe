from board import Board

board = Board()
print("\nWelcome to tic-tac-toe.\n\n")
board.show_grid()

p1 = board.player_1
p2 = board.player_2

def make_move(player):
    print(f"\n{player.name}, please enter your move in x, y coords:")
    try:
        move_x = int(input("Enter the x coordiante: "))
        move_y = int(input("Enter the y coordiante: "))
        board.play(player, move_x, move_y)
        board.show_grid()
    except Exception as e:
        print(f"Error: {str(e)}")
        make_move(player)

while True:
        # P1
        make_move(p1)
        if board.check_winner():
            print(f"{p1.name} won!")
            break
        elif board.is_a_draw():
            print("It's a draw!")
            break

        # P2
        make_move(p2)
        if board.check_winner():
            print(f"{p2.name} won!")
            break   
        elif board.is_a_draw():
            print("It's a draw!")   
            break  




