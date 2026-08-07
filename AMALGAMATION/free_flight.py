import sys

from fetching_database import store_data
from used_functions import current_location
from used_functions import calculate_coordinates
from used_functions import radar



def free_flight(lat,lon,distance,degree,ident):

    # distance=int(input("enter the distance: "))
    # degree=int(input("enter the degree: "))
    # data=store_data()
    # for items in data:
    #     lat=data[items]['latitude']
    #     lon=data[items]['longitude']
    #     # print(lat,lon)
    a=calculate_coordinates(lat,lon,distance,degree)
    lat1=a[0]
    lon1=a[1]
    # print(lat1,lon1)
    # new_ident=current_location(lat1,lon1,silent=True)
    b=radar(lat1,lon1)
    # print(b)
    nearby_airports=[]

    if b:
        for items in b:
            if items['ident']!=ident: # and items['ident']!=default_location:
                nearby_airports.append(items)
    else:
        print("\033[31mThere are no airports at that location, unless you want to land in the ocean... 🙁\033[0m")
        print("\033[32m Try Again 😉\033[0m ")
    # print(f'NEARBY AIRPORTS TO LAND')
    # for i, item in enumerate(nearby_airports,start=1):
    #     print(f'{i}. [{item["ident"]}] {item['name']}, {item['airport_name']} [{item['continent']}]\n')
    # for i, item in enumerate(nearby_airports,start=1):
    #     list_of_airports=f"{i} . [{item['ident']}] {item['name']}, {item['airport_name']} [{item['continent']}]"
    #     print(list_of_airports)

    # print(f'0. Free flight')
    #
    return nearby_airports


















