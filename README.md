# 🤠 **Mr. Cowboy -- Arena Shooter/Platformer**  
*Updated as of 4/27/24*  

---

## 📜 **Project Info**  
- **Game Title**: Mr. Cowboy -- Arena Shooter/Platformer  
- **Author**: M.BONAL, C.MASSEY  
- **Game Type**: Action/Platformer  
- **Language**: Python  
- **Libraries Used**: `pygame`, `os`, `sys`, `time`, `random`, `math`  

---

## 🛠️ **Installation Instructions**  
1. Install the latest version of Python 3 on your device.  
2. Install the latest version of `pygame` via pip:
    ```bash
    pip install pygame
    ```
3. The `os` and `sys` libraries come pre-installed with Python, so no installation is needed for them.  
4. Start the game only by running **`main.py`**. Trying to run any other module won't work.  

---

## 🎮 **Game Start Instructions**  
- Start the game in the IDLE editor, ensuring that **ALL .py files** are in the same folder.  
- As mentioned, **only run `main.py`** to play the game.  
- When a player dies, restart the entire program to play again.  

---

## ⌨️ **Controls**  
- **ENTER**: Start Game  
- **W**: Jump  
- **A**: Move Left  
- **D**: Move Right  
- **Space**: Shoot  
- **Q**: Throw Dynamite  
- **T**: Travel (Credits Page)  
- **B**: Exit Travel Mode  
- **P**: Debug Key (Grants absurd health for testing purposes)  

---

## 📏 **Rules**  
- Players may double jump only when on the ground, not while on a platform.  
- Falling or walking off a platform prevents landing on one below.  
- Platforms are for going higher, not lower.  
- Players can walk off one side of the screen and reappear on the other side. Dynamite follows this rule, but bullets do not.  
- After a certain amount of time:  
    - Platform speed will continuously change.  
    - Enemy speeds will increase infinitely.  
    - 2 new enemies will spawn for a total of 4 enemies.  

---

## 🎁 **Item Drops and Odds**  
- **Golden Hats**: Restore a small amount of health (15% at Start, 0% after X Time)  
- **Boots**: Permanent speed boost (5% at Start, 15% after X Time)  
- **Dynamite Crate**: Replenishes dynamite (40% at Start, 25% after X Time)  
- **Ammo Box**: Replenishes 12 bullets (39% at Start, 50% after X Time)  
- **Silver Dollar**: Completely restores all player attributes and ammo (1% chance for the full game)  

---

## 🗂️ **Modules**  
- **`main.py`**: Contains the main instance of the game and other essential functions.  
  - Relies on **`setUp.py`** and other modules for smooth operation.  
  - ONLY use this file to build or compile the game.  

- **`setUp.py`**: Backend setup. Initializes all necessary objects and loads images.  
  - Calls other modules for proper game operation.

- **`attacks.py`**: Stores all character attacks (shooting, throwing dynamite, etc.).  
  - Includes: Bullet class, Dynamite class, Explosion class.

- **`characters.py`**: Character-related information and classes.  
  - Includes: Characters class, Healthbar class.

- **`environment.py`**: Defines dynamic environment objects.  
  - Includes: Tumbleweed class, Platform class.

- **`items.py`**: Contains player-only collectibles and power-ups.  
  - Includes: ItemBox class.

- **`guiFeatures.py`**: Defines necessary GUI features for buttons.  
  - Includes: GUI_Button class.

---
