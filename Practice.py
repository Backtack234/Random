class Match:
    def __init__(self, Team_1, Team_2):
        self.Team_1 = Team_1
        self.Team_2 = Team_2
p1 = Match(3, 3)

Best_of_9 = range(1, 10)

for score in Best_of_9:
    if p1.Team_1 < 5 and p1.Team_2 < 5:
        if p1.Team_1 + score == 5:
            print(f'Team 1 will win in {score} games')
        if p1.Team_2 + score == 5:
            print(F'Team 2 will win in {score} games')
    else:
        print("Error! Try again")
