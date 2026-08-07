from free_flight import free_flight
from used_functions import current_location, calculate_coordinates
import random
from data_function import villain_gen
from used_functions import type_with_cursor
from used_functions import store_data
from used_functions import radar
from used_functions import blip_line

from used_functions import type_with_sound


default_location="EFHK"
lat = float(store_data()[default_location]["latitude"])
longi = float(store_data()[default_location]["longitude"])
b=current_location(lat,longi,silent=False)

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
                blip_line("\033[31m    ANOMALY DETECTED \033[0m")
                list_of_airports=f"\033[31m{list_of_airports} \033[0m"

            type_with_sound(list_of_airports)
        type_with_sound('0 . Free Flight',speed=0.03)




        value=int(input("\nPress the given corresponding number you want to travel: "))
        if value==0:
            #{here should be the flying part i mean graphcal)
            distance=float(input("enter the distance in km: "))
            degree=float(input("enter the direction in degree: "))
            new_airport_list= free_flight(lat,longi,distance,degree,ident=b)
            if new_airport_list:
                airport_list=new_airport_list
                villain_airport,villain_randomize=villain_assign_randomly(airport_list,villain_list=None)

        elif 1<=value<=len(airport_list):
            #{here should be the landing part)
            airport=airport_list[value-1]
            lat1=float(airport['latitude'])
            lon1=float(airport['longitude'])
            current_location(lat1,lon1)
            airport_list=radar(lat1,lon1,ident=airport['ident'])
            break
        else:
            print("Not a valid choice 😡")
    else:
        print('goodbye')


# main_mechanics()

    #{here should be the logic where the user wants to battle or not something}

