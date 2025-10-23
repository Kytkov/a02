"""Import objects."""

import player as player
import dice as dice
import Intelligence as intelligence
import Statistics as stats


class Game:
    """Handle game's running status."""

    def __init__(self):
        self.is_running = True
        self.player_has_current_hand = True
        self.score_collected_this_round = 0
        # all objects
        self.current_player = player.Player("")
        self.current_intelligence = (
            intelligence.Intelligence()
        )  # in constructor?
        self.current_dice = dice.Dice(6)
        self.stats = stats.Statistics()

    def player_turn(self):
        """Player's turn to play."""
        still_playing = True
        while still_playing:
            decision_after_roll_input = ""

            roll_input = input("Press R to roll dice\n")

            if roll_input.lower().strip() == "r":
                has_rolled = self.current_dice.roll()
                print("\nYou rolled " + str(has_rolled) + "!\n")

                self.stats.record_roll(has_rolled)

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
                    + " in this turn.\n"
                    + "CHOOSE:\nR: Roll another\nS: Stand and keep your score\n"
                )
            if decision_after_roll_input.lower().strip() == "s":
                    self.current_player.add_score(
                        self.score_collected_this_round
                    )
                    print(
                        "\nEnd of round! You earned "
                        + str(self.score_collected_this_round)
                        + " in this round. \tIn total you have " + str(self.current_player.get_score()) + "\n"
                        )
                    break
                   # still_playing = False

                # FIX ? : says "roll another" here then "roll" again on loop's start

    def computer_turn(self):
        """Computer's turn to play."""
        still_playing = True
        opponent_final_message = "Opponent has rolled "
        while still_playing:
            has_rolled = self.current_dice.roll()

            if self.is_round_over(has_rolled):
                print(opponent_final_message + "\nbut at last rolled a one and lost\n ")
                break

            self.score_collected_this_round += has_rolled
            opponent_final_message += str(has_rolled) + ", "
            # depending on difficulty, keep on playing depedning on score or stand
            
            
            should_stand = self.current_intelligence.make_choice(self.score_collected_this_round, 
                                                                 self.current_player.get_score())
            
            if should_stand:
                self.current_intelligence.add_score(self.score_collected_this_round)
                print("Opponent collected " + str(self.score_collected_this_round)
                      + "\t ..and has a total score of " + str(self.current_intelligence.get_score()) + "\n")
                #return
                break
        
        
        # depending on intelligence ..
        # call one of intelligence's methods depending on
        # chosen difficult level

    def is_round_over(self, roll):
        """Check if round is over."""
        return roll == 1

    def has_won(self, score):
        """check if game is won"""
        return score >=15
    
    def set_difficulty(self):
        """set current difficult for game"""
        difficulty_level = input(
                    "\nFinally, enter difficult level:\nE = EASY\nM = MEDIUM\nH = HARD\n"
                )
        if difficulty_level.upper() not in [
                    "E",
                    "M",
                    "H",
                ]:  # assign level automatically
                    difficulty_level = "E"
        self.current_intelligence.set_difficulty(difficulty_level)
    
    def reset_scores(self):
        """reset all player scores"""
        self.current_player.set_score(0)
        self.current_intelligence.set_score(0)

    def run(self):
        """Manage menu and handle both input and output"""
        MENU_OUTPUT = "Welcome to Pig Dice!\t\n1:New game\n"
        MENU_OUTPUT_GAME = "\nKeep playing?\n1: New round\n2: View stats\n3: Change difficulty\n4: Quit\n"
        MENU_INPUT: int
        game_over = False
        DICE_SIDES: int
        PLAYER_NAME = ""

        
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
                    print(
                        "[!] Your name needs to consist of atleast one character"
                    )

                self.set_difficulty()

                DICE_SIDES = int(input("Enter amount of dice sides: "))

                # use objects
                self.current_player = player.Player(PLAYER_NAME)
                self.current_dice = dice.Dice(DICE_SIDES)
                self.stats = stats.Statistics()

        while self.is_running:
                self.reset_scores()
              
                while not game_over:  # game loop
                    self.score_collected_this_round = 0

                # the variabels below are general for both player and opponent.
                # After every round, they are assigned those default values

                    if self.player_has_current_hand:
                        self.player_turn()
                    else:
                        self.computer_turn()

                    if self.has_won(self.current_player.get_score()):
                        print("\n😁👑Player won!\n")
                        self.stats.record_round(self.current_player.get_score())
                        break
                    if self.has_won(self.current_intelligence.get_score()):
                        print("\n🤖👑Opponent won!\n")
                        self.stats.record_round(self.current_player.get_score())
                        break
 
                    self.player_has_current_hand = (
                        not self.player_has_current_hand
                    )  # change turn
                    
                game_over = True
                try: 
                   
                    MENU_INPUT_GAME = int(input(MENU_OUTPUT_GAME))

                    if MENU_INPUT_GAME == 1:
                        print("\n* NEW ROUND *\n")
                        game_over = False

                    elif MENU_INPUT_GAME == 2:
                        print("\n" + self.stats.__str__())
                
                    elif MENU_INPUT_GAME == 3:
                        self.set_difficulty()
                
                    elif MENU_INPUT_GAME == 4:
                        self.is_running = False
                except ValueError:
                     print("Please input valid number")