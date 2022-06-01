competitions = [
    ["HTML","C#"],
    ["C#", "Python"],
    ["Python","HTML"]
]
results = [0,0,1]

'''
O(n) time | O(k) space
n is the number of competitions and k is the number of teams
'''
def tournamentWinner(competitions, results):
    homeTeamWon = 1
    bestTeam = ''
    score={bestTeam:0}

    for idx, comp in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = comp
        
        winningTeam = homeTeam if result == homeTeamWon else awayTeam

        updateScores(winningTeam,3,score)
        
        if score[winningTeam] > score[bestTeam]:
            bestTeam = winningTeam

    return bestTeam



def updateScores(team, points, score):
    if team not in score:
        score[team] = 0

    score[team] +=points  





