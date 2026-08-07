import random #
import sys
import time
import all_pokemon_list
import msvcrt
import threading
from type_chart_factor import type_bonus_dict
from attack_dict import attack_dict
from all_pokemon_list import Arceus
from all_pokemon_list import Pikachu
from all_pokemon_list import Meowth
from all_pokemon_list import LC_Poke
from all_pokemon_list import NU_Poke
from all_pokemon_list import OU_Poke
from all_pokemon_list import Uber_Poke
from achievements import achv_dict
from dialogues import landed_evil
from dialogues import land_safe
from dialogues import villain_intro
from dialogues import wdyw_line
from dialogues import battle_intro_line
from dialogues import poker_intro_line
from dialogues import roulette_intro_line
from dialogues import invalid_selection_line
from dialogues import leave_chat_line
# FLIGHT FUNCTION IMPORTS
from free_flight import free_flight
from used_functions import current_location, calculate_coordinates, play_ping, play_sound
import random
from data_function import villain_gen
from used_functions import type_with_cursor
from used_functions import store_data
from used_functions import radar
from used_functions import blip_line
# Duy's Animation
from Intro import intro
from Fly import animation_flying
from loading import loading_ani
from Fly import animation_landing
from airport import airport_ani
from win import ani_win1
from gameover import gameover




class Human:
    def __init__(self, name: str, rank: str):
        self.name = name
        self.rank = rank
        self.health = 300
        self.max_health = 300
        self.fuel = 100
        self.location = ["60.3179° N", "24.9496° E"]
        self.team = []
        self.exclude = set()
        self.team_p = []
        self.exclude_p = set()
        self.achv = []
        if rank == "cop":
            for team_no in range(1):
                available_poke = []
                for poke in NU_Poke:
                    if poke not in self.exclude:
                        available_poke.append(poke)
                poke = random.choice(available_poke)
                self.team.append(poke)
                self.exclude.add(poke)
                evil_poke.append(poke)
        elif rank == "grunt":
            for team_no in range(2):
                available_poke = []
                for poke in NU_Poke:
                    if poke not in self.exclude:
                        available_poke.append(poke)
                poke = random.choice(available_poke)
                self.team.append(poke)
                self.exclude.add(poke)
                evil_poke.append(poke)
        elif rank == "manager":
            for team_no in range(3):
                available_poke = []
                for poke in OU_Poke:
                    if poke not in self.exclude:
                        available_poke.append(poke)
                poke = random.choice(available_poke)
                self.team.append(poke)
                self.exclude.add(poke)
                evil_poke.append(poke)
        elif rank == "exec":
            for team_no in range(6):
                uber_rate = random.randint(1,2)
                available_poke = []
                if uber_rate == 1:
                    for poke in Uber_Poke:
                        if poke not in self.exclude:
                            available_poke.append(poke)
                    poke = random.choice(available_poke)
                    self.team.append(poke)
                    self.exclude.add(poke)
                    evil_poke.append(poke)
                else:
                    for poke in OU_Poke:
                        if poke not in self.exclude:
                            available_poke.append(poke)
                    poke = random.choice(available_poke)
                    self.team.append(poke)
                    self.exclude.add(poke)
                    evil_poke.append(poke)


    def capture(self, pokemon):
        self.team.append(pokemon)



class Pokemon:
    def __init__(self, name, evo, type_1, type_2, hp, att,
                 deff, spd, a1, a2, a3, a4):
        self.name = name
        self.evo = evo
        self.type_1 = type_1
        self.type_2 = type_2
        self.hp_1 = hp
        self.atk_stat = att
        self.deff = deff
        self.spd = spd
        self.lvl = 1
        self.health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))
        self.max_health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))
        self.atk_1 = a1
        self.atk_2 = a2
        self.atk_3 = a3
        self.atk_4 = a4
        self.att_key = [a1, a2, a3, a4]



    def attack(self, player_2, key):
        dmg_pre = round(self.atk_stat * attack_dict[key][1] / random.randint(200, 300))
        dmg_out = round(((1 + ((self.lvl - 1) /10)) * (dmg_pre * 0.5) + (dmg_pre * (0.5 * (player_2.deff/300)))) * float(type_bonus(key, player_2)))
        player_2.health -= dmg_out
        # print(dmg_pre)
        # print(dmg_out)
        d_print(f"{self.name} used {key} on {player_2.name}! [{dmg_out}]\n")
        if float(type_bonus(key, player_2)) > 1.5:
            d_print("Its super effective!\n")
        elif float(type_bonus(key, player_2)) == 0:
            d_print(f"{player_2.name} is immune to {key}\n")
        elif float(type_bonus(key, player_2)) < 1:
            d_print("Its not very effective!\n")
        # + str(player_2.health) + " " + str(dmg_out))



def police_attack(): ########################################################################3
    "function to place at the beginning of every flight selection"
    if "Global Warming" in player_achv:
        # player.health -= 20
        cop = Human("Cop", "cop")
        d_print("You noticed someone running after you, its the cops!!")
        d_print("Hold it right there! You're under arrest for excessive co2 discharge!")
        trainer_battle(player, cop)
        print("Nows your chance, RUN!!!")
        input("Press Enter to flee from the cops!")



def flight_cost():
    distance = 500
    fuel_cost = (distance / 7500) * 100
    player.fuel -= int(fuel_cost)
    co2_cost = 1
    achv_dict["co2"][1] -= co2_cost



def achievement_check(achv_dict, player_achv):
    if achv_dict["co2"][1] <= 0:
        achv_dict["co2"][1] = 999 ** 99
        player_achv.append(achv_dict["co2"][0])
    if achv_dict["rr"][1] <= 0:
        achv_dict["rr"][1] = 999 ** 99
        player_achv.append(achv_dict["rr"][0])
    if achv_dict["poker"][1] <= 0:
        achv_dict["poker"][1] = 999 ** 99
        player_achv.append(achv_dict["poker"][0])
    if achv_dict["continent"][1] <= 0:
        achv_dict["continent"][1] = 999 ** 99
        player_achv.append(achv_dict["continent"][0])
    if achv_dict["polar"][1] <= 0:
        achv_dict["polar"][1] = 999 ** 99
        player_achv.append(achv_dict["polar"][0])
    if achv_dict["defeat god"][1] <= 0:
        achv_dict["defeat god"][1] = 999 ** 99
        player_achv.append(achv_dict["defeat god"][0])
    if achv_dict["free god"][1] <= 0:
        achv_dict["free god"][1] = 999 ** 99
        player_achv.append(achv_dict["free god"][0])



def d_print(s): # CHANGE time.sleep to 0 when testing code.
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        if msvcrt.kbhit():
            key = msvcrt.getch()

            if key == b'\r':
                sys.stdout.write(f"\r{s}")
                sys.stdout.flush()
                break
    # print(s)




def helper(context):
    if context == "rr_game":
        user_input = input("Press enter to continue")
        if user_input == "/HELP":
            print("You're on your own now. You signed up for this.")
            user_input_2 = input("Press enter to continue")
            return user_input_2
        return user_input
    elif context == "trainer_battle":
        user_input = input("Enter your attack: ")
        if user_input == "/HELP":
            print("In a Pokemon Battle, you command your Pokemon by writing their attacks correctly.")
            print("Remember that attack commands are case sensitive. So pay attention to capital letters.")
            print("Swap out your Pokemon during battle by entering 'SWAP' then select the Pokemon you with to swap out")
            print("Once you defeated the opponent, you can choose to add that Pokemon to your Team.")
            print("Remember, you are a criminal on the run, and will not be able to have more than 6 Pokemon.")
            print("That means, you wont store excess Pokemon in a PC, your only option is to release them.")
            user_input_2 = input("Select your attack: ")
            return user_input_2
        return user_input
    elif context == "Poker": ### I dont know what to do here yet
        user_input = input("Enter your choice: ")
        if user_input == "/HELP":
            print("Play Poker, bet your Pokemon on the line. Remember.")
            user_input_2 = input("Select your choice: ")
            return user_input_2
        return user_input
    else:
        user_input_2 = input("Select your choice: ")
        return user_input_2



def game_russian(self, player_2):
    player_team_hp = team_health_check(self)
    opo_team_hp = team_health_check(player_2)
    print(f"{self.name} challenged {player_2.name} to Russian Roulette!")
    while len(player_team_hp) > 0 and len(opo_team_hp) > 0:
        player_team_hp = team_health_check(self)
        opo_team_hp = team_health_check(player_2)
        sacrifice = 0
        print("You must select a Pokemon to play for you.")
        for index, pokemon in enumerate(self.team):
            print(f"{index + 1}. {pokemon.name}")
        while sacrifice not in self.team:
            p_select = input("Select your Pokemon: ")
            try:
                test_1 = int(p_select)
            except ValueError:
                print("Invalid input")
                continue

            if self.team[int(p_select) - 1] in self.team:
                sacrifice = self.team[int(p_select) - 1]
            else:
                print("Invalid input")
        shot = 1
        player_list = [self, player_2]
        print(f"{sacrifice.name} will stand in for {self.name}")
        while sacrifice in self.team and len(player_2.team) > 0:
            for turn in player_list:
                print("*Spinning the barrel*")
                bullet = random.randint(1, 6)
                # print(f"Bullet is {bullet}") #remove later after testing
                if turn == self:
                    print(f"{self.name}'s turn. Click.")
                    if shot != bullet:
                        input("Press Enter to shoot")
                        print("Nothing happened.")
                        input("Press Enter to continue")
                    else:
                        input("Press Enter to shoot")
                        wild_poke.append(sacrifice)
                        self.team.remove(sacrifice)
                        print("=" * 100)
                        print(f"Bang! {sacrifice.name} fell giving you everything.")
                        input("Press enter to continue.")
                        player_team_hp = team_health_check(self)
                        opo_team_hp = team_health_check(player_2)
                        break
                elif turn == player_2:
                    print(f"{player_2.name}'s turn. Click.")
                    if shot != bullet:
                        input("Press Enter to shoot")
                        print("Nothing happened.")
                        input("Press Enter to continue")
                    else:
                        input("Press Enter to shoot")
                        print("=" * 100)
                        print(f"Bang! {player_2.team[0].name} fell abruptly.")
                        wild_poke.append(player_2.team[0])
                        player_2.team.remove(player_2.team[0])
                        player_team_hp = team_health_check(self)
                        opo_team_hp = team_health_check(player_2)
                        if len(player_2.team) > 0:
                            print(f"{player_2.team[0].name} steps up in its trainer's place.")
                        else:
                            print(f"{player_2.name} is out of Pokemon.")
                            break
                    print("=" * 100)
                    player_team_hp = team_health_check(self)
                    opo_team_hp = team_health_check(player_2)


    if len(player_team_hp) > 0:
        print("You get to walk away.")
    else:
        print("You made a lot of bad choices. Game Over.")



def wild_pokemon_assigner(player, evil):
    """
    A function to move all the unused pokemon into the wild pool
    :param player:
    :param evil:
    :return:
    """
    for pokemon in LC_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)
    for pokemon in NU_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)
    for pokemon in OU_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)
    for pokemon in Uber_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)



def type_bonus(key: str, defender) -> int:
    """
    Returns the integer of the type bonus an attack has on any specific Pokemon.
    :param key: The attack key for the attack dictionary
    :param defender: The defending Pokemon
    :return: Integer of percentage bonus, 1 = 100%
    """
    if str(attack_dict[key][0]) + str(defender.type_1) in type_bonus_dict:
        bonus_1 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)]
        if str(attack_dict[key][0]) + str(defender.type_2) in type_bonus_dict:
            bonus_2 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)] * type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_2)]
            return bonus_2
        return bonus_1
    else:
        return 1



def team_health_check(trainer):
    """
    Checks the Trainer's team, returns a list of Pokemon in that team who
    health is over 0.
    :param trainer: Variable the trainer is assigned to
    :return: List of healthy Pokemon
    """
    healthy_trainer_team = []
    for poke in trainer.team:
        if poke.health > 0:
            healthy_trainer_team.append(poke)
    return healthy_trainer_team



def opo_bonus(opponent):
    """
    Adjusts the health stats of a particular Pokemon, this code is meant
    to be used to increase the health of an opponent to artificially increase
    difficulty.
    :param opponent: The Pokemon, whose stat to be modified
    :return: None
    """
    opponent.health *= 2
    opponent.max_health *= 2



def type_display(poke):
    """
    Returns str of a Pokemon's type as such: [ Type 1 ] [ Type 2 ] with
    space reserved
    :param poke: Pokemon
    :return: Str of the Pokemon's type
    """
    if poke.type_2 != None:
        output = f"[{poke.type_1:^10}][{poke.type_2:^10}]"
    else:
        output = f"[{poke.type_1:^10}]"

    return output



def poke_hp_bar(pokemon_a):
    """
    Returns the Pokemon HP bar, used as a visual indicator of the Pokemon's
    health percentage
    :param pokemon_a: Pokemon whose health is to be displayed
    :return: Str of Pokemon's health as a bar
    """
    c_hp = int(pokemon_a.health)
    f_hp = int(pokemon_a.max_health)
    bar ="■" * (round( c_hp / f_hp * 20))
    output = ("[" + f"{bar:<20}]" )
    return output



def alive_team(teammates, exclude=None):
    """
    Takes in your team via you.team format and returns your alive team
    members.
    :param teammates: Your team in you.team format
    :param exclude:
    :return: Alive team members.
    """
    alive_members = [p for p in teammates if p.health > 0 and p is not exclude]
    return alive_members



def choose_switch_from_team(teammates, exclude = None, prompt =
"Who do you want to swap to?"):
    """
    Takes in your team (you.team), with option to exclude and gives you
    a prompt asking who do you want to swap to. Prints out your healthy Pokemon
    and returns your selection for who to send out next.
    :param teammates: Your team in you.team format
    :param exclude: Leave empty
    :param prompt: Leave empty
    :return: Chosen Pokemon
    """
    options = alive_team(teammates, exclude=exclude)
    if not options:
        return None
    print(prompt)
    for index, pokemon_a in enumerate(options):
        print(f"{index + 1}. {pokemon_a.name} [HP: {max(pokemon_a.health,0)} / {pokemon_a.max_health}] (Lv. {pokemon_a.lvl})")
    while True:
        try:
            pick = int(input("Send out: "))
            if 1 <= pick <= len(options):
                return options[pick - 1]
        except ValueError:
            pass
        print("Invalid choice. Try again.")



def swap_out(current, you):
    """
    (This is meant to be used when its your turn and you want to swap,
    not when your Pokemon fainted)
    Takes in your current Pokemon, and You, then shows you your other Pokemon
    and asks you if you want to switch to any of them.
    :param current: your current Pokemon
    :param you: The player
    :return: The Pokemon you chose to swap to
    """
    return choose_switch_from_team(you.team, exclude = current, prompt = "Who do you want to swap to?")



def your_battle_turn(your_mon, opo_mon, you, opo):
    """
    Function for your battle turn, takes in your pokemon, opponent Pokemon,
    you, and opponent then performs the battle functions or swap functions
    for gameplay.
    :param your_mon: Your Pokemon
    :param opo_mon: Your opponent's Pokemon
    :param you: The player
    :param opo: The opponent
    :return:
    """
    your_att = helper("trainer_battle")
    if your_att == "SWAP":
        new_mon = swap_out(your_mon, you)
        if new_mon is None:
            print("No other healthy Pokemon!!")
        else:
            d_print(f"{your_mon.name} come back! Go, {new_mon.name}!\n")
            return "switch", new_mon
    # your_att = "Flamethrower"
    if your_att in your_mon.att_key:
        your_mon.attack(opo_mon, your_att)
        input("Press Enter to continue")
        return "no switch"
    elif your_att != "SWAP" and your_att not in your_mon.att_key:
        d_print(f"You fumbled your command, {your_mon.name} froze in confusion!\n")
        input("Press Enter to continue")
        return "no switch"
    else:
        input("Press Enter to continue")
        return "no switch"



def into_team(player, opo, wild):
    """
    The inner function used for stealing or capturing Pokemon, the function
    creates a loop until you enter 0 that allows you to move the opposing
    pokemon into your team, and moves excess Pokemon into the wild list
    :param player: player
    :param opo: opponent whose team to check, write None if capturing wild Pokemon
    :param wild: wild pokemon, write None if battling human NPC
    :return: None
    """
    if wild == None:
        while True:
            if len(player.team) < 6:
                while len(player.team) < 6 and len(opo.team) > 0:
                    print(f"{opo.team[0].name} was added to your team.")
                    player.team.append(opo.team[0])
                    opo.team.remove(opo.team[0])
                    if len(player.team) == 6:
                        continue
            else:
                d_print("Which Pokemon would you like to add to your team?\n")
                for index_o, poke_o in enumerate(opo.team):
                    print(f"{index_o + 1}. {poke_o.name}")
                print(f"0. End")
                user_input_opo = input("Select your choice: ")
                try:
                    test_1 = int(user_input_opo)
                except ValueError:
                    print("Invalid input")
                    continue
                if 0 < int(user_input_opo) <= len(opo.team):
                    d_print("Which Pokemon from your team would you like to release?\n")
                    for index_p, poke_p in enumerate(player.team):
                        print(f"{index_p + 1}. {poke_p.name}")
                    print(f"0. End")
                    user_input_player = input("Select your choice: ")
                    try:
                        test_01 = int(user_input_player)
                    except ValueError:
                        print("Invalid input")
                        continue
                    if 0 < int(user_input_player) <= len(player.team):
                        wild_poke.append(player.team[int(user_input_player) - 1])
                        player.team[int(user_input_player) - 1] = opo.team[int(user_input_opo) - 1]
                        opo.team.remove(opo.team[int(user_input_opo) - 1])
                    elif int(user_input_player) == 0:
                        if len(opo.team) > 0:
                            for index, poke in enumerate(opo.team):
                                wild_poke.append(opo.team[index])
                                opo.team.remove(opo.team[index])
                        d_print("Stealing ended\n")
                        break
                    else:
                        print("Invalid input")
                elif int(user_input_opo) == 0:
                    if len(opo.team) > 0:
                        for index, poke in enumerate(opo.team):
                            wild_poke.append(opo.team[index])
                            opo.team.remove(opo.team[index])
                    d_print("Stealing ended\n")
                    break
                else:
                    print("Invalid input")
    elif opo == None:
        while True:
            d_print("Which Pokemon from your team would you like to release?\n")
            for index_p, poke_p in enumerate(player.team):
                print(f"{index_p + 1}. {poke_p.name}")
            print(f"0. End")
            user_input_player = input("Select your choice: ")
            try:
                test_01 = int(user_input_player)
            except ValueError:
                print("Invalid input")
                continue
            if 0 < int(user_input_player) <= len(player.team):
                wild_poke.append(player.team[int(user_input_player) - 1])
                player.team[int(user_input_player) - 1] = wild
                wild_poke.remove(wild)
                break
            elif int(user_input_player) == 0:
                print("Capture ended")
                break
            else:
                print("Invalid input")


# Ignore the highlight here
def wild_capture(wild, player):
    """
    Takes in wild Pokemon and Player, and asks you if you want to add it to
    your team. If you select yes, it will run the into_team function
    :param wild:
    :param player:
    :return:
    """
    while True:
        if len(player.team) < 6:
            print(f"{wild.name}, started following you.")
            player.team.append(wild)
            break
        else:
            d_print("""You cannot have more than 6 Pokemon, and you do not have 
legal access to a PC to store excess Pokemon.\n""")
            print("Would you like to capture this Pokemon?")
            print("1. Yes")
            print("2. No")
            y_n = int(input("Select your choice:"))
            if y_n == 1:
                into_team(player, None, wild)
                break
            if y_n == 2:
                break
            else:
                print("Invalid input")
input("Press Enter to continue")

# Ignore the highlight here
def battle_steal(player, opo):
    """
    Takes in Opponent and Player, and asks you if you want to add pokemon from
    the opponent's team to your team. If you select yes, it will run the
    into_team function. If it is the first time you are running this function it
    will present an extra prompt
    :param player: player
    :param opo: opponent
    :return:
    """
    first_time = 1
    while first_time >= 1 and len(player.team) >= 6:
        d_print("""You won! But you're only able to carry 6 Pokemon at all times.\n""")
        first_time -= 1

    into_team2(player, opo, None)



def all_poke_heal(player):
    """
    Heals all Pokemon in the team, can be used for any trainer class.
    :param player:
    :return:
    """
    for pokemon in player.team:
        pokemon.health = round((1 + ((pokemon.lvl - 1) /10)) *150 * (pokemon.hp_1/100))



def pokemon_battle_4trainer(your_mon, opo_mon, you, opo):
    """
    The inner function for the trainer battle function. Requires you to enter
    the player's first Pokemon, the Opponent's first Pokemon, the player, and
    the opponent.
    :param your_mon: Player's Pokemon
    :param opo_mon: Opponent's Pokemon
    :param you: The Player
    :param opo: The Opponent
    :return: None
    """
    while your_mon.health > 0 and opo_mon.health > 0:
        print("=" * 100)
        your_hp_str = f"{your_mon.health}/{your_mon.max_health}"
        opo_hp_str = f"{opo_mon.health}/{opo_mon.max_health}"
        print(f"{str(your_mon.name) + " [Lv." + str(your_mon.lvl) + "]":<40} "
              f"{str(opo_mon.name) + " [Lv." + str(opo_mon.lvl)}]")
        print(f"{type_display(your_mon):<41}" + type_display(opo_mon))
        print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
        print(f"HP:{your_hp_str:<38}HP:{opo_hp_str}" )
        print("")
        print("")
        print("")
        print("Your Moves: ")
        print(f"[{your_mon.atk_1:^20}][{your_mon.atk_2:^20}]")
        print(f"[{your_mon.atk_3:^20}][{your_mon.atk_4:^20}]")
        if your_mon.spd >= opo_mon.spd:
            if your_mon.health > 0:
                battle_input = your_battle_turn(your_mon, opo_mon, you, opo)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]
            if opo_mon.health > 0:
                d_print("Opponent's turn!\n")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
        else:
            if opo_mon.health > 0:
                d_print("Your opponent is fast!\n")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
            if your_mon.health > 0:
                battle_input = your_battle_turn(your_mon, opo_mon, you, opo)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]

        if your_mon.health <= 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{"0":<38}HP:{opo_hp_str}")
            d_print(f"Your {your_mon.name} is knocked out!\n")
            replacement = choose_switch_from_team(you.team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
            if replacement is None:
                d_print("You have no Pokemon left..\n")
                d_print("That's okay, you can get em next time!\n")
                break
            d_print(f"Go, {replacement.name}!\n")
            your_mon = replacement
        elif your_mon.health > 0 and opo_mon.health <= 0:
            healthy_opo_team = team_health_check(opo)
            your_healthy_team = team_health_check(you)
            d_print(f"{opo_mon.name} is knocked out!\n")
            if len(healthy_opo_team) > 0:
                d_print(f"Opponent sends out {healthy_opo_team[0].name}!\n")
                opo_mon = healthy_opo_team[0]
                input("Press Enter to continue")
            # print("=" * 100)
            # print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
            #       f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            # print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            # print(f"HP:{your_hp_str:<38}HP:0/{opo_mon.max_health}")
            # print("The opposing Pokémon is knocked out!")
            # print("You won!")



def trainer_battle(you, opo):
    """
    The outer function for trainer battles, takes in the player and the
    TRAINER opponent, then automatically runs the pokemon_battle_4trainer
    function, with the appropriate prompts when winning or losing.
    :param you: Player
    :param opo: Trainer Opponent
    :return:
    """
    healthy_opo_team = team_health_check(opo)
    your_healthy_team = team_health_check(you)
    print(f"\n{opo.name} sends out {opo.team[0].name}")
    print(f"\nYou send out {you.team[0].name}")
    while len(healthy_opo_team) > 0 and len(your_healthy_team) > 0:
        healthy_opo_team = team_health_check(opo)
        your_healthy_team = team_health_check(you)
        pokemon_battle_4trainer(you.team[0], opo.team[0], you, opo)


    if len(healthy_opo_team) <= 0:
        print("You Won!")
        battle_steal(you, opo)
    elif len(your_healthy_team) <= 0:
        print("You Lost!")

    # for poke in you.team: # Code for testing team modification
    #     print(poke.name)



def pokemon_battle_4wild(your_mon, wild_mon, you):
    """
    The inner function for the wild encounter battle with wild Pokemon.
    :param your_mon: Your first Pokemon in your team
    :param wild_mon: The wild Pokemon
    :param you: The player
    :return:
    """
    opo_mon = wild_mon
    while your_mon.health > 0 and opo_mon.health > 0:
        print("=" * 100)
        your_hp_str = f"{your_mon.health}/{your_mon.max_health}"
        opo_hp_str = f"{opo_mon.health}/{opo_mon.max_health}"
        print(f"{str(your_mon.name) + " [Lv." + str(your_mon.lvl) + "]":<40} "
              f"{str(opo_mon.name) + " [Lv." + str(opo_mon.lvl)}]")
        print(f"{type_display(your_mon):<41}" + type_display(opo_mon))
        print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
        print(f"HP:{your_hp_str:<38}HP:{opo_hp_str}" )
        print("")
        print("")
        print("")
        print("Your Moves: ")
        print(f"[{your_mon.atk_1:^20}][{your_mon.atk_2:^20}]")
        print(f"[{your_mon.atk_3:^20}][{your_mon.atk_4:^20}]")
        if your_mon.spd >= opo_mon.spd:
            if your_mon.health > 0:
                battle_input = your_battle_turn(your_mon, opo_mon, you, None)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]
            if opo_mon.health > 0:
                d_print("Opponent's turn!\n")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
        else:
            if opo_mon.health > 0:
                d_print("Your opponent is fast!\n")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
            if your_mon.health > 0:
                battle_input = your_battle_turn(your_mon, opo_mon, you, None)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]

        if your_mon.health <= 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{"0":<38}HP:{opo_hp_str}")
            print(f"Your {your_mon.name} is knocked out!")
            replacement = choose_switch_from_team(you.team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
            if replacement is None:
                d_print("You have no Pokemon left..\n")
                d_print("That's okay, you can get em next time!\n")
                break
            print(f"Go, {replacement.name}!")
            your_mon = replacement
        elif your_mon.health > 0 and opo_mon.health <= 0:
            your_healthy_team = team_health_check(you)
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{your_hp_str:<38}HP:0/{opo_mon.max_health}")
            d_print("The opposing Pokémon is knocked out!\n")
            print("You won!")



def wild_encounter_battle(your_mon, you, wild_pokemon_list):
    """
    Takes in your first Pokemon, you, and the wild Pokemon list (wild Poke)
    or you can change the wild Poke list to be randomly selected from, then
    runs the wild Pokemon Battle Function
    :param your_mon: Your first Pokemon in you.team format
    :param you: The player
    :param wild_pokemon_list: the list of wild Pokemon to be randomly selected
    :return:
    """
    d_print(random.choice(land_safe) + "\n")
    wild_mon = random.choice(wild_pokemon_list)
    d_print(f"\nA wild {wild_mon.name} appeared!!\n")
    pokemon_battle_4wild(your_mon, wild_mon, you)
    your_healthy_team = team_health_check(you)
    if len(your_healthy_team) <= 0:
        print("You Lost!")
    else:
        wild_capture(wild_mon, you)
    # for poke in you.team: # Code for testing team modification
    #     print(poke.name)



def wild_arceus_battle(your_mon, you, wild_pokemon_list):
    """
    Takes in your first Pokemon, you, and the wild Pokemon list (wild Poke)
    or you can change the wild Poke list to be randomly selected from, then
    runs the wild Pokemon Battle Function
    :param your_mon: Your first Pokemon in you.team format
    :param you: The player
    :param wild_pokemon_list: the list of wild Pokemon to be randomly selected
    :return:
    """
    d_print("The earth began to rumble, the heavens parted, and a portal in the sky opened.\n")
    d_print("For your transgression, you will be judge by he who stands above all other Pokemon.\n")
    wild_mon = random.choice(wild_pokemon_list)
    d_print(f"\nA wild {wild_mon.name} appeared!!\n")
    pokemon_battle_4wild(your_mon, wild_mon, you)
    your_healthy_team = team_health_check(you)
    if len(your_healthy_team) <= 0:
        print("You Lost!")
    else:
        wild_capture(wild_mon, you)
    # for poke in you.team: # Code for testing team modification
    #     print(poke.name)



def start_rr_game(player, opo):
    """
    For starting the Russian roulette game.
    :param player: Player
    :param opo: Opponent NPC
    :return:
    """
    print("""You are about to initiate a game of Russian Roulette. There's no
turning back if you decide to start until either you or your opponent are out
of Pokemon. Are you sure you want to continue?""")
    print("1. Yes")
    print("2. No")
    while True:
        choice = input("Select your choice: ")
        try:
            y_n = int(choice)
        except ValueError:
            print("Invalid input.")
            continue
        if y_n == 1:
            game_russian(player, opo)
            break
        elif y_n == 2:
            print("You left the interaction.")
            break
        else:
            print("Invalid input")



def poker(player1,player2):
    """
    Poker demo (2 players) with ASCII card rendering and basic hand evaluation.
    Notes:
    - Ranking tuple shape varies across categories; see `CATEGORY_NAME`.
    """
    import random
    ranks = list(range(2,15))
    # suits = ['C','D','H','S']  #C -> Clubs, D-> Diamonds, H-> Hearts, S -> Spades
    ranks_string = {11: 'J',12: 'Q',13: 'K',14: 'A'}
    # suits_icon = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}
    suits = ['♣','♦','♥','♠']

    CATEGORY_NAME = {
        10: "Royal Flush",
        9: "Straight Flush",
        8: "Four of a Kind",
        7: "Full House",
        6: "Flush",
        5: "Straight",
        4: "Three of a Kind",
        3: "Two Pair",
        2: "One Pair",
        1: "High Card",
    }

    # Pack of cards
    def new_pack():
        """
        Build a standard 52-card pack.

        Returns:
            list[tuple[int, str]]: List of cards where each card is (rank, suit),
            rank in [2..14] (14 = Ace), suit in {'♣','♦','♥','♠'}.
        """
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append((rank,suit))
        return deck
    pack_of_cards = new_pack()
    random.shuffle(pack_of_cards)
    #Card
    # a = random.choice(pack_of_cards)

    def card_str(card):
        """
           Convert a card tuple to a short human-readable string.

           Args:
               card (tuple[int, str]): The card as (rank, suit).

           Returns:
               str: e.g., "A♠", "10♦", "J♥".
           """
        r, s = card
        return f"{ranks_string.get(r, r)}{s}"

    def deal(n):
        """
           Pop and return n cards from the global shuffled pack.

           Args:
               n (int): Number of cards to deal.

           Returns:
               list[tuple[int, str]]: A list of n cards (rank, suit).

           Side Effects:
               Mutates `pack_of_cards` by popping from the end.
           """
        return [pack_of_cards.pop() for _ in range(n)]
    your_cards = deal(2)
    # print(your_cards)
    bot_cards = deal(2)
    Flop = deal(3)
    Turn = deal(1)
    River = deal(1)

    # print(' - '.join(card_str(i)for i in your_cards)) -> Card output
    def show(x):

        y = (' - '.join(card_str(c) for c in x))
        return y
    ##Draw
    def ascii_card(rank, suit):
        """
          Render a single card as a list of ASCII-art lines.

          Args:
              rank (int): 2..14 (11=J,12=Q,13=K,14=A).
              suit (str): One of {'♣','♦','♥','♠'}.

          Returns:
              list[str]: 5 lines forming a boxed ASCII card.
                         Use together with `show_hand` to print side-by-side.
          """
        suit_symbol = {
            '♠': '♠',
            '♥': '♥',
            '♦': '♦',
            '♣': '♣'
        }
        rank_str = {11: "J", 12: "Q", 13: "K", 14: "A"}.get(rank, str(rank))
        s = suit_symbol[suit]

        return [
            "┌───────┐",
            f"│{rank_str:<2}     │",
            f"│   {s}   │",
            f"│     {rank_str:>2}│",
            "└───────┘"
        ]

    def show_hand(cards):
        """
          Print multiple ASCII cards side-by-side.

          Args:
              cards (list[tuple[int, str]]): Cards to render, each (rank, suit).

          Output:
              Prints to stdout the combined ASCII-art of all cards.
          """
        ascii_cards = [ascii_card(r, s) for (r, s) in cards]
        for row in zip(*ascii_cards):
            print("  ".join(row))

    # board = [show(Flop), show(Turn), show(River)]
    board = [Flop, Turn, River]
    street = []
    idx = -1
    #Main Gameplay
    print('[PRE-FLOP]')
    print('Your card: ')

    # print('Your cards: ',show(your_cards))
    show_hand(your_cards)
    while True:
        idx = idx + 1
        lst = ['FLOP', 'TURN', 'RIVER']
        for i in board[idx]:
            street.append(i)
        # street.append(board[idx])
        if input('Press enter to continue...: ') == '':

            print(f'{lst[idx]}')
            print('Your card: ')
            show_hand(your_cards)
            print('Board: ')
            show_hand(street)
            # print(f'Board: {street}')
            if idx == 2:
                break
    #Whole
    your_whole = your_cards + Flop + Turn + River
    # for i in your_cards:
    #     whole.append(i)
    # for i in Flop:
    #     whole.append(i)
    # for i in Turn:
    #     whole.append(i)
    # for i in River:
    #     whole.append(i)
    # print('whole=',your_whole)

    from collections import Counter

    ranks7 = [r for r, s in your_whole]
    suits7 = [s for r, s in your_whole]

    rc = Counter(ranks7)   #Count by rank
    sc = Counter(suits7)   #Count by suit
    # print('ranks7=',rc)
    # print('suits7=',sc)
    #Pair
    pair = [r for r, c in rc.items() if c >= 2]
    # print('pair=',pair)
    #Triple
    triple = [r for r,c in rc.items() if c >= 3]
    # print('triple=',triple)
    #Four of a Kind
    four = [r for r,c in rc.items() if c ==4]
    # print('four=',four)
    #Flush
    flush = [s for s,c in sc.items() if c >= 5]
    # print('flush=',flush)
    pairs = sorted([r for r,c in rc.items() if c == 2], reverse=True)
    trips = sorted([r for r,c in rc.items() if c == 3], reverse=True)
    # Straight
    r = []
    s = []
    for i in your_whole:
        a, b = i
        r.append(a)
        s.append(b)
    r = set(r)
    s = set(s)
    r = list(r)
    s = list(s)
    r.sort(reverse=True)

    # print('r=',r)
    def straight():
        """
         Detect straight or straight flush from player's 7 cards.

         Logic:
             - Check straight flush/royal flush by scanning ranks within any flush suit.
             - Then check normal straight using unique sorted ranks.
             - Straight wheel (A-2-3-4-5) is NOT considered.

         Returns:
             tuple:
                 (kind, high, sequence)
                 - kind (str): 'Royal Flush', 'Straight Flush', 'Normal straight', or 'Not Straight'
                 - high (int): Highest rank of the straight (e.g., 14 for A-high), or a fallback top rank.
                 - sequence (list[int]): Ranks of the found straight window, or the unique rank list when not found.

         Notes:
             Uses outer-scope variables `your_whole` and `flush`.
         """
        for fs in flush:
            suit_ranks = sorted({rr for (rr, ss) in your_whole if ss == fs}, reverse=True) #To get the number with the same suit by flush
            for i in range(len(suit_ranks) - 4):
                w = suit_ranks[i:i + 5]
                if all(w[j] - 1 == w[j + 1] for j in range(4)):
                    if w[0] == 14:
                        return 'Royal Flush', 14, w
                    else:
                        return 'Straight Flush', w[0], w
        for i in range(len(r) - (5 - 1)):
            window = r[i:i + 5]
            if all(window[j] - 1 == window[j + 1] for j in range(4)):
                return 'Normal straight', window[0], window
        else:
                return 'Not Straight', r[0], r

    #Main mechanic of game
    ##What you got
    if straight()[0] == 'Royal Flush':
        Bool, High, Straight = straight()
        rank = 10,High
    elif straight()[0] == 'Straight Flush':
        Bool, High, Straight = straight()
        rank = 9, High
    elif len(four) >=1:
        rest = sorted(set(ranks7), reverse=True)
        rest.remove(four[0])
        kicker = rest[0]
        rank = 8, max(four), kicker
    elif len(trips) >= 2:
            rank = (7, trips[0], trips[1])  # Highest trips + Next Trips
    elif trips and pairs:
            rank = (7, trips[0], pairs[0])  # trips + Highest pair
    elif len(flush) >=1:
        for fs in flush:
            rank_in_fs = [r for (r, s) in your_whole if s == fs]
            rank_in_fs.sort(reverse=True)
            rank = 6, rank_in_fs[:5]
    elif straight()[0] == 'Normal straight':
        Bool, High, Straight = straight()
        rank = 5, High
    elif len(triple) >=1:
        rest = sorted(set(ranks7), reverse=True)
        rest.remove(triple[0])
        kicker = rest[:2]
        k1, k2 = kicker
        rank = 4, max(triple), k1, k2
    elif len(pair) >= 2:
        rest = sorted(set(ranks7), reverse=True)
        pair.sort(reverse=True)
        rest.remove(pair[0])
        rest.remove(pair[1])
        rank = 3, pair[0],pair[1],max(rest)
    elif len(pair) >= 1:
        rest = sorted(set(ranks7), reverse=True)
        rest.remove(pair[0])
        kicker = rest[:3]

        rank = 2, pair[0], kicker
    else:
        card = r[:5]
        rank = 1, card

    # print(50*'=')
    # print(f'Bot cards {show(bot_cards)}')
    ##What Bot Got
    #Bot Whole
    bot_whole = bot_cards + Flop + Turn + River

    # print('Bot whole=',bot_whole)

    from collections import Counter

    ranksbots7 = [r for r, s in bot_whole]
    suitsbots7 = [s for r, s in bot_whole]

    rcbot = Counter(ranksbots7)
    scbot = Counter(suitsbots7)
    # print('ranks7=',rcbot)
    # print('suits7=',scbot)
    #Pair
    pairbot = [r for r, c in rcbot.items() if c >= 2]
    # print('pairbot=',pairbot)
    #Triple
    triplebot = [r for r,c in rcbot.items() if c >= 3]
    # print('triplebot=',triplebot)
    #Four of a Kind
    fourbot = [r for r,c in rcbot.items() if c ==4]
    # print('fourbot=',fourbot)
    #Flush
    flushbot = [s for s,c in scbot.items() if c >= 5]
    # print('flushbot=',flushbot)
    pairsbot = sorted([r for r,c in rcbot.items() if c == 2], reverse=True)
    tripsbot = sorted([r for r,c in rcbot.items() if c == 3], reverse=True)
    # Straight
    rbot = []
    sbot = []
    for i in bot_whole:
        a, b = i
        rbot.append(a)
        sbot.append(b)
    rbot = set(rbot)
    sbot = set(sbot)
    rbot = list(rbot)
    sbot = list(sbot)
    rbot.sort(reverse=True)
    # print('r=',r)
    def straightbot():
        """
        Same logic with straight() function.
        """
        for fs in flushbot:
            suit_ranks = sorted({rr for (rr, ss) in bot_whole if ss == fs}, reverse=True)
            for i in range(len(suit_ranks) - 4):
                w = suit_ranks[i:i + 5]
                if all(w[j] - 1 == w[j + 1] for j in range(4)):
                    if w[0] == 14:
                        return 'Royal Flush', 14, w
                    else:
                        return 'Straight Flush', w[0], w
        for i in range(len(rbot) - (5 - 1)):
            window = rbot[i:i + 5]
            if all(window[j] - 1 == window[j + 1] for j in range(4)):
                return 'Normal straight', window[0], window
        else:
                return 'Not Straight', rbot[0], rbot
    if straightbot()[0] == 'Royal Flush':
        Bool, High, Straight = straightbot()
        rankbot = 10,High
    elif straightbot()[0] == 'Straight Flush':
        Bool, High, Straight = straightbot()
        rankbot = 9, High
    elif len(fourbot) >=1:
        rest = sorted(set(ranksbots7), reverse=True)
        rest.remove(fourbot[0])
        kicker = rest[0]
        rankbot = 8, max(fourbot), kicker
    elif len(tripsbot) >= 2:
            rankbot = (7, tripsbot[0], tripsbot[1])  # Highest trips + Next Trips
    elif tripsbot and pairsbot:
            rankbot = (7, tripsbot[0], pairsbot[0])  # trips + Highest pair
    elif len(flushbot) >=1:
        for fs in flushbot:
            rank_in_fs = [r for (r, s) in bot_whole if s == fs]
            rank_in_fs.sort(reverse=True)
            rankbot = 6, rank_in_fs[:5]
    elif straightbot()[0] == 'Normal straight':
        Bool, High, Straight = straightbot()
        rankbot = 5, High
    elif len(triplebot) >=1:
        rest = sorted(set(ranksbots7), reverse=True)
        rest.remove(triplebot[0])
        kicker = rest[:2]
        k1, k2 = kicker
        rankbot = 4, max(triplebot), k1, k2
    elif len(pairbot) >= 2:
        rest = sorted(set(ranksbots7), reverse=True)
        pairbot.sort(reverse=True)
        rest.remove(pairbot[0])
        rest.remove(pairbot[1])
        rankbot = 3, pairbot[0], pairbot[1], max(rest)
    elif len(pairbot) >= 1:
        rest = sorted(set(ranksbots7), reverse=True)
        rest.remove(pairbot[0])
        kicker = rest[:3]
        rankbot = 2, pairbot[0], kicker
    else:
        card = rbot[:5]
        rankbot = 1, card

    print(f'You have got a/an {CATEGORY_NAME.get(rank[0])}')
    print(f'Bot has got a/an {CATEGORY_NAME.get(rankbot[0])}')
    print(f'Bot Cards: {show(bot_cards)}')

    #Comparison
    if rank[0:] > rankbot[0:]:
        print("Congratulations! You won!")
        achv_dict["poker"][1] -= 1
        into_team2( player1, player2,None)
        # villain_list.remove(villain_list[0])
        # show_poke(main_pokemon_file.Sam)
        # print('Kari')
        # show_poke(main_pokemon_file.Kari)
    elif rank[0:] < rankbot[0:]:
        print("You lost, you're a loser, your parents were right.")
        lose_poke(player1 ,player2 )

    elif rank[0:] == rankbot[0:]:
        print("Its a draw! You're a terrible artist.")
        a = input("Do you wanna play again? (y/n)")
        if a == 'y':
            poker(player1, player2)
        elif a == 'n':
            print("Fine")



def into_team2(player, opo, wild):
    """
    The inner function used for stealing or capturing Pokemon, the function
    creates a loop until you enter 0 that allows you to move the opposing
    Pokemon into your team, and moves excess Pokemon into the wild list
    :param player: player
    :param opo: opponent whose team to check, write None if capturing wild Pokemon
    :param wild: wild pokemon, write None if battling human NPC
    :return: None
    """
    if wild == None:
        while True:
            if len(opo.team) == 0:
                break
            if len(player.team) < 6:
                while len(player.team) < 6 and len(opo.team) > 0:
                    print(f"{opo.team[0].name} was added to your team.")
                    player.team.append(opo.team[0])
                    opo.team.remove(opo.team[0])
                    if len(player.team) == 6:
                        continue
                    if len(opo.team) == 0:
                        break
                # break
            else:
                d_print("Which Pokemon would you like to add to your team?\n")
                for index_o, poke_o in enumerate(opo.team):
                    print(f"{index_o + 1}. {poke_o.name}")
                print(f"0. End")
                user_input_opo = input("Select your choice: ")
                try:
                    test_1 = int(user_input_opo)
                except ValueError:
                    print("Invalid input")
                    continue
                if 0 < int(user_input_opo) <= len(opo.team):
                    d_print("Which Pokemon from your team would you like to release?\n")
                    for index_p, poke_p in enumerate(player.team):
                        print(f"{index_p + 1}. {poke_p.name}")
                    print(f"0. End")
                    user_input_player = input("Select your choice: ")
                    try:
                        test_01 = int(user_input_player)
                    except ValueError:
                        print("Invalid input")
                        continue
                    if 0 < int(user_input_player) <= len(player.team):
                        wild_poke.append(player.team[int(user_input_player) - 1])
                        player.team[int(user_input_player) - 1] = opo.team[int(user_input_opo) - 1]
                        opo.team.remove(opo.team[int(user_input_opo) - 1])
                    elif int(user_input_player) == 0:
                        if len(opo.team) > 0:
                            for index, poke in enumerate(opo.team):
                                wild_poke.append(opo.team[index])
                                opo.team.remove(opo.team[index])
                        d_print("Stealing ended\n")
                        break
                    else:
                        print("Invalid input")
                elif int(user_input_opo) == 0:
                    if len(opo.team) > 0:
                        for index, poke in enumerate(opo.team):
                            wild_poke.append(opo.team[index])
                            opo.team.remove(opo.team[index])
                    d_print("Stealing ended\n")
                    break
                else:
                    print("Invalid input")
            # break
    elif opo == None:
        while True:
            d_print("Which Pokemon from your team would you like to release?\n")
            for index_p, poke_p in enumerate(player.team):
                print(f"{index_p + 1}. {poke_p.name}")
            print(f"0. End")
            user_input_player = input("Select your choice: ")
            try:
                test_01 = int(user_input_player)
            except ValueError:
                print("Invalid input")
                continue
            if 0 < int(user_input_player) <= len(player.team):
                wild_poke.append(player.team[int(user_input_player) - 1])
                player.team[int(user_input_player) - 1] = wild
                wild_poke.remove(wild)
                break
            elif int(user_input_player) == 0:
                print("Capture ended")
                break
            else:
                print("Invalid input")



def lose_poke(player,opo):
    d_print("The opponent stole one of your Pokemon, you ran off!\n")
    d_print("Well, that suck.")
    time.sleep(1)
    if len(player.team) > 0:
        take = random.choice(player.team)
        player.team.remove(take)
        opo.team.append(take)
        evil_poke.append(take)



def villain_interaction(player, villain):
    """
    Function for interacting with a villain when player lands on an airport
    with an anomaly.
    :param player:
    :param villain:
    :return:
    """
    if villain.rank == "cop":
        time.sleep(1.5)
        trainer_battle(player, villain)
        if len(villain.team) <= 0:
            d_print(f"The {villain.name} fumbled and you took his Pokemon.\n")
            if len(villain.team) < 0:
                villain_list.remove(villain)
                wild_pokemon_assigner(player, evil_poke)

    else:
        d_print(random.choice(landed_evil) + "\n")
        print()
        d_print(f"{villain.name}: {random.choice(villain_intro)}\n")
        d_print(f"{villain.name}: {random.choice(wdyw_line)}\n")
        print("""1. Battle
2. Play Poker
3. Play Russian Roulette
0. Exit""")
        while True:
            while True:
                user_input = input("Select your choice: ")
                try:
                    input_check = int(user_input)
                    break
                except ValueError:
                    print("Invalid input")
                    continue
            if user_input == "1": # Battle
                d_print(random.choice(battle_intro_line) + "\n")
                time.sleep(1)
                trainer_battle(player, villain)
                if len(villain.team) <= 0:
                    d_print(f"{villain.name} surrendered and have given themselves to the police.\n")
                    if len(villain.team) <= 0:
                        villain_list.remove(villain_list[0])
                        wild_pokemon_assigner(player, evil_poke)
                break
            elif user_input == "2": # Poker
                d_print(random.choice(poker_intro_line) + "\n")
                time.sleep(1)
                poker(player, villain)
                if len(villain.team) <= 0:
                    d_print(f"{villain.name} surrendered and have given themselves to the police.\n")
                    # ACHV DICT ALREADY MODIFIED IN THE POKER FUNCTION
                    if len(villain.team) <= 0:
                        villain_list.remove(villain_list[0])
                        wild_pokemon_assigner(player, evil_poke)
                break
            elif user_input == "3": # Roulette
                d_print(random.choice(roulette_intro_line) + "\n")
                time.sleep(1)
                start_rr_game(player, villain)
                if len(villain.team) <= 0:
                    d_print(f"{villain.name} surrendered and have given themselves to the police.\n")
                    if len(villain.team) <= 0:
                        achv_dict["rr"][1] -= 1
                        villain_list.remove(villain_list[0])
                        wild_pokemon_assigner(player, evil_poke)
                break
            elif user_input == "0":
                d_print(random.choice(leave_chat_line) + "\n")
                break
            else:
                print(random.choice(invalid_selection_line))



def villain_gen() -> list:
    """
    Generates a list of villains
    :return: list of villains
    """
    villain_1 = Human("Lady Gaga", "grunt")
    villain_2 = Human("Zandaya", "grunt")
    villain_3 = Human("Beyonce", "manager")
    villain_4 = Human("P Diddy", "manager")
    villain_5 = Human("Taylor Swift", "manager")
    villain_6 = Human("Elon Musk", "exec")
    villain_7 = Human("Sydney Sweeney", "exec")
    villain_8 = Human("Ed Sheeran", "exec")
    villain_human_list = [villain_1, villain_2, villain_3, villain_4, villain_5, villain_6, villain_7, villain_8]
    return villain_human_list



def character_creator():
    """
    Creates the player and assigns them their first Pokemon
    :return:
    """
    player_name = input("Enter Your Name: ")
    player = Human(str(player_name), "player")
    d_print(f"Welcome, {player.name}.\n")
    print("""Select your partner Pokemon:
    1. Venusaur
    2. Charizard
    3. Blastoise
    """)
    while True:
        while True:
            no_select = input("Choose your starter: ")
            try:
                test = int(no_select)
                break
            except ValueError:
                print("Invalid input")
        if int(no_select) == 1:
            poke_select = all_pokemon_list.Venusaur
            d_print(f"You chose {poke_select.name}.\n")
            player.team.append(poke_select)
            d_print(f"{player.team[0].name} has been added to your party\n")
            break
        elif int(no_select) == 2:
            poke_select = all_pokemon_list.Charizard
            d_print(f"You chose {poke_select.name}.\n")
            player.team.append(poke_select)
            d_print(f"{player.team[0].name} have been added to your party\n")
            break
        elif int(no_select) == 3:
            poke_select = all_pokemon_list.Blastoise
            d_print(f"You chose {poke_select.name}.\n")
            player.team.append(poke_select)
            d_print(f"{player.team[0].name} have been added to your party\n")
            break
        else:
            print("Invalid selection")
            continue
    return player



def tutorial(player):
    """
    Tutorial scenario to be run at the beginning of the game after character_creator
    :param player:
    :return:
    """
    print("=" * 100)
    print("")
    d_print(f"""News Anchor: This just in, 8 airports around the world have been
reported to being attacked by a terrorist organisation. We dont know their
motives but the international police have apprehended a 23 year old former 
Pokemon Champion, {player.name}, now stripped of their title, suspected to
be the criminal mastermind behind these attacks.\n""")
    print("")
    d_print(f"""News Anchor: {player.name}'s PC has been disabled, and their Pokemon
confiscated. Police found a device that lets a trainer steal another trainer's 
Pokemon, called a 'Snag Em' gear, and  will begin interroga... wait! What's this? 
I've just received a report that a {player.team[0].name} just burst out of its 
Pokeball in the police department where {player.name} is being held.\n""")
    # SLEEP
    print("")
    d_print("""You escaped the detention center with only one Pokemon in your 
party and the Snag Em gear.\n""")
    #SLEEP
    print("")
    input("--Press Enter to continue--")
    print("=" * 100)
    print()
    d_print("""You somehow made it to the airport. It's empty, everyone had been
evacuated due to the terrorist threats. They upped the the security, but you 
were able to make it past most of the guards. If only you could get to your
plane then you would be able to...\n""")
    print("")
    time.sleep(1)
    print("Police Officer Jeffrey Dahmer: HOLD IT RIGHT THERE!!!")
    time.sleep(3)
    print("")
    d_print("Oh no...\n")
    print()
    time.sleep(1)
    input("--Press Enter to continue--")
    print("")
    d_print(f"""Dahmer: {player.name}, you are under arrest! Unlike other criminals
like you, I'm not playing by the rules. I won't accept a challenge in a game
of Poker, or Russian Roulette. Don't bother with the command /HELP either,
that's only useful once you played past the tutorial.\n""")
    print()
    d_print("How will you respond?\n")
    print("""1. Challenge the Police Officer Jeffrey Dahmer to a Pokemon Battle.
2. Tell Dahmer that he is legally obligated to battle you before arresting you.
3. He's a cop, he is probably crooked anyway, so as a criminal, he has moral 
obligations to comply with the criminal code of conduct but hes so crooked, he 
probably doesn't care.""")
    input("Select your choice: ")
    d_print("""\nDahmer: Dont underestimate me, I am aware that when battling, 
that my command to my Pokemon is case sensitive, or my Pokemon will get confused 
and freeze.\n""")
    time.sleep(2)
    print("=" * 100 + "\n")
    trainer_battle(player, Dahmer)
    if len(player.team) > 0:
        d_print("""Dahmer: If I had more Pokemon, I could have swapped out 
Pokemon by using the SWAP command when it was my turn.\n""")
    all_poke_heal(player)
    print()
    d_print("=" * 100 + "\n")
    print()
    d_print("""You quickly make your way to your airplane, the runway is empty
so you easily took off without worrying about collision with another
plane in the area.\n""")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # USE DUY'S FLIGHT ANIMATION
    airport_ani("Helsinki Vantaa Airport")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("=" * 100)
    print("\n")
    print("-beep beep-")
    d_print(f"""Ed Sheeran: Hey man, I saw what happened to you on the news, this
is so unfair. I think you should lay low for now, don't draw any 
attention to yourself and go into hiding.\n-bzz- *click*""")
    print("\n")
    d_print("""I guess he got cut off.. You can either take your friend's 
advice, or... you can clear your name and defeat all 8 terrorists scattered
throughout the world. Surely, if you defeat all 8 of them, you will be 
pardoned of all misunderstandings.\n""")
    print("=" * 100 + "\n")
    time.sleep(2)



def arceus_encounter():
    """
    Used for when the player triggers an Arceus encounter after playing
    Russian Roulette 2 times.
    :return: None
    """
    if Arceus not in wild_poke and Arceus not in player.team and "Sinful Transgression" in player_achv:
        wild_arceus_battle(player.team[0], player, arceus_list)
        achv_dict["defeat god"][1] -= 1



def poke_stat_options(player):
    """
    A function to run when the player opens the Pokemon & Player Stats Menu
    :param player:
    :return:
    """
    d_print("Press Enter to Continue or Enter \"RELEASE\" to select a Pokemon to release.\n")
    choice = input("Enter your choice: ")
    if choice == "RELEASE":
        print("Which Pokemon do you want to release?")
        release = input("Select your choice: ")
        print("""Are you sure?""")
        print("""1. Yes
2. No""")
        sure = input("Select your choice: ")
        try:
            test = player.team[int(release) - 1]
            if player.team[int(release) - 1] in player.team and sure == "1":
                d_print(f"{player.team[int(release) -1].name} was released into the wild. Goodbye, friend.\n")
                if "Father's Blessing" not in player_achv and player.team[int(release) -1] == Arceus:
                    achv_dict["free god"][1] -= 1
                wild_poke.append(player.team[int(release) - 1])
                player.team.remove(player.team[int(release) - 1])
        except ValueError:
            print("Invalid Input")



def villain_assign_randomly(airport_list,villain_list):
    villain_list=villain_gen()
    villain_airport=None
    chance_of_villain=0.5
    villain_randomize={airport['ident']:None for airport in airport_list}
    if airport_list and random.random()<chance_of_villain:
        villain_airport=random.choice(airport_list)
        villain_randomize[villain_airport['ident']]=villain_list[0]
    return villain_airport,villain_randomize



def main_mechanics():
    # print(b)
    global lat,longi

    airport_list=radar(lat,longi,ident=b)
    while True:
        villain_airport,villain_randomize=villain_assign_randomly(airport_list,villain_list=None)
        #{here should be the randomizer for villains}
        # villain_list=villain_gen()
        # #this will just assign the chance of villain being there
        # villain_airport=None
        # chance_of_villain=0.5 #50%chance of villain being there
        # villain_randomize={airport['ident']:None for airport in airport_list}
        # if airport_list and random.random()<chance_of_villain:
        #     villain_airport=random.choice(airport_list)
        #     villain_randomize[villain_airport['ident']]=villain_list[0]

        print("NEARBY AIRPORTS:\n")
        for i, item in enumerate(airport_list,start=1):
            list_of_airports=f"{i} . [{item['ident']}] {item['name']}, {item['airport_name']} [{item['continent']}]"

            if villain_airport and item ==villain_airport:
                play_sound("anamoly.mp3")  # correct

                blip_line("\033[31m    ANOMALY DETECTED \033[0m")
                list_of_airports=f"\033[31m{list_of_airports} \033[0m"
                # villain_yn = True

            print(list_of_airports)
            time.sleep(0.5)
        print('0 . Free Flight')


        first_value=(input("\nPress the given corresponding number you want to travel: "))

        if first_value=="":
            print("enter the valid choice")
            play_ping()
            continue
        if not first_value.isdigit():
            print('Please enter a valid choice\n\n')
            play_ping()
            time.sleep(1)
            continue

        value=int(first_value)

        if value==0:

            while True:
                dist_input = input("enter the distance in km: ")
                deg_input = input("enter the direction in degree: ")

                # Check for empty input first
                if not dist_input or not deg_input:
                    play_ping()
                    print("Invalid choice: fields cannot be empty.\n")
                    continue  # ask again

                try:
                    distance = float(dist_input)
                    degree = float(deg_input)
                    break  # success, exit loop
                except ValueError:
                    play_ping()
                    print("Invalid choice: must be a number, try again.\n")

            # Once we’re out of the loop, both distance and degree are valid floats
            # Duy's Loading Animation
            loading_ani()
            new_airport_list = free_flight(lat, longi, distance, degree, ident=b)
            if new_airport_list:
                airport_list = new_airport_list
                villain_airport, villain_randomize = villain_assign_randomly(airport_list, villain_list=None)


        elif 1<=value<=len(airport_list):
            # Animation to Fly to the location
            animation_flying()
            airport=airport_list[value-1]
            lat1=float(airport['latitude'])
            lon1=float(airport['longitude'])

            current_location(lat1,lon1)
            lat = lat1
            longi = lon1
            airport_list=radar(lat1,lon1,ident=airport['ident'])
            has_villain = (villain_randomize.get(airport['ident']))  # assumes value is None/False if no villain

            return "VILLAIN" if has_villain else "SAFE", airport
        else:
            play_ping()
            print("Not a valid choice 😡")





def second_menu(input_sec, player):
    """Part of the main menu"""
    choice = str(input_sec).strip().casefold()
    if choice == "a" or choice.casefold() == "menu":
        print("=" * 100)
        print("""
1. Help
2. Cheats
0. Exit""")
        a_menu = input("Select your choice: ")
        if a_menu == "1":
            print("Your objective is to fly around the world looking for villains to defeat.")
            print("If there are not anomolies in your area, try free flight. Don't fly too far in one go.")
            print("When you detect an anomoly fly to that location, then choose to ladnd there.")
            print("Defeat all 8 villains to win the game. If you are out of Pokemon, you lose the game.")
            print("You can heal your Pokemon with medicine from your bag.")
            print("You may only carry 6 Pokemon at one time, you do not have access to a PC to store them.")
        elif a_menu == "2":
            print("Enter: PAYDAY to add 'Meowth' to your team in the main user interface")
            print("Enter: PAYDAY to add 'I choose you!' to your team in the main user interface")
        print("=" * 100)
        if a_menu.casefold() == "exit":
            return "exit"
        return None
    elif choice == "b" or choice.casefold() == "bag":
        print("=" * 100)
        print("1. Medicine")
        print("2. Photograph")
        print("3. Gun")
        print("0. Exit")
        choice = input("Select an Item: ")
        if choice == "1":
            all_poke_heal(player)
            d_print("You've fully restored all your Pokemon to full health!\n")

        elif choice == "2":
            d_print("""Its a photo of you and your best friend from childhood. He's a
famous pop star now a days, Ed Sheeran. Wonder what he is up to right now.\n""")

        elif choice == "3":
            d_print("Things arent that bad yet.\n")
        input("Press Enter to continue")
        print("=" * 100)
        return None
    elif choice == "c" or choice.casefold() == "stats":
        print("=" * 100)
        print()
        print(f"Player Name: {player.name}")
        print("Airplane HP: " + str(player.health) + "/300")
        print("Fuel: " + str(player.fuel) + "/100")
        print()
        print("Pokemon List:")
        for index, pokemon in enumerate(player.team):
            print(f"{index + 1}. {pokemon.name} "
                  f"[{pokemon.health}/{pokemon.max_health}]"
                  f" - Attacks: [{pokemon.atk_1:^16}] [{pokemon.atk_2:^16}]"
                  f" [{pokemon.atk_3:^16}] [{pokemon.atk_4:^16}]")
        poke_stat_options(player)
        print("=" * 100)
        return None
    elif choice == "d" or choice.casefold() == "achievements":
        print("=" * 100)
        if len(player_achv) == 0:
            print("You have not unlocked any achievements.")
        for index, achv in enumerate(player_achv):
            print(f"{index + 1}. {achv}")
        input("Press Enter to continue")
        print("=" * 100)
        return None
    elif input_sec == "PAYDAY" and Meowth not in player.team:
        print("=" * 100)
        print("[YOU RECEIVED MEOWTH]") # Saved for later MIGHT REMOVE
        if len(player.team) == 6:
            into_team(player, None, Meowth)
        else:
            wild_capture(Meowth, player)
        input("Press Enter to continue")
        print("=" * 100)
        return None
    elif input_sec == "I choose you!" and Pikachu not in player.team:
        print("=" * 100)
        print("[YOU RECEIVED PIKACHU]") # Saved for later MIGHT REMOVE
        if len(player.team) == 6:
            into_team(player, None, Pikachu)
        else:
            wild_capture(Pikachu, player)
        input("Press Enter to continue")
        print("=" * 100)
        return None
    else:
        print("=" * 100)
        print("Please enter a valid input.")
        input("Press Enter to continue")
        print("=" * 100)
        return None



def latitude_check(latitude: float) -> str:
    """ Checks the latitude then returns N or S depending on the degree"""
    if latitude >= 0:
        return "N"
    else:
        return "S"



def longitude_check(longitude: float) -> str:
    """Checks the longitude then returns E or W depending on the degree"""
    if longitude >= 0:
        return "E"
    else:
        return "W"



# villain_yn = "SAFE" PUT THIS BACK IF ERRORS ARISE
def travel_menu(input_travel, player, villain_status):
    """Part of the main menu, but for travelling"""
    choice = int(input_travel)
    if choice == 1:
        flight_cost()
        print("=" * 100)
        villain_yn.remove(villain_yn[0])
        output = main_mechanics()
        x = output[0]
        player_loca.remove(player_loca[0])
        player_loca.remove(player_loca[0])
        player_loca.remove(player_loca[0])
        player_loca.append(output[1]["latitude"])
        player_loca.append(output[1]["longitude"])
        player_loca.append(output[1]["airport_name"])
        villain_yn.append(x)
        all_poke_heal(player)
    elif choice == 0:
        animation_landing()
        player.fuel = 100
        all_poke_heal(player)
        airport_ani(str(player_loca[2]))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if villain_status[0] == "VILLAIN":
            villain_interaction(player, villain_list[0])
            villain_yn.remove(villain_yn[0])
            villain_yn.append("SAFE")
        else:
            arceus_encounter()
            wild_encounter_battle(player.team[0], player, wild_poke)
            villain_yn.remove(villain_yn[0])
            villain_yn.append("SAFE")
            # police_attack()
            if "Global Warming" in player_achv:
                player.health -= 20
                cop = Human("Cop", "cop")
                d_print("You noticed someone running after you, its the cops!!\n")
                d_print("Hold it right there! You're under arrest for excessive co2 discharge!\n")
                villain_interaction(player, cop)
                villain_yn.remove(villain_yn[0])
                villain_yn.append("SAFE")
                print("Now's your chance, RUN!!!")
                input("Press Enter to flee from the cops!")



    else:
        print("=" * 100)
        print("Please enter a valid input.")
        input("Press Enter to continue")
        print("=" * 100)



def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Prints out different lines of a banner created with `** on each sides`.

    :param text: Prints str inside the banner.
        An asterisk (*) will result in a row of asterisks.
        Prints out " " by default if left empty.
    :param screen_width: The width of the banner by character number.
        The width is set to 80 by default if left empty.
    :raises ValueError: if the supplied str is too long to fit the banner.
    :return:
        None
    """
    # screen_width = y # I originally used this, but you can just change it up there
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)



def death_check(): # Lose conditions #######################################################33 LOSING CONDITION DUY DUY DUY DUY DUY!!!!
    """Checks the player for losing conditions and ends the game accordingly."""
    if len(player.team) == 0:
        d_print("""You have no Pokemon left, you see a black Rayquaza in the distance.
Unfortunately for you, it seems like you are caught in it's territory.
Without any Pokemon to defend you, Rayquaza attacked you directly with 
a Hyper Beam.\n""")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        gameover()
        return True
    elif player.health <= 0:
        d_print("You've taken too much damage without recovery. Your journey ends here.")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        gameover()
        return True
    elif player.fuel <= 0:
        print("""You're out of fuel, your plane is losing altitude fast. You try to...""")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        gameover()
        return True
    else:
        return False



def main_menu(player):
    """Main menu, start this after the tutorial"""
    while True:
        achievement_check(achv_dict, player_achv)
        check = death_check()
        if len(villain_list) <= 0:
            ani_win1(10,130,135) ################Here is Win animation and you guys could modify position by x & y -> ani_win1(x,y,y2)###################################################
            break
        if check == True:
            break
        print("=" * 100)
        ap_hp = "Airplane: " + str(player.health) + "/300"
        fuel = "Fuel: " + str(player.fuel) + "/100"
        location = f"Location: [{player_loca[0]}° {latitude_check(float(player_loca[0]))}, {player_loca[1]}° {longitude_check(float(player_loca[1]))}]"
        print(f"[{ap_hp}]           [{fuel}]             [{location}]")
        print()
        print()
        print()
        print("1. Initiate Travel")
        print(f"0. Land at {player_loca[2]}")
        print("-" * 100)
        print("A. Open Menu")
        print("B. Open Bag")
        print("C. Pokemon Stats")
        print("D. Open Achievements")
        print("=" * 100)
        main_input = input("Enter choice: ")
        if main_input.isdigit():
            travel_menu(main_input, player, villain_yn)
        else:
            if second_menu(main_input, player) == "exit":
                print("-Session Ended-")
                break



#RUN DUY'S INTRO HERE

intro()
print("\n\n\n\n\n\n")
# LIST OF LISTS AND STUFF WE WANT TO START OUT WITH
arceus_list = [Arceus]
wild_poke = []
evil_poke = []
player_achv = []
player_loca = ["60.3172", "24.9633", "Helsinki Vantaa Airport"]
villain_list = villain_gen()
# Meeri = Human("Meeri", "grunt") # Test
# villain_list = [Meeri] # Test
Dahmer = Human("Police Officer Dahmer", "cop")
villain_yn = ["SAFE"]
default_location="EFHK"
lat = float(store_data()[default_location]["latitude"])
longi = float(store_data()[default_location]["longitude"])
b=current_location(lat,longi,silent=False)
# Game Starts Here
player = character_creator()
wild_pokemon_assigner(player, evil_poke)
tutorial(player)
animation_flying()
main_menu(player)


