from SevenWonders.conquest_score import *
from SevenWonders.money_score import *
from SevenWonders.wonders_score import *
from SevenWonders.civilian_score import *
from SevenWonders.market_score import *
from SevenWonders.guild_score import *
from SevenWonders.science_score import *


class TestMain:
    def __init__(self):
        print("Hello")
    def say_something(self):
        print("Say something")


conquest = ConquestScore()
money = MoneyScore()
wonders = WondersScore()
civilian = CivilianScore()
market = MarketScore()
guild = GuildScore()
science = ScienceScore()


def add_name(dict, name):
    if name not in dict:
        dict[name] = 0
        print("Adding new player: " + name)
    else:
        print("Player already added.")
    return dict


def add_score(player_dict, name):
    total_points = 0
    score_finished = False;
    while not score_finished:
        score_command = input("What would you like to try to add?\n "
                              "[C]onquest, [M]oney, [W]onders, Ci[v]ilian, Mar[k]ets, [G]uilds, [S]ciences [Q]uit: ")\
                             .upper()
        if score_command == 'Q':
            score_finished = True
        elif score_command == 'C':
            total_points = total_points + conquest.conquest_score_total()
        elif score_command == 'M':
            total_points = total_points + money.money_score_total()
        elif score_command == 'W':
            total_points = total_points + wonders.wonders_score_total()
        elif score_command == 'V':
            total_points = total_points + civilian.civilian_score_total()
        elif score_command == 'K':
            total_points = total_points + market.market_score_total()
        elif score_command == 'G':
            total_points = total_points + guild.guild_score_total()
        elif score_command == 'S':
            total_points = total_points + science.science_score_total()
    print("Total Points: " + str(total_points))
    player_dict[name] = total_points
    return player_dict


if __name__ == '__main__':
    finish = False
    player_dict = {}
    while not finish:
        command = input("What would you want to do? (Add [N]ame, [A]dd score, [P]rint players, [Q]uit): ")
        if command.upper() == 'N':
            name = input("Enter the name of the player: ").upper()
            add_name(player_dict, name)
            print(player_dict)
        elif command.upper() == 'A':
            name = input("Enter name of player you want to add score for: ").upper()
            if name not in player_dict:
                print("Player not found. Please select a new option.")
            else:
                add_score(player_dict, name)
        elif command.upper() == 'Q':
            finish = True
        elif command.upper() == 'P':
            print(player_dict)
        else:
            print("I'm not sure what you want to do. Try again.")

