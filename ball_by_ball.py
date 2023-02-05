import random

ball_possibilities = [0, 4, 6, "Wicket"]
wicket_possibilies = ["Bowled", "L.B.W.", "Caught"]

team1 = input("Team 1 Name: ")
team1_strengths = {"Batting Strength": input(f"Enter {team1} batting strength (1-5): "), 
                   "Bowling Strength": input(f"Enter {team1} bowling strength (1-3): ")
                   }

team2 = input("Team 2 Name: ")
team2_strengths = {"Batting Strength": input(f"Enter {team2} batting strength (1-5): "), 
                   "Bowling Strength": input(f"Enter {team2} bowling strength (1-3): ")
                   }

print(type(team1_strengths.get("Batting Strength")))

def first_innings():    
    team1_score = 0
    batsmen = 0
    ballcount = 0 
    while batsmen <4:
        input("Press enter to bowl: ")
        newball = random.choices(ball_possibilities, weights=(3,int(team1_strengths.get("Batting Strength")),1,int(team2_strengths.get("Bowling Strength"))))
        if newball[0] == "Wicket":
            wicket_type = random.choices(wicket_possibilies, weights=[5,6,7])
            print("GOT HIM!", wicket_type[0])
            batsmen = batsmen +1
            print(f"{team1_score}/{batsmen}")
            ballcount += 1
        else:
            print(newball[0]) 
            team1_score = team1_score + int(newball[0])
            ballcount += 1
            if ballcount % 6 == 0:
                print(f'At the end of the over the score is {team1_score}/{batsmen}.')
    return team1_score

def second_innings():
    team2_score = 0
    batsmen = 0
    ballcount = 0 
    while batsmen <4 and team2_score<team1_score:
        input("Press enter to bowl: ")
        newball = random.choices(ball_possibilities, weights=(3,int(team2_strengths.get("Batting Strength")),1,int(team1_strengths.get(("Bowling Strength")))))
        if newball[0] == "Wicket":
            wicket_type = random.choices(wicket_possibilies, weights=[5,6,7])
            print("GOT HIM!", wicket_type[0])
            batsmen = batsmen +1
            print(f"{team2_score}/{batsmen}")
            ballcount += 1
        else:
            print(newball[0]) 
            team2_score = team2_score + int(newball[0])
            ballcount += 1
            if ballcount % 6 == 0:
                print(f'At the end of the over the score is {team2_score}/{batsmen}.')
                print(f'Team 2 require {team1_score-team2_score+1} runs to win.')
    team2_remaining_batsmen = 4 - batsmen
    return team2_score, team2_remaining_batsmen

team1_score = first_innings()
team2_score = second_innings()
if team1_score > team2_score[0]: 
    print(f'{team1} won by {team1_score-team2_score[0]} runs.')
else:
    print(f'{team2} won by {team2_score[1]} wickets.')