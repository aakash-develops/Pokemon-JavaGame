import random
import pokedex_player
from SAM_TEST.pokedex_player import Raging_Bolt
from attack_dict import attack_dict
from npc_attack_dict import npc_attack_dict
from type_chart_factor import type_bonus_dict

def opo_bonus(opponent, n: int):
    """
    Multiplies the opponent's health by n number of time.
    :param opponent: Pokemon whose stat is to be multiplied
    :param n: number of times the stat is multiplied by
    :return:
    """
    opponent.health *= n
    opponent.max_health *= n




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
        print(f"{self.name} used {key} on {player_2.name}! [{dmg_out}]")
        if float(type_bonus(key, player_2)) > 1.5:
            print("Its super effective!")
        elif float(type_bonus(key, player_2)) == 0:
            print(f"{player_2.name} is immune to {key}")
        elif float(type_bonus(key, player_2)) < 1:
            print("Its not very effective!")
        # + str(player_2.health) + " " + str(dmg_out))


def type_display(poke):
    if poke.type_2 != None:
        output = f"[{poke.type_1:^10}][{poke.type_2:^10}]"
    else:
        output = f"[{poke.type_1:^10}]"

    return output



def poke_hp_bar(pokemon_a):
    c_hp = int(pokemon_a.health)
    f_hp = int(pokemon_a.max_health)
    bar ="■" * (round( c_hp / f_hp * 20))
    output = ("[" + f"{bar:<20}]" )
    return output



def alive_team(teammates, exclude=None):
    alive_members = [p for p in teammates if p.health > 0 and p is not exclude]
    return alive_members



def choose_switch_from_team(teammates, exclude = None, prompt =
"Who do you want to swap to?"):
    options = alive_team(teammates, exclude=exclude)
    if not options:
        return None
    print(prompt)
    for index, pokemon_a in enumerate(options, start=1):
        print(f"{index}. {pokemon_a.name} [HP: {max(pokemon_a.health,0)} / {pokemon_a.max_health}] (Lv. {pokemon_a.lvl})")
    while True:
        try:
            pick = int(input("Send out: "))
            if 1 <= pick <= len(options):
                return options[pick - 1]
        except ValueError:
            pass
        print("Invalid choice. Try again.")



def your_battle_turn(your_mon, opo_mon):
    your_att = input("Select your attack: ")
    if your_att == "SWAP":
        new_mon = swap_out(your_mon, opo_mon)
        if new_mon is None:
            print("No other healthy Pokemon!!")
        else:
            print(f"{your_mon.name} come back! Go, {new_mon.name}!")
            return "switch", new_mon
    # your_att = "Flamethrower"
    if your_att in your_mon.att_key:
        your_mon.attack(opo_mon, your_att)
        input("Press Enter to continue")
        return "no switch"
    elif your_att != "SWAP" and your_att not in your_mon.att_key:
        print(f"You fumbled your command, {your_mon.name} froze in confusion!")
        input("Press Enter to continue")
        return "no switch"
    else:
        input("Press Enter to continue")
        return "no switch"



def swap_out(current, opponent):
    return choose_switch_from_team(poke_team, exclude = current, prompt = "Who do you want to swap to?")



def pokemon_battle(your_mon, opo_mon):
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
                battle_input = your_battle_turn(your_mon, opo_mon)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]
            if opo_mon.health > 0:
                print("Opponent's turn!")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
        else:
            if opo_mon.health > 0:
                print("Your opponent is fast!")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
            if your_mon.health > 0:
                battle_input = your_battle_turn(your_mon, opo_mon)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]

        if your_mon.health <= 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{"0":<38}HP:{opo_hp_str}")
            print(f"Your {your_mon.name} fainted!")
            replacement = choose_switch_from_team(poke_team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
            if replacement is None:
                print("You have no Pokemon left..")
                print("That's okay, you can get em next time!")
                break
            print(f"Go, {replacement.name}!")
            your_mon = replacement
        elif your_mon.health > 0 and opo_mon.health < 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{your_hp_str:<38}HP:0/{opo_mon.max_health}")
            print("The opposing Pokémon is knocked out!")
            print("You won!")
            your_mon.lvl += 1


def type_bonus(key: str, defender: Pokemon) -> float:
    """
    Checks the attack type, and the defending Pokemon types to determine
    damage bonuses or reductions based on the type chart.
    :param key: dictionary key for the attack being used
    :param defender: the defending Pokemon
    :return:
    """
    if str(attack_dict[key][0]) + str(defender.type_1) in type_bonus_dict:
        bonus_1 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)]
        if str(attack_dict[key][0]) + str(defender.type_2) in type_bonus_dict:
            bonus_2 = type_bonus_dict[str(attack_dict[key][0]) +
            str(defender.type_1)] * type_bonus_dict[str(attack_dict[key][0])
            + str(defender.type_2)]
            return bonus_2
        return bonus_1
    else:
        return 1.0

import random

attack_dict = {
    "DELETE": ("Dark", 9999),
    "Judgment": ("All", 9999),
    "Seismic Toss": ("Fighting", 95),
    "Thunder": ("Electric", 110),
    "Thunderclap": ("Electric", 110),
    "Crunch": ("Dark", 80),
    "Stomping Tantrum": ("Ground", 75),
    "Magical Leaf": ("Grass", 80),
    "Flamethrower": ("Fire", 95),
    "Dragon Claw": ("Dragon", 80),
    "Hydropump": ("Water", 120),
    "Draco Meteor": ("Dragon", 130),
    "Moonblast": ("Fairy", 95),
    "Bitter Blade": ("Fire", 90),
    "Close Combat": ("Fighting", 120),
    "Phantom Force": ("Ghost", 90),
    "Outrage": ("Dragon", 120),
    "Aura Sphere": ("Fighting", 80),
    "Trump Card": ("Normal", random.randint(50, 175)),
    "Ominous Wind": ("Ghost", 75),
    "Sludge Bomb": ("Poison", 90),
    "Solar Blade": ("Grass", 125),
    "X-Scissor": ("Bug", 80),
    "Psychic Noise": ("Psychic", 75),
    "Expanding Force": ("Psychic", 80),
    "Bullet Punch": ("Steel", 95),
    "Flash Cannon": ("Steel", 80),
    "Earthquake": ("Ground", 100),
    "Roar of Time": ("Dragon", 150),
    "Shadow Ball": ("Ghost", 80),
    "Psystrike": ("Psychic", 100),
    "Blaze Kick": ("Fire", 85),
    "Sky Uppercut": ("Fighting", 85),
    "Stone Edge": ("Rock", 85),
    "Thunderbolt": ("Electric", 90),
    "Ice Beam": ("Ice", 95),
    "Rock Slide": ("Rock", 75),
    "Scratch": ("Normal", 40),
    "Aerial Ace": ("Flying", 90),
    "Thunder Punch": ("Electric", 75),
    "Psychic": ("Psychic", 90),
    "Surf": ("Water", 90),
    "Ice Punch": ("Ice", 75),
    "Flare Blitz": ("Fire", 120),
    "High Horsepower": ("Ground", 95),
    "Overheat": ("Fire", 130),
    "Solar Beam": ("Grass", 120),
    "Shadow Claw": ("Ghost", 70),
    "Rock Tomb": ("Rock", 70),
    "Hyper Beam": ("Normal", 150),
    "Iron Tail": ("Steel", 100),
    "Slash": ("Normal", 70),
}

npc_attack_dict = [
    "Flamethrower",
    "Dragon Claw",
    "Hydropump",
    "Draco Meteor",
    "Earthquake",
    "Roar of Time",
    "Shadow Ball",
    "Psystrike",
    "Blaze Kick",
    "Sky Uppercut",
    "Stone Edge",
    "Ice Beam",
    "Rock Slide",
    "Scratch",
    "Aerial Ace",
    "Thunder Punch",
    "Ice Punch",
    "Flare Blitz",
    "Overheat",
    "Solar Beam",
    "Shadow Claw",
    "Hyper Beam",
    "Iron Tail",
    "Slash"
]

import random
from attack_dict import attack_dict
from npc_attack_dict import npc_attack_dict
from type_chart_factor import type_bonus_dict


def type_bonus(key, defender):
    if str(attack_dict[key][0]) + str(defender.type_1) in type_bonus_dict:
        bonus_1 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)]
        if str(attack_dict[key][0]) + str(defender.type_2) in type_bonus_dict:
            bonus_2 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)] * type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_2)]
            return bonus_2
        return bonus_1
    else:
        return 1




type_bonus_dict = {
                    "NormalNormal": 1,
                    "NormalFire": 1,
                    "NormalWater": 1,
                    "NormalGrass": 1,
                    "NormalElectric": 1,
                    "NormalIce": 1,
                    "NormalFighting": 1,
                    "NormalPoison": 1,
                    "NormalGround": 1,
                    "NormalFlying": 1,
                    "NormalPsychic": 1,
                    "NormalBug": 1,
                    "NormalRock": 0.5,
                    "NormalGhost": 0,
                    "NormalDragon": 1,
                    "NormalDark": 1,
                    "NormalSteel": 0.5,
                    "NormalFairy": 1,
                    "FireNormal": 1,
                    "FireFire": 0.5,
                    "FireWater": 0.5,
                    "FireGrass": 2,
                    "FireElectric": 1,
                    "FireIce": 2,
                    "FireFighting": 1,
                    "FirePoison": 1,
                    "FireGround": 1,
                    "FireFlying": 1,
                    "FirePsychic": 1,
                    "FireBug": 2,
                    "FireRock": 0.5,
                    "FireGhost": 1,
                    "FireDragon": 0.5,
                    "FireDark": 1,
                    "FireSteel": 2,
                    "FireFairy": 1,
                    "WaterNormal": 1,
                    "WaterFire": 2,
                    "WaterWater": 0.5,
                    "WaterGrass": 0.5,
                    "WaterElectric": 1,
                    "WaterIce": 1,
                    "WaterFighting": 1,
                    "WaterPoison": 1,
                    "WaterGround": 2,
                    "WaterFlying": 1,
                    "WaterPsychic": 1,
                    "WaterBug": 1,
                    "WaterRock": 2,
                    "WaterGhost": 1,
                    "WaterDragon": 0.5,
                    "WaterDark": 1,
                    "WaterSteel": 1,
                    "WaterFairy": 1,
                    "GrassNormal": 1,
                    "GrassFire": 0.5,
                    "GrassWater": 2,
                    "GrassGrass": 0.5,
                    "GrassElectric": 1,
                    "GrassIce": 1,
                    "GrassFighting": 1,
                    "GrassPoison": 0.5,
                    "GrassGround": 2,
                    "GrassFlying": 0.5,
                    "GrassPsychic": 1,
                    "GrassBug": 0.5,
                    "GrassRock": 2,
                    "GrassGhost": 1,
                    "GrassDragon": 0.5,
                    "GrassDark": 1,
                    "GrassSteel": 0.5,
                    "GrassFairy": 1,
                    "ElectricNormal": 1,
                    "ElectricFire": 1,
                    "ElectricWater": 2,
                    "ElectricGrass": 0.5,
                    "ElectricElectric": 0.5,
                    "ElectricIce": 1,
                    "ElectricFighting": 1,
                    "ElectricPoison": 1,
                    "ElectricGround": 0,
                    "ElectricFlying": 2,
                    "ElectricPsychic": 1,
                    "ElectricBug": 1,
                    "ElectricRock": 1,
                    "ElectricGhost": 1,
                    "ElectricDragon": 0.5,
                    "ElectricDark": 1,
                    "ElectricSteel": 1,
                    "ElectricFairy": 1,
                    "IceNormal": 1,
                    "IceFire": 0.5,
                    "IceWater": 0.5,
                    "IceGrass": 2,
                    "IceElectric": 1,
                    "IceIce": 0.5,
                    "IceFighting": 1,
                    "IcePoison": 1,
                    "IceGround": 2,
                    "IceFlying": 2,
                    "IcePsychic": 1,
                    "IceBug": 1,
                    "IceRock": 1,
                    "IceGhost": 1,
                    "IceDragon": 2,
                    "IceDark": 1,
                    "IceSteel": 0.5,
                    "IceFairy": 1,
                    "FightingNormal": 2,
                    "FightingFire": 1,
                    "FightingWater": 1,
                    "FightingGrass": 1,
                    "FightingElectric": 1,
                    "FightingIce": 2,
                    "FightingFighting": 1,
                    "FightingPoison": 0.5,
                    "FightingGround": 1,
                    "FightingFlying": 0.5,
                    "FightingPsychic": 0.5,
                    "FightingBug": 0.5,
                    "FightingRock": 2,
                    "FightingGhost": 0,
                    "FightingDragon": 1,
                    "FightingDark": 2,
                    "FightingSteel": 2,
                    "FightingFairy": 0.5,
                    "PoisonNormal": 1,
                    "PoisonFire": 1,
                    "PoisonWater": 1,
                    "PoisonGrass": 2,
                    "PoisonElectric": 1,
                    "PoisonIce": 1,
                    "PoisonFighting": 1,
                    "PoisonPoison": 0.5,
                    "PoisonGround": 0.5,
                    "PoisonFlying": 1,
                    "PoisonPsychic": 1,
                    "PoisonBug": 1,
                    "PoisonRock": 0.5,
                    "PoisonGhost": 0.5,
                    "PoisonDragon": 1,
                    "PoisonDark": 1,
                    "PoisonSteel": 0,
                    "PoisonFairy": 2,
                    "GroundNormal": 1,
                    "GroundFire": 2,
                    "GroundWater": 1,
                    "GroundGrass": 0.5,
                    "GroundElectric": 2,
                    "GroundIce": 1,
                    "GroundFighting": 1,
                    "GroundPoison": 2,
                    "GroundGround": 1,
                    "GroundFlying": 0,
                    "GroundPsychic": 1,
                    "GroundBug": 0.5,
                    "GroundRock": 2,
                    "GroundGhost": 1,
                    "GroundDragon": 1,
                    "GroundDark": 1,
                    "GroundSteel": 2,
                    "GroundFairy": 1, # THIS IS WHERE I LAST LEFT OFF
                    "FlyingNormal": 1,
                    "FlyingFire": 1,
                    "FlyingWater": 1,
                    "FlyingGrass": 2,
                    "FlyingElectric": 0.5,
                    "FlyingIce": 1,
                    "FlyingFighting": 2,
                    "FlyingPoison": 1,
                    "FlyingGround": 1,
                    "FlyingFlying": 1,
                    "FlyingPsychic": 1,
                    "FlyingBug": 2,
                    "FlyingRock": 0.5,
                    "FlyingGhost": 1,
                    "FlyingDragon": 1,
                    "FlyingDark": 1,
                    "FlyingSteel": 0.5,
                    "FlyingFairy": 1,
                    "PsychicNormal": 1,
                    "PsychicFire": 1,
                    "PsychicWater": 1,
                    "PsychicGrass": 1,
                    "PsychicElectric": 1,
                    "PsychicIce": 1,
                    "PsychicFighting": 2,
                    "PsychicPoison": 2,
                    "PsychicGround": 1,
                    "PsychicFlying": 1,
                    "PsychicPsychic": 0.5,
                    "PsychicBug": 1,
                    "PsychicRock": 1,
                    "PsychicGhost": 1,
                    "PsychicDragon": 1,
                    "PsychicDark": 0,
                    "PsychicSteel": 0.5,
                    "PsychicFairy": 1,
                    "BugNormal": 1,
                    "BugFire": 0.5,
                    "BugWater": 1,
                    "BugGrass": 2,
                    "BugElectric": 1,
                    "BugIce": 1,
                    "BugFighting": 0.5,
                    "BugPoison": 0.5,
                    "BugGround": 1,
                    "BugFlying": 0.5,
                    "BugPsychic": 2,
                    "BugBug": 1,
                    "BugRock": 1,
                    "BugGhost": 0.5,
                    "BugDragon": 1,
                    "BugDark": 2,
                    "BugSteel": 0.5,
                    "BugFairy": 0.5,
                    "RockNormal": 1,
                    "RockFire": 2,
                    "RockWater": 1,
                    "RockGrass": 1,
                    "RockElectric": 1,
                    "RockIce": 2,
                    "RockFighting": 0.5,
                    "RockPoison": 1,
                    "RockGround": 0.5,
                    "RockFlying": 2,
                    "RockPsychic": 1,
                    "RockBug": 2,
                    "RockRock": 1,
                    "RockGhost": 1,
                    "RockDragon": 1,
                    "RockDark": 1,
                    "RockSteel": 0.5,
                    "RockFairy": 1,
                    "GhostNormal": 0,
                    "GhostFire": 1,
                    "GhostWater": 1,
                    "GhostGrass": 1,
                    "GhostElectric": 1,
                    "GhostIce": 1,
                    "GhostFighting": 1,
                    "GhostPoison": 1,
                    "GhostGround": 1,
                    "GhostFlying": 1,
                    "GhostPsychic": 2,
                    "GhostBug": 1,
                    "GhostRock": 1,
                    "GhostGhost": 2,
                    "GhostDragon": 1,
                    "GhostDark": 0.5,
                    "GhostSteel": 1,
                    "GhostFairy": 1,
                    "DragonNormal": 1,
                    "DragonFire": 1,
                    "DragonWater": 1,
                    "DragonGrass": 1,
                    "DragonElectric": 1,
                    "DragonIce": 1,
                    "DragonFighting": 1,
                    "DragonPoison": 1,
                    "DragonGround": 1,
                    "DragonFlying": 1,
                    "DragonPsychic": 1,
                    "DragonBug": 1,
                    "DragonRock": 1,
                    "DragonGhost": 1,
                    "DragonDragon": 2,
                    "DragonDark": 1,
                    "DragonSteel": 0.5,
                    "DragonFairy": 0,
                    "DarkNormal": 1,
                    "DarkFire": 1,
                    "DarkWater": 1,
                    "DarkGrass": 1,
                    "DarkElectric": 1,
                    "DarkIce": 1,
                    "DarkFighting": 0.5,
                    "DarkPoison": 1,
                    "DarkGround": 1,
                    "DarkFlying": 1,
                    "DarkPsychic": 2,
                    "DarkBug": 1,
                    "DarkRock": 1,
                    "DarkGhost": 2,
                    "DarkDragon": 1,
                    "DarkDark": 0.5,
                    "DarkSteel": 1,
                    "DarkFairy": 0.5,
                    "SteelNormal": 1,
                    "SteelFire": 0.5,
                    "SteelWater": 0.5,
                    "SteelGrass": 1,
                    "SteelElectric": 0.5,
                    "SteelIce": 2,
                    "SteelFighting": 1,
                    "SteelPoison": 1,
                    "SteelGround": 1,
                    "SteelFlying": 1,
                    "SteelPsychic": 1,
                    "SteelBug": 1,
                    "SteelRock": 2,
                    "SteelGhost": 1,
                    "SteelDragon": 1,
                    "SteelDark": 1,
                    "SteelSteel": 0.5,
                    "SteelFairy": 2,
                    "FairyNormal": 1,
                    "FairyFire": 0.5,
                    "FairyWater": 1,
                    "FairyGrass": 1,
                    "FairyElectric": 1,
                    "FairyIce": 1,
                    "FairyFighting": 2,
                    "FairyPoison": 0.5,
                    "FairyGround": 1,
                    "FairyFlying": 1,
                    "FairyPsychic": 1,
                    "FairyBug": 1,
                    "FairyRock": 1,
                    "FairyGhost": 1,
                    "FairyDragon": 2,
                    "FairyDark": 2,
                    "FairySteel": 0.5,
                    "FairyFairy": 1,
                    "AllNormal": 2,
                    "AllFire": 2,
                    "AllWater": 2,
                    "AllGrass": 2,
                    "AllElectric": 2,
                    "AllIce": 2,
                    "AllFighting": 2,
                    "AllPoison": 2,
                    "AllGround": 2,
                    "AllFlying": 2,
                    "AllPsychic": 2,
                    "AllBug": 2,
                    "AllRock": 2,
                    "AllGhost": 2,
                    "AllDragon": 2,
                    "AllDark": 2,
                    "AllSteel": 2,
                    "AllFairy": 2,

}
