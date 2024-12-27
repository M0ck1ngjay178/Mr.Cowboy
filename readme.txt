# 🤠 Mr. Cowboy -- Arena Shooter/Platformer  

*Updated as of 4/27/24*  

---

## << LIBRARIES >>  
- 🐍 `pygame`  -- Support for games in Python  
- 📁 `os`      -- Support for folder/file navigation  
- 🖥️ `sys`  
- ⏳ `time`  
- 🎲 `random`  
- ➗ `math`  

---

## << INSTALL INSTRUCTIONS >>  
- 📥 **Python3**: User must install the latest version of Python3 on their device  
- 🎮 **pygame**: User must `pip install` the latest version of pygame on their device  
- 🧰 The `os` and `sys` libraries are built into Python3 and don’t need to be installed.  
- 🚀 **main.py**: User should only try to start the game in **`main.py`**; trying in any other module will not work.

---

## << GAME START INSTRUCTIONS >>  
- 💻 User may start the game in the IDLE editor, but ensure that ALL `.py` files are in the same folder.  
- ⚡ Only start the game in **`main.py`**.  
- 🔁 Anytime a player dies, they must restart the entire program to play again.

---

## << CONTROLS >>  
- ⏎ **ENTER** - Start Game  
- 🕹️ **W** - Jump  
- ⬅️ **A** - Move Left  
- ➡️ **D** - Move Right  
- 🔫 **Space** - Shoot  
- 💥 **Q** - Throw Dynamite  
- 🏆 **T** - Travel (Credits Page)  
- 🚶 **B** - Exit Travel Mode  
- 🛠️ **P** - Debug key; Grants player an absurd amount of health for testing purposes.  

---

## << RULES >>  
- 🔄 Player may double jump when on the ground, but not when on a platform. More options in tight situations.  
- 🏃‍♂️ If a player falls or walks off a platform, they cannot land on one below them.  
- 🪜 Platforms are only used to go higher, not lower.  
- 🌐 Players may walk off the sides of the screen, but be careful, you'll reappear on the other side! Applies to dynamite too, but not bullets.  
- ⏱️ After a certain amount of time, platform speed will continually change, enemy speeds will increase infinitely, and 2 new enemies will appear for a total of 4 enemies.

---

## << ITEM DROPS AND ODDS >>  
- 👒 **Golden Hats** - Restore a small amount of health (15% at Start, 0% after X Time)  
- 👢 **Boots** - Permanent speed boost for the player (5% at Start, 15% after X Time)  
- 💣 **Dynamite Crate** - Replenish some dynamite (40% at Start, 25% after X Time)  
- 🎯 **Ammo Box** - Replenish 12 Bullets (39% at Start, 50% after X Time)  
- 💰 **Silver Dollar** - Completely restores all player attributes and ammo (1% for Full Game)

---

## << MODULES >>  
- **`main.py`** - Contains the main instance of the game among MANY other things. Relies on `setUp.py` and various other modules for successful operation. **ONLY USE THIS FILE TO BUILD/COMPILE.**
  
- **`setUp.py`** - Contains backend setup. Loads images, creates needed game objects, and holds essential functions. Calls on other modules.

- **`attacks.py`** - Handles all character attacks (shooting, throwing dynamite, etc). Includes the `Bullet`, `Dynamite`, and `Explosion` classes.

- **`characters.py`** - All character-related info and classes. AI and player features are in this file. Includes `Characters` and `Healthbar` classes.

- **`environment.py`** - Contains dynamic environment objects that move, like the `Tumbleweed` and `Platform` classes.

- **`items.py`** - Holds player-only collectibles/power-ups. Includes the `ItemBox` class.

- **`guiFeatures.py`** - Handles GUI features for buttons and interactions. Includes the `GUI_Button` class.

---

Enjoy the wild west adventure in Mr. Cowboy! 🤠💥  


