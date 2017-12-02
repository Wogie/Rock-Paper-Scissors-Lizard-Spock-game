# Defining score variables
# Round counter
count = 0
# The score needed to win
score_to_win = 0
# Player 1 score
score1 = 0
# Player 2 score
score2 = 0


def clearfunc():
    """This functions clears the screen"""
    clear = "\n" * 50
    print(clear)


def rules():
    """This function explains the rules when called"""
    clearfunc()

    print('''Anecdotal evidence suggests that in a
    \rgame of Rock Paper Scissors players that are
    \rfamiliar with each other will tie 75 to 80
    \rpercent of the time do to the limited number
    \rof outcomes.''')
    input()
    print('''For this reason Rock, Paper, Scissors,
    \rLizard, Spock was invented.''')
    input()
    print('''With 5 options there are 25 different outcomes
    \rof which only 5 are ties''')
    input()
    print("The rules are as follows:")
    input()
    print("Scissors cuts Paper")
    input()
    print("Paper covers Rock")
    input()
    print("Rock crushes Lizard")
    input()
    print("Lizard poisons Spock")
    input()
    print("Spock smashes Scissors")
    input()
    print("Scissors decapitates Lizard")
    input()
    print("Lizard eats Paper")
    input()
    print("Paper disproves Spock")
    input()
    print("Spock vaporizes Rock")
    input()
    print("(and as it always has) Rock crushes Scissors")
    input()
    clearfunc()


def rules_question():
    """This function loops if question is not answered with yes or no.
    Calls rule function when answer is no"""
    rule_answer = input("(y/n) > ")

    if rule_answer == 'y' or rule_answer == "yes":
        clearfunc()
    elif rule_answer == 'n' or rule_answer == "no":
        rules()
    else:
        rules_question()


def play_again_question():
    """This function loops if answer is neither yes nor no.
    adds 1 to round counter if yes, else exits
    """
    global count
    print("Play again?")
    play_again_answer = input("(y/n) > ")

    if play_again_answer == "y":
        count += 1
        game()
        exit(1)
    elif play_again_answer == "n":
        clearfunc()
        print("Bye!")
        exit(0)
    else:
        play_again_question()


def game():
    """The game itself"""
    global count, score_to_win, score1, score2

    if count == 0:

        clearfunc()
        print('''
        \rWelcome to Rock, Paper, Scissors, Lizard, Spock!\n
        \rThis is a game originally invented by Sheldon Cooper.
        \r.. And now recreated as a textformat game by L.B. Rasmussen.\n
        \rAre you familiar with the rules?''')

        rules_question()

        # Loops until a valid answer is given
        invalid_answer = True
        while invalid_answer:
            clearfunc()
            print('''Do you want the game to end after
            \ra certain score is reached?\n''')
            point_ques1 = input("(y/n) > ")
            if point_ques1 == "y" or point_ques1 == "yes" or (
                            point_ques1 == "n" or point_ques1 == "no"):
                invalid_answer = False

        # Loops until a valid answer is given
        invalid_answer = True
        while invalid_answer:
            if point_ques1 == "y" or point_ques1 == "yes":
                print("\nHow many points are needed to win?")
                point_ques2 = input("(1-5) > ")

                if point_ques2.isdigit():
                    point_ques2 = int(point_ques2)
                    if 0 < point_ques2 <= 5:
                        invalid_answer = False
                        score_to_win = point_ques2
                    else:
                        print('''\nSorry. I didn't understand that.
                        \rPlease try again''')
                else:
                    print("\nSorry. I didn't understand that.\nPlease try again")

            elif point_ques1 == "n" or point_ques1 == "no":
                invalid_answer = False
                clearfunc()
            else:
                print("error")
                exit()

        clearfunc()
        print("Great. Let's get started\n")

    else:
        clearfunc()

        if score_to_win > 0:
            print("Score to win: %d" % score_to_win)

        print("Player one score: %d" % score1)
        print("Player two score: %d\n" % score2)

    p1p = input("Player one pick:\n> ")
    clearfunc()
    p2p = input("Player two pick:\n> ")
    clearfunc()

    # Transforming answers to single-letter
    rocklist = ['r', 'R', 'rock', 'Rock']
    paperlist = ['p', 'P', 'paper', 'Paper']
    scissorslist = ['s', 'S', 'scissors', 'Scissors']
    lizardlist = ['l', 'L', 'lizard', 'Lizard']
    spocklist = ['sp', 'Sp', 'spock', 'Spock']

    if p1p in rocklist:
        p1p = rocklist[3]
    elif p1p in paperlist:
        p1p = paperlist[3]
    elif p1p in scissorslist:
        p1p = scissorslist[3]
    elif p1p in lizardlist:
        p1p = lizardlist[3]
    elif p1p in spocklist:
        p1p = spocklist[3]
    else:
        print("Player one didn't choose a valid option")
        count += 1
        input()
        game()
        exit(1)

    if p2p in rocklist:
        p2p = rocklist[3]
    elif p2p in paperlist:
        p2p = paperlist[3]
    elif p2p in scissorslist:
        p2p = scissorslist[3]
    elif p2p in lizardlist:
        p2p = lizardlist[3]
    elif p2p in spocklist:
        p2p = spocklist[3]
    else:
        print("Player two didn't choose a valid option")
        count += 1
        input()
        game()
        exit(1)

    # Matchup texts
    pr = "Paper covers Rock"
    rs = "Rock crushes Scissors"
    rl = "Rock crushes Lizard"
    spr = "Spock vaporizes Rock"
    sp = "Scissors cuts Paper"
    lp = "Lizard eats Paper"
    psp = "Paper disproves Spock"
    sl = "Scissors decapitates Lizard"
    sps = "Spock smashes Scissors"
    lsp = "Lizard poisons Spock"

    p1_wins = False
    p2_wins = False

    # The 15 matchups and 25 results
    if (p1p in rocklist or p2p in rocklist) and not (
                    p1p in rocklist and p2p in rocklist):  # One and only one is Rock

        if p1p in paperlist or p2p in paperlist:
            print(pr)

            if p1p in paperlist:
                p1_wins = True
            elif p2p in paperlist:
                p2_wins = True

        elif p1p in scissorslist or p2p in scissorslist:
            print(rs)

            if p1p in rocklist:
                p1_wins = True
            elif p2p in rocklist:
                p2_wins = True

        elif p1p in lizardlist or p2p in lizardlist:
            print(rl)

            if p1p in rocklist:
                p1_wins = True
            elif p2p in rocklist:
                p2_wins = True

        elif p1p in spocklist or p2p in spocklist:
            print(spr)

            if p1p in spocklist:
                p1_wins = True
            elif p2p in spocklist:
                p2_wins = True

        else:
            print("Doesn't work 222")

    elif (p1p in paperlist or p2p in paperlist) and not (
                    p1p in paperlist and p2p in paperlist):  # One and only one is Paper

        if p1p in scissorslist or p2p in scissorslist:
            print(sp)

            if p1p in scissorslist:
                p1_wins = True
            if p2p in scissorslist:
                p2_wins = True

        if p1p in lizardlist or p2p in lizardlist:
            print(lp)

            if p1p in lizardlist:
                p1_wins = True
            if p2p in lizardlist:
                p2_wins = True

        if p1p in spocklist or p2p in spocklist:
            print(psp)

            if p1p in paperlist:
                p1_wins = True
            if p2p in paperlist:
                p2_wins = True

    elif (p1p in scissorslist or p2p in scissorslist) and not (
                    p1p in scissorslist and p2p in scissorslist):  # One and only one is Scissors

        if p1p in lizardlist or p2p in lizardlist:
            print(sl)

            if p1p in scissorslist:
                p1_wins = True
            if p2p in scissorslist:
                p2_wins = True

        if p1p in spocklist or p2p in spocklist:
            print(sps)

            if p1p in spocklist:
                p1_wins = True
            if p2p in spocklist:
                p2_wins = True

    elif (p1p in lizardlist or p2p in lizardlist) and not (
                    p1p in lizardlist and p2p in lizardlist):  # One and only one is Lizard
        print(lsp)

        if p1p in lizardlist:
            p1_wins = True
        elif p2p in lizardlist:
            p2_wins = True

    elif p1p == p2p:
        print("You both chose %s. It's a tie" % p1p)

    else:
        print("Error")
        exit()

    # Finding round winner
    if p1_wins:
        score1 += 1
        print("\nPlayer 1 wins!\n")
        input(">")
    elif p2_wins:
        score2 += 1
        print("\nPlayer 2 wins!\n")
        input(">")

    # Checking if score to win is reached
    if (score1 == score_to_win or score2 == score_to_win) and score_to_win > 0:
        clearfunc()
        if score1 > score2:
            print('''Congratulations to Player 1!!
            \rYou were the first to reach a score of %d''' % score_to_win)
            input(">")
            print("Game over")
            input(">")
            score1 = 0
        elif score2 > score1:
            print('''Congratulations to Player 2!!
            \rYou were the first to reach a score of %d''' % score_to_win)
            input(">")
            print("Game over")
            input(">")
            score2 = 0

    play_again_question()


game()
