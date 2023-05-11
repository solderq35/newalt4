# New Alt 4

Ori13 and ChatGPT's idea to troll IOI for trying to prevent people from cheesing Hitman Freelancer mode

## Disclaimer
**NOTE: It is probably more convenient to just open Task Manager, then stop HITMAN3.exe. This program is just for fun.**

With that said:

## Setup Instructions

### EXE
- Wait until you have actually started up Hitman 3 before doing the below
- Better if you don't want to actually compile or install Python
- Open `dist` directory, then run `newalt4.exe`

### Python Compile
- Wait until you have actually started up Hitman 3 before doing the below
- Better if you want to edit the keybind etc
- `pip install -r requirements.txt`
- You do need Python installed... I have Python 3.8
- `python newalt4.exe`
- https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen
  - This explains to compile the Python to exe, if you want to edit the exe keybinds
- When a level is loaded, press CTRL + ALT + Q to force quit without ALT + F4

## Usage Instructions
- When a level is loaded, press CTRL + ALT + Q to force quit without ALT + F4

## Next Steps
- You can include this with a [batch file](https://github.com/solderq35/hitman-tech-tips/blob/main/misc/h3legendary.md#batch-files) to launch the game, especially if you have Legendary (there is probably Steam CLI equivalent), which might end up being more convenient than Task Manager at that point idk.
