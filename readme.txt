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

<< CALEB'S NOTES >>
>> ONLY COMPILE IN main.py... USING ANY OTHERS WILL NOT WORK.
>> Definitely recommend VSCode with the 3 recommended Python extensions, and pygame installed on the PC. Way easier to navigate and work with.
>> We have 3 instances of platforms in the game; Instead of deleting them, they'll be on a timer or something and reappear at the right again (all off-screen of course).
>> Answered your question just under where it was Margo. See attacks.py / characters.py (I think) Just find the shoot() function, but don't mess with playerShoot() please.
>> Also cleaned up the cactus a little bit. Noticed it had a lot of transparent space around it, think it was messing with the rect or something. Also gave it a single frame death.
>> I also added in the "P" button, which is good for debugging some stuff... Just see main.py and the keyDown events to edit it as needed for debugging processes.
>> 4/6/24 - 4/15/24 -- Working on platforms. Failing miserably.
>> 4/15/24 -- Completely rewrote platform collision. Still haven't cracked it yet. But I'm close. It has to do with a loop or a flag or SOMETHING.
>> 4/17/24 -- PLATFORMS WORK! Will keep working on desert background.
>> 4/18/24 -- Added in score tracking via files, made some small QoL changes to enemies; Cactus is now technically impossible to kill.
>> 4/19/24 -- Enemies now give 100 points when deafeated; Enemies can now respawn off screen after X amount of time; More QoL stuff.
>> 4/19/24 -- Cont'd; New difficulties are added in over time, eventually speeds up infinitely; Enemies now drop collectibles. Time survived changes what's available.
>> 4/22-23/24 -- More QoL stuff.
>> 4/26/24 -- Fixed an issue where players could just wander off the screen; Fixed enemy sightlines; Player may now walk across screen infinitely, as they'll reappear on other side now.


<< MARGO'S NOTES >>
>> did a clean up on the files
>> now can toggle between screens, t-travel/ b-back from travel
>> finally fixed pause screen
>> still need to pause everything behind new screen
>> cactus shoot his bullet now/updated bullet/shooting/character classes (still cant figure out the indexing error)
>> did some edits to the event handler for smoother transitions
>> fixed indexing
>> did backend changes today(4/13/24) nothing real obvious on in game
>> finished on enemy ai
>> took some liberties with main layout
>> added scrolling desert
>> added collision for tumbleweed
>> 4/20/24 -- added game over banner
>> 4/21/24 -- toggle between day/night and did some clean up on files
>> 4/27/24 -- Final Project Review/file clean up!
