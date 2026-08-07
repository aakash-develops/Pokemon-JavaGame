## Poke Flight

A Pokémon fan game where you fly between airports, battle trainers, capture/steal Pokémon, and try to clear your name. Includes a short story, ASCII animations, and two mini-games (Poker & Russian Roulette).

> ⚠️ Fan-made, for education only. Not affiliated with Nintendo/Game Freak/TPC.

## Features

- Turn-based battles with type effectiveness
- Travel to nearby airports or free-fly by distance & bearing
- Villain encounters (battle, Poker, Russian Roulette)
- Capture/steal system (max 6 Pokémon, no PC)
- Achievements and simple ASCII UI

## Requirements

- Python 3.10+
- Windows recommended (uses `msvcrt` for fast text skipping)
- Unicode-capable terminal

## Install & Run

[Not public right now]

Download off github

Run main_pokemon_file.py in a terminal from the amalgamation folder for visuals and sound effects.
Use Maria DB with the database SQL file uploaded on OMA
Change to allow user access with sql connector, change the username and password accordingly .
Run on a terminal in FULL SCREEN

## Controls

- In battle: type the **exact move name** (case-sensitive) or `SWAP`
- `/HELP` for tips in battle
- Main menu: `1` travel, `0` land, `A/B/C/D` menus
- Cheats: `PAYDAY` (Meowth), `I choose you!` (Pikachu)

## Notes

- Ensure local modules (e.g., `all_pokemon_list.py`, `attack_dict.py`, `type_chart_factor.py`, `dialogues.py`, etc.) are present.
-  macOS/Linux: if `msvcrt` causes issues, disable the skip-key path in `d_print()`.
-  SQL file required (check OMA uploads)
-  mp3 and wav files required, if they're missing for some strange reason, download from OMA

License

Educational use only. Do not distribute commercially.
