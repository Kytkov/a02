"""import objects"""
import player as player
import dice as dice
import Intelligence as intelligence
import Statistics as stats



class Game:
    """Handle game's running status"""

    def __init__(self):
        self.is_running = True
        self.player_has_current_hand = True
        self.score_collected_this_round = 0
         # all objects
        self.current_player = player.Player()
        self.current_intelligence = (
                    intelligence.Intelligence()
                )  # in constructor?
        self.current_dice = dice.Dice()
        self.stats = stats.Statistics()

    def player_turn(self):
        """player's turn to play"""
        still_playing = True
        while still_playing:
            decision_after_roll_input = ""

            roll_input = input("Press R to roll dice")

            if roll_input.lower().strip() == "r":
                has_rolled = self.current_dice.roll()
                print("You rolled " + str(has_rolled) + "!")

            if self.is_round_over(has_rolled):
                print("woops, you rolled a one and lost your turn!")
                break

            self.score_collected_this_round += has_rolled

            while (
                len(decision_after_roll_input) == 0
            ):  # for safety; player may accidentaly send nothing as input
                decision_after_roll_input = input(
                    "You have gained "
                    + str(self.score_collected_this_round)
                    + " in this round.\n"
                    + "CHOOSE:\nR: Roll another\nS: Stand and keep your score\n"
                )
                if decision_after_roll_input.lower().strip() == "s":
                    self.current_player.add_score(self.score_collected_this_round)
                    print(
                        "\nEnd of round! You earned "
                        + str(self.score_collected_this_round)
                        + " in this round."
                    )
                    still_playing = False

                # FIX ? : says "roll another" here then "roll" again on loop's start

    def computer_turn(self):
        """computer's turn to play"""

        still_playing = True
        while still_playing:
            has_rolled = self.current_dice.roll()

            if self.is_round_over(has_rolled):
                break

            self.score_collected_this_round += has_rolled

            # depending on difficulty, keep on playing depedning on score or stand
            
            
            should_stand = self.current_intelligence.make_choice(self.score_collected_this_round, 
                                                                 self.current_player.get_score())
            if should_stand:
                print("Opponent has collected " + str(self.score_collected_this_round))
                self.current_intelligence.add_score(self.score_collected_this_round)
                break
        
        print("Opponent rolled a one and lost")
        # depending on intelligence ..
        # call one of intelligence's methods depending on
        # chosen difficult level
        

    def is_round_over(self, roll):
        """check if round is over"""
        return roll == 1

    def has_won(self, score):
        """check if game is won"""
        return score >= 100

    def run(self):
        """Manage menu and handle both input and output"""
        MENU_OUTPUT = "Welcome to Pig Dice!\t\n1:New game\n2: View stats"
        MENU_INPUT: int
        game_over = False
        DICE_SIDES: int
        PLAYER_NAME = ""
        difficulty_level: str

        while self.is_running:
            game_over = False

            try:
                MENU_INPUT = int(input(MENU_OUTPUT))

            except ValueError:
                has_recovered_from_err = False
                for i in range(
                    len(MENU_INPUT)
                ):  # potential spelling error with integers in the input..
                    # ..check for first integer.
                    try:
                        int(i)
                        has_recovered_from_err = True
                        break
                    except ValueError:
                        continue
                if not has_recovered_from_err:
                    print("[!] Please chooce correct menu option")

        if MENU_INPUT == 1:
            
                while len(PLAYER_NAME) == 0:  # only assign name once
                    PLAYER_NAME = input("Enter your name: ")
                    if len(PLAYER_NAME) == 0:
                        print("[!] Your name needs to consist of atleast one character")

                # choose sides for dice
                try:
                    DICE_SIDES = int(input("Enter amount of sides for the dice:"))
                except ValueError:
                    print("[!] Did not get valid number.\nSides for dice:\t6")
                    DICE_SIDES = 6

                difficulty_level = input(
                    "Finally, enter difficult level:\nE = EASY\nM = MEDIUM\nH = HARD"
                )
                if difficulty_level not in [
                    "E",
                    "M",
                    "H",
                ]:  # assign level automatically
                    difficulty_level = "E"

                # use objects
                self.current_player = player.player(PLAYER_NAME)
                self.current_dice = dice.Dice(DICE_SIDES)
                self.stats = stats.Statistics()
                self.current_intelligence = intelligence.Intelligence()

                self.current_intelligence.set_difficulty(difficulty_level)
               

                while not game_over:  # game loop

                    # the variabels below are general for both player and opponent.
                    # After every round, they are assigned those default values

                    self.score_collected_this_round = 0

                    if self.has_won(self.current_player.get_score()):
                        print("player won")
                        break
                    if self.has_won(self.current_intelligence.get_score()):
                        print("opponent won!")
                        break

                    if (
                        self.player_has_current_hand
                    ):  # if the player is the current one playing
                        self.player_turn()

                    else:
                        self.computer_turn()

                    self.player_has_current_hand = (
                        not self.player_has_current_hand
                    )  # change turn
        elif MENU_INPUT == 2:
            print("--STATS--")
            
            



# if __name__ == '__main__':
#     g = Game()
#     g.run()
