from fetching_database import store_data
import math
import time
import sys
import warnings

# Suppress only that specific pygame pkg_resources warning
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="pygame.pkgdata"
)
def coordinates(item):
    data=store_data()
    item=input("enter the items :")
    if item in data:
        a=data[item]['latitude']
        b=data[item]['longitude']
        print(f'{item} is\n latitude: {a} \n and \n longitude: {b}')
        return (a,b)
    else:
        print("code exited because invalid input")
        return None

def details(item):
    data=store_data()
    if item in data and data[item]["type_airport"]=="small_airport":
        print(data[item])
        print(data[item]["name"],data[item]["continent"],data[item]["country"],data[item]["gps_code"])


def country():
    countries=[]
    count=0
    data=store_data()
    for item  in data:
        if data[item]['country'] not in countries:
            countries.append(data[item]['country'])
            print(data[item]["continent"])

            count+=1
    print(countries)
    print(count)

def calculate_distance(lat1,long1,lat2,long2):
    radius=6371 #earth radius

    #converting the latitude and longitude to radians
    rad_lat1=math.radians(lat1)
    rad_long1=math.radians(long1)
    rad_lat2=math.radians(lat2)
    rad_long2=math.radians(long2)
    new_lat=math.radians(lat2-lat1)
    new_long=math.radians(long2-long1)
    #now using the haversine formula to calculate distance
    a = math.sin(new_lat / 2) ** 2 + math.cos(rad_lat1) * math.cos(rad_lat2) * math.sin(new_long / 2) ** 2
    c=2*math.asin(math.sqrt(a))
    distance=radius*c
    print(distance)
    return distance

def calculate_coordinates(lat,long1,distance,degree):
    radius=6371 #earth radius in km

    rad_lat=math.radians(lat)
    rad_long=math.radians(long1)
    rad_degree=math.radians(degree)

    #angular distance
    a_distance=distance/radius

    latitude=math.asin(math.sin(rad_lat)*math.cos(a_distance)+math.cos(rad_lat)*math.sin(a_distance)*math.cos(rad_degree))
    longitude= rad_long+ math.atan2(math.sin(rad_degree)*math.sin(a_distance)*math.cos(rad_lat),math.cos(a_distance)-math.sin(rad_lat)*math.sin(latitude))

    latitude= math.degrees(latitude)
    longitude= math.degrees(longitude)
    # print(latitude,longitude)
    return (latitude,longitude)


def current_location(lat,longi,silent=False):
    data=store_data()
    tolerance=0.002 #this generally helps with the small difference
    for item in data:
        if (abs(float(data[item]['latitude'])-lat))<=tolerance and (abs(float(data[item]['longitude'])-longi))<=tolerance:

            a=data[item]["name"]
            b=data[item]['continent']
            c=data[item]['gps_code']
            d=data[item]['ident']
            e=data[item]['airport_name']
            if not silent: #small changes because it kept printing
                if [e]:
                   typewriter(    f'\nYour Current Location is :\n\033[32m[AIRPORT NAME]: {e}\033[0m \n[CONTINENT]: {b}\n[COUNTRY]: {a}\n[gps_code]: {c}\n')
            else:
                    print(f'\nYour Current Location is :\n\033[32m[AIRPORT NAME]: {e}\033[0m \n[CONTINENT]: {b}\n[COUNTRY]: {a}\n[gps_code]: {c}\n')
            return d

    if not silent:
        print("Location not found")
    return None



def radar(lat,lon,radius_km=500,ident=None):
    data=store_data()
    nearby_airports={}

    lat_diff=radius_km/111
    lon_diff=radius_km/(111*math.cos(math.radians(lat)))

    for item in data:
        lat1=float(data[item]['latitude'])
        lon1=float(data[item]['longitude'])


        if(abs(lat1-lat)<=lat_diff) and (abs(lon1-lon)<=lon_diff):
            nearby_airports[item]=data[item]
    a=[]
    for items in nearby_airports:
        if nearby_airports[items]['type_airport']=="large_airport" and items!=ident:
            a.append(nearby_airports[items])
    return a


import sys
import time

def type_with_cursor(text, speed=0.01, cursor='_', blip_speed=0.2, blip_times=1):
    """
    Prints text one character at a time with a blinking cursor effect at the end.

    Parameters:
    - text: str, the string to print
    - speed: float, delay between characters
    - cursor: str, the character to blink at the end
    - blip_speed: float, how fast the cursor blinks
    - blip_times: int, number of times the cursor blinks after finishing text
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

    # Blinking cursor after finishing
    for _ in range(blip_times):
        print(cursor, end='', flush=True)
        time.sleep(blip_speed)
        print('\b \b', end='', flush=True)  # erase the cursor
        time.sleep(blip_speed)
    print()  # move to the next line

def blip_line(text, blip_speed=0.3):
    """
    Makes an entire line of text blink twice (appear and disappear).

    Parameters:
    - text: str, the line to blip
    - blip_speed: float, time in seconds for each blink
    """
    for _ in range(2):  # blink exactly twice
        print(text, end='\r', flush=True)  # show text
        time.sleep(blip_speed)
        print(' ' * len(text), end='\r', flush=True)  # erase text
        time.sleep(blip_speed)
    print(text)



#
#
# def line_by_line_print(lines, pause=1.0):
#     """
#     Prints each line immediately, waits for a pause, then prints the next line.
#
#     Parameters:
#     - lines: list of str, each string is a full line to print
#     - pause: float, seconds to wait before printing the next line
#     """
#     for line in lines:
#         print(line)       # full line prints instantly
#         time.sleep(pause)
#
#
# import sys, time, random, re
# import pygame
# import platform
#
# # Initialize pygame mixer
# pygame.mixer.init()
# click_sound = pygame.mixer.Sound("click.wav")  # Typing sound
#
# def play_ping(times=2, delay_ms=100):
#     """
#     Plays a short ping to highlight status/current location.
#     Cross-platform: winsound for Windows, ASCII bell for others.
#     times: how many times to repeat
#     delay_ms: delay between pings in milliseconds
#     """
#     if platform.system() == "Windows":
#         import winsound
#         for _ in range(times):
#             winsound.Beep(1000, 150)  # 1000 Hz, 150 ms
#             time.sleep(delay_ms / 1000)
#     else:
#         for _ in range(times):
#             print('\a', end='', flush=True)
#             time.sleep(delay_ms / 1000)
#
# def typewriter(text):
#     """
#     Drop-in replacement for print() with typewriter effect.
#     - Plays typing click per character
#     - Plays a double ping at the end
#     """
#     min_delay = 0.05
#     max_delay = 0.1
#     cursor = '|'
#
#     ansi_escape = re.compile(r'(\033\[[0-9;]*m)')
#     parts = ansi_escape.split(text)
#
#     for part in parts:
#         if ansi_escape.match(part):
#             sys.stdout.write(part)
#             sys.stdout.flush()
#         else:
#             for char in part:
#                 sys.stdout.write(f"{char}{cursor}")
#                 sys.stdout.flush()
#                 try:
#                     click_sound.play()
#                 except Exception:
#                     pass
#                 time.sleep(random.uniform(min_delay, max_delay))
#                 sys.stdout.write('\b')
#                 sys.stdout.flush()
#
#     print()  # newline at the end
#     play_ping(times=2, delay_ms=100)  # double ping at the end
#
# # Example usage:
# location_text = (
#     "Your current location is:\n"
#     "Airport name: ALSKDFJLASDKF, Continent: EU, Country: Finland, GPS code: EFHK"
# )
#
#
#
#
#
#
#
#
import pygame

# Initialize the mixer once
pygame.mixer.init()

def play_sound(file_path="sound.mp3"):
    """Play an MP3 file."""
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()





import sys, time, random, re, pygame, platform, os, builtins


# ---------------- SOUND SETUP ----------------
def play_ping(times=2, delay_ms=100):
    """Plays a ping sound or terminal beep."""
    if platform.system() == "Windows":
        import winsound
        for _ in range(times):
            winsound.Beep(1000, 150)
            time.sleep(delay_ms / 1000)
    else:
        for _ in range(times):
            print('\a', end='', flush=True)
            time.sleep(delay_ms / 1000)


pygame.mixer.init()
click_sound = pygame.mixer.Sound("click.wav")

# def play_ping(times=2, delay_ms=100):
#     """Plays a ping sound or terminal beep."""
#     if platform.system() == "Windows":
#         import winsound
#         for _ in range(times):
#             winsound.Beep(1000, 150)
#             time.sleep(delay_ms / 1000)
#     else:
#         for _ in range(times):
#             print('\a', end='', flush=True)
#             time.sleep(delay_ms / 1000)

# ---------------- TYPEWRITER EFFECT ----------------
def typewriter(text, min_delay=0.05, max_delay=0.1, cursor='|'):
    """Fully blocking typewriter print with typing sound and ping at the end."""
    ansi_escape = re.compile(r'(\033\[[0-9;]*m)')
    parts = ansi_escape.split(text)

    for part in parts:
        if ansi_escape.match(part):
            sys.stdout.write(part)
            sys.stdout.flush()
        else:
            for char in part:
                sys.stdout.write(f"{char}{cursor}")
                sys.stdout.flush()
                try:
                    click_sound.play()
                except Exception:
                    pass
                time.sleep(random.uniform(min_delay, max_delay))
                sys.stdout.write('\b')
                sys.stdout.flush()
    print()
    # play_ping(times=2, delay_ms=100)
    sys.stdout.flush()

# ---------------- SAFE INPUT SYSTEM ----------------

_original_input = builtins.input  # keep Python’s original input

def _flush_stdin():
    """Flush any accidental keystrokes from stdin."""
    try:
        if os.name == 'nt':  # Windows
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getwch()  # discard any buffered key
        else:  # Linux/macOS
            import termios, select
            fd = sys.stdin.fileno()
            try:
                termios.tcflush(fd, termios.TCIFLUSH)
            except Exception:
                # fallback: read all pending input
                while select.select([sys.stdin], [], [], 0)[0]:
                    sys.stdin.read(1)
    except Exception:
        pass  # ignore if flush fails (harmless)

def animated_input(prompt=""):
    """
    A blocking input that waits until the typewriter animation is finished.
    Discards any keys pressed during animation.
    """
    if prompt:
        typewriter(prompt)
    sys.stdout.flush()
    time.sleep(0.1)  # allow sound to settle
    _flush_stdin()   # clear any pre-pressed keys
    user_in = _original_input("> ").strip()
    return user_in

# Make all input() calls automatically use animated_input
builtins.input = animated_input
























