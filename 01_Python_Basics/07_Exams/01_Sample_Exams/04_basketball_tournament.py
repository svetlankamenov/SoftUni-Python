games_count = 0
total_games = 0
host_points = 0
rival_points = 0
wins = 0
losses = 0

while True:
    tournament = input()
    if not tournament == "End of tournaments":
        #Статистика на турнирите
        #Брой на мачовете
        games_count = int(input())
        total_games += games_count
        #За всеки мач прочитане на резултатите
        for i in range(games_count):
            host_points = int(input())
            rival_points = int(input())

            #Победа
            if host_points > rival_points:
                wins += 1
                print(f"Game {i+1} of tournament {tournament}: win with {abs(host_points-rival_points)} points.")
            #Загуба
            elif host_points < rival_points:
                losses += 1
                print(f"Game {i+1} of tournament {tournament}: lost with {abs(host_points-rival_points)} points.")

    else:
        #Изход от цикъла при End of tournaments
        print(f"{(wins/total_games*100):.2f}% matches win")
        print(f"{(losses/total_games*100):.2f}% matches lost")
        break