from player import Player

class Board:
    """A class for a tic tac toe board"""
    
    def __init__(self, row_num=3):
        """init and set the size of the board, must be square"""
        self.row_num = row_num
        self.col_num = row_num

        # set players
        self.player_1 = Player('X', "Player 1")
        self.player_2 = Player('O', "Player 2")

        # Set inital board to blank cells
        self.set_board()

        # Set list of moves 
        self.moves = []

        # Set win status to False
        self.game_won = False

    def set_board(self):
        """Set a blank board"""
        self.grid = []

        # Fill the grid with '_'s
        for curr_row in range(self.row_num):
            # each row starts blank
            new_row = []
            # iterate on curr_row across columns
            for curr_col in range(self.col_num):
                new_row.append('_')
            self.grid.append(new_row)
    
    def show_grid(self):
        """Show state of board"""
        for i in self.grid:
            print(i)

    def play(self, curr_player, x_position, y_position):
        """Play a player at specific position."""

        # check if move is in range
        if self._out_of_range(x_position, y_position):
            raise Exception("Move is out of range. Please try again.")
        else:
        # put move in a tuple
            new_move = (x_position, y_position)
        
        # if new move isn't in history of moves, play it
        if new_move not in self.moves:
            print(f"{curr_player.name} is playing a move at {x_position} and {y_position}\n")
            self.grid[x_position][y_position] = curr_player.mark
            self.moves.append(new_move)
        else:
            raise Exception("The move has already been played. Please try again.")
 
    def _is_empty_cell(self, x_position, y_position):
        return self.grid[x_position][y_position] == '_'
    
    def _out_of_range(self, x_position, y_position):
        return (x_position > (self.row_num - 1)) or (y_position > (self.col_num - 1))
    
    def _check_rows_win(self, player_marker):
        """Check if any of the rows have a match"""
        row_match = False
        for curr_row in range(self.row_num):
            for curr_col in range(self.col_num):
                if self.grid[curr_row][curr_col] == player_marker:
                    row_match = True
                else:
                    row_match = False
                    break
            if row_match == True:
                break
        return row_match
    
    def _check_cols_win(self, player_marker):
        """Check if any of the columns have a match"""
        col_match = False
        for curr_col in range(self.col_num):
            for curr_row in range(self.row_num):
                if self.grid[curr_row][curr_col] == player_marker:
                    row_match = True
                else:
                    row_match = False
                    break
            if row_match == True:
                break
        return row_match
    
    def _check_diag_win(self, player_marker):
        """Check if any of the diagnoals have a match"""
        diag_match = False

        # Check top-left to bottom-right
        pointer = 0
        while pointer < self.row_num:
            if self.grid[pointer][pointer] == player_marker:
                diag_match = True
                pointer += 1
            else:
                diag_match = False
                break

        if diag_match: # if matching top-left to bottom-right, return true
            return diag_match
        else: 
        # check top-right to bottom-left
            row_pos = 0
            col_pos = self.col_num - 1
            while col_pos >= 0:
                if self.grid[row_pos][col_pos] == player_marker:
                    diag_match = True
                    row_pos += 1
                    col_pos -= 1
                else:
                    diag_match = False
                    break
            return diag_match

    def check_winner(self):
        """Returns winning player or None if there's no winner"""
        players = [self.player_1, self.player_2] 
        winner = None
        
        for player in players:
            row_win_check = self._check_rows_win(player.mark)
            col_win_check = self._check_cols_win(player.mark)
            diag_win_check = self._check_diag_win(player.mark)

            if row_win_check or col_win_check or diag_win_check:
                #print(f"Winner is {player.name}")
                winner = player
                self.game_won = True
                break
            else:
                continue
        
        if winner:
            #print(f"Game won status: {self.game_won}")
            return winner
        else:
            #print(f"Game won status: {self.game_won}")
            return None
            
    def is_a_draw(self):
        status = False
        if self.check_winner() == None:
            for row in self.grid:
                if '_' in row:
                    return False
                else:
                    status = True
            return status
        else:
            return False




  
my_board = Board()
my_board.grid = [
    ['O','X','X'], 
    ['X','X','O'], 
    ['X','O','X']
    ]

print(my_board.is_a_draw())




    






                



        