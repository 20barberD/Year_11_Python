#Task 5
def countScores(scores):
    teams = []
    teamScores = []
    for teamScore in scores:
        team = teamScore[0]
        score = teamScore[1]
        if team not in teams:
            teams.append(team)
            teamScores.append([team, score])
        else:
            for i in range(0, len(teamScores)-1):
                if teamScores[i][0] == team:
                    teamScores[i][1] += score
    return teamScores

player = [
    [1, 45],
    [2, 30],
    [2, 46],
    [1, 31],
    [1, 10],
    [1, 32],
    [2, 2]
]
countedScores = countScores(player)
teamNames = ["Green", "Red"]
for teamScore in countedScores:
    print(f"{teamNames[teamScore[0]-1]} Team got {teamScore[1]} points in total! ")