# Zorklon5!

Garfield: Larger Than Life is a python-based Adventure/Horror RPG to be run on the command line. It was my first "big" self-developed project. 


## Developed by

Ethan Gula

[email me](Ethangula96@gmail.com) / [github](https://github.com/Emgula96/DCBC/tree/main/On%20going%20projects/Games)


## Requirements

- Python3 or later (built on Python3.10)



## To run

- On Mac Terminal: `python3 GarfieldLTL .py`
- On Windows Command Line: `python3 GarfieldLTL.py`


## Similar projects

I've designed two more text-based RPG games that are similar in concept; [heroRPG](https://github.com/dgelok/heroRPG) and [Pyramid_Game](https://github.com/dgelok/pyramidGame). Both utilize OOP principles, but heroRPG is significantly larger, and was made as part of DigitalCrafts curriculum (June 2020 Houston cohort). 

GarfieldLTL.py was designed to develop my coding skills across a larger project. At the time of development, I did not know how to properly utilize classes or import other modules. It was started largely thanks to the help of my instructors at Digital Crafts, fellow cohort members, and through supplemental practice. The book I used was Zed Shaw's, *Learn Python the Hard Way* (available [here](https://www.amazon.com/Learn-Python-Hard-Way-Introduction/dp/0134692888/ref=sr_1_1?keywords=python+the+hard+way&qid=1577465107&sr=8-1)). 


## How it works

| Feature | Description |
| ----------- | ----------- |
| Locations | Garfield: Larger Than Life involves traveling to and interacting with locations. Locations are dictionaries, each containing visual descriptions, interactive text, items, enemies, and references to other locations that you can travel to from here. The map is laid out in a 9X9 grid with an extra location at the far north. |
| Items | Items are appended to a list of supplies and can be used in various ways. Most items found must be worked with in the workshop() function in order to be usable. Each item found can be transformed into a useful tool (like weapons or an underwater breathing apparatus) or food. The game cannot advance without developing items, which in turn are used to develop other items. Items are distributed around the map. Once an item is observed, it is appended to the player's supplies and does not regenerate.|
| Fights | Since this is a horror game with the presence of a very fordible boss, the object is not to fight if given the option. Each chracter (stored as a class) is given attack power and health points, and starting items that can be used to meet the vitory parameters or increases survivability. |
| Dying or Winning | If a player runs out of health completely, they die and the game exits. To defeat the cat overlord, you must carefully navigate the game and collect the necasarry items to 'End it all'. If you do not, well I think you know what happens. 


## Current bugs and possible additional developments
- Add items to increase health or distract garfield(prevent damage)
- Cleanup of coding lines to make game more visibly readable
- Add more playable characters or unique endings.