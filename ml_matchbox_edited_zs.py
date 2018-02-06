import random

print("THIS IS MATCH BOX ML DEMO")

# First Round
box1 = ["Rock"]*10 + ["Paper"]*10 + ["Scissors"]*10

# Second Round given First move
box2 = [box1] + [box1] + [box1]

# Third Round give First and Second move
box3 = [box2] + [box2] + [box2]

boxes = [box1] + [box2] + [box3]

# Function to check which input won
def checkIfWon(x,y):
    if (x.lower() == "rock" and y.lower() == "paper"):
        return False
    elif (x.lower() == "rock" and y.lower() == "scissors"):
        return True
    elif (x.lower() == "paper" and y.lower() == "scissors"):
        return False
    elif (x.lower() == "paper" and y.lower() == "rock"):
        return True
    elif (x.lower() == "scissors" and y.lower() == "rock"):
        return False
    elif (x.lower() == "scissors" and y.lower() == "paper"):
        return True

# Function to convert from index to label
# Rock index = 0, Paper index = 1, Scissors index = 2
def convert2label(x):
    if (x == 0):
          out = "rock"
    elif (x == 1):
          out = "paper"
    else:
          out = "scissors"
    return out

def gameon(p_wins, r_wins, round_num, p_answer, r_answer):
    repatedTimes = 0;
    ranswer = 0;
    while (p_answer.lower() == r_answer.lower()):
        print("\n\nRound {0} \n".format(round_num))
        print('You had a Draw! Replay the Round! \n' if repatedTimes > 0 else '')
        p_answer = input("Rock, Paper, or Scissors: ")
        if(round_num == 1):
            r_answer = boxes[round_num-1].pop(random.randrange(0,len(boxes[round_num-1])))
        elif(round_num == 2):
            r_answer = boxes[round_num-1][int(r_answers[0])].pop(random.randrange(0,len(boxes[round_num-1][int(r_answers[0])])))
        elif(round_num == 3):
            r_answer = boxes[round_num-1][int(r_answers[0])][int(r_answers[1])].pop(random.randrange(0,len(boxes[round_num-1][int(r_answers[0])][int(r_answers[1])])))
        print("\n||| COMPUTER THREW " + r_answer + " |||")
        repatedTimes+=1

    if (checkIfWon(p_answer,r_answer)):
        print("\n-> You Won!")
        p_wins = p_wins + 1
    else:
        print("\n-> You Lost!")
        r_wins = r_wins + 1

    if (r_answer.lower() == "rock"):
        ranswer= 0
    elif (r_answer.lower() == "paper"):
        ranswer = 1
    elif (r_answer.lower() == "scissors"):
        ranswer = 2
    return [p_wins, r_wins, ranswer]

# Number of games played
EPOCHS = 10

for epoch in range(EPOCHS):
    # Current Round
    rounds = 0
    # Current Number of User Wins
    p_wins = 0
    # Current Number of Computer Wins
    r_wins = 0

    # Save spots for answers
    p_answer = ""
    r_answer = ""
    r_answers = ["","",""]

    while(p_wins < 2 and r_wins < 2):
        rounds = rounds + 1
        p_answer = ""
        r_answer = ""

        # Plays Round 1, Round 2, and Round 3
        if (rounds == 1):
            [p_wins, r_wins, r_answers[0]] = gameon(p_wins, r_wins, 1, p_answer, r_answer)
        elif (rounds == 2):
            [p_wins, r_wins, r_answers[1]] = gameon(p_wins, r_wins, 2, p_answer, r_answer)
        elif (rounds == 3):
            [p_wins, r_wins, r_answers[2]] = gameon(p_wins, r_wins, 3, p_answer, r_answer)

    if(p_wins > r_wins):
        print("==================\n")
        print("Trial " + str(epoch))
        print("\n==================")
        print("\n\nYou Won The Game!")
        print(str(p_wins) + "-" + str(r_wins))
    else:
        print("==================\n")
        print("\nTrial " + str(epoch))
        print("\n==================\n")
        print("\n\nComputer Won The Game!")
        print(str(p_wins) + "-" + str(r_wins))
        # Adds winning answers to box
        for i in range(5):
            boxes[0].append(convert2label(r_answers[0]))
        for i in range(5):
            boxes[1][int(r_answers[0])].append(convert2label(r_answers[1]))
        for i in range(5):
            boxes[2][int(r_answers[0])][int(r_answers[1])].append(convert2label(r_answers[2]))
