team_1=96
team_2=92
team_3=99
team_4=91
team_5=95

Total=team_1+team_2+team_3+team_4+team_5
Average=Total / 5
print("Total:",Total)
print("Average:",Average)

Stars_Per_Point=5
Reward=Total * Stars_Per_Point
print("Reward:",Reward)

Boxes=Reward // 25
print("Boxes needed:",Boxes)
Remaining_Reward=Reward % 25
print("Remaining reward:",Remaining_Reward)

Last_Week=300
print("Is it  greater than last week?",Total > Last_Week)
print("Is it same to last week?",Total == Last_Week)
print("Is it at least same or greater?",Total >= Last_Week)

Total += 27
print("Total with bonus points:",Total)

Total -= 5
print("Total after minus points:",Total)