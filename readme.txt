UPDATED AS OF 4/27/24
Mr. Cowboy -- Arena Shooter/Platformer
----------------------------------------------

<< LIBRARIES >>
>> pygame      -- Support for games in python
>> os          -- Support for folder/file navigation
>> sys
>> time
>> random
>> math

----------------------------------------------

<< INSTALL INSTRUCTIONS >>
>> User must install the latest version of Python3 on their device
>> User must pip install the latest version of pygame on their device
>> The os library does not need to be installed by users; this library comes with the latest version of Python3.
>> The sys library does not need to be installed by users; this library comes with the latest version of Python3.
>> User should only try to start the game in main.py : Trying in any other module will not work.


<< GAME START INSTRUCTIONS >>
>> User may start the game in the IDLE editor, but ensure that ALL .py files are in the same folder.
>> As previously mentioned, only start the game in main.py
>> Anytime a player dies, they must restart the entire program to play again.

----------------------------------------------

<< CONTROLS >>

>> ENTER - Start Game

>> W - Jump
>> A - Move Left
>> D - Move Right

>> Space - Shoot
>> Q - Throw Dynamite
>> T - Travel (Credits Page)
>> B - Exit Travel Mode

>> P - Debug key; Grants player absurd amount of health. Mostly did this to possibly make grading/examination of features easier.

<< RULES >>
>> Player may double jump when on the ground, but not when on a platform. More options in tight situations.
>> If a player falls/walks off of a platform, they cannot land on one below them.
>> Platforms are only used to go higher, not lower.
>> Players may walk off the sides of the screen, but be careful, you'll reappear on the the otherside! Applies to dynamite too, but not bullets.
>> After a certain amount of time, platform speed will continually change, enemy speeds will increase infinitely, and 2 new enemies will appear for 4 enemies total.

<< ITEM DROPS AND ODDS >>
>> Golden Hats      - Restore a small amount of health (15% at Start, 0% after X Time)
>> Boots            - Permanent speed boost for player (5% at Start, 15% after X Time)
>> Dynamite Crate   - Replenish some dynamite (40% at Start, 25% after X Time)
>> Ammo Box         - Replenish 12 Bullets (39% at Start, 50% after X Time)
>> Silver Dollar    - Completely restores all player attributes and ammo (1% for Full Game)

----------------------------------------------

<< MODULES >>

>> main.py - Contains the main instance of the game among MANY other things.
Relies on setUp.py and various other modules for successful operation
ONLY USE THIS FILE TO BUILD/'COMPILE'

>> setUp.py - Lots of backend. Consists of instances of every needed object in the game, loads images, and contains various functions used throughout program
Calls on some of the following modules

>> attacks.py - All character attacks (shooting, throwing dynamite, etc) will be stored here.
Includes; Bullet class, Dynamite class, Explosion class

>> characters.py - All character related information and classes. Most AI and player features are in this file.
Includes; Characters class and Healthbar class.

>> environment.py - Dynamic evironment objects will be here, i.e. stuff that moves.
Includes; Tumbleweed class, Platform class

>> items.py - Contains player-only collectibles/power ups
Includes; ItemBox class

>> guiFeatures.py - Contains necessary gui features for buttons to work properly
Includes; GUI_Button class

----------------------------------------------


