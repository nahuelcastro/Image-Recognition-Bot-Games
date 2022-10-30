# Image Recognition-Bot-Games

## Collections of bots that automatically play games with image recognition.

---

## Piano Tiles Bot:

![Piano Tiles Bot Demo](Demos/PianoTilesBotDemo.gif)
The bot automatically locate the game in screen and identify the tiles. It then clicks on the tiles in the correct order. My score record with this bot is _3335_ in [this website](https://www.agame.com/game/magic-piano-tiles).

An improvement to this bot is to use a neural network to identify the tiles. This will make the bot more robust to different screen resolutions and different game versions, and also make it more efficient.

You can find the code in [pianoTilesBot.py](pianoTilesBot.py).

Feel free to try it out and beat my score!

---

## AimBooster Bot:

![AimBooster Bot Demo](Demos/AimBoosterDemo.gif)

The bot automatically locate the game in screen and identify the targets. It then clicks on the targets in the correct order. I don't have a score record with this bot because the bot works too well and doesn't miss any targets :)

You can find the code in [aimboosterBot.py](aimboosterBot.py) and try it with [this website](https://aimbooster.com/).

## Feel free to try it out and improve my code!

---

## How to use

1. Clone the repository
2. Install the required packages with `pip install -r requirements.txt`
3. Open the game that you want to play in your browser.
4. I used this websites: [Piano Tiles](https://www.agame.com/game/magic-piano-tiles), [AimBooster](https://aimbooster.com/), but you can use any other website that you want while the game screen is similar to these games. If the screen are not similar, you need to change the locator images in locator folder for a focus screenshot of these new screen games.
5. Run the code with `python aimboosterBot.py` or `python pianoTilesBot.py`
6. Press `s` to start the bot and `q` to quit the bot.
7. Take fun beating scores!
