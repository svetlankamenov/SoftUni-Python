from project.player import Player


class Team:
    def __init__(self, name:str, rating:int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player:Player):
        for added_player in self.__players:
            if added_player.name == player.name:
                return f"Player {added_player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name:str):
        for added_player in self.__players:
            if added_player.name == player_name:
                self.__players.remove(added_player)
                return added_player

        return f"Player {player_name} not found"