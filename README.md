# Gnex_cli - A new way to manage your GNOME Extensions

Gnex_cli is a Terminal User Interface (TUI) application designed to manage your GNOME Shell extensions easily and efficiently directly from your terminal. Built with Python and the [Textual](https://textual.textualize.io/) framework, it provides a clean, intuitive interface to view, enable, and disable your GNOME extensions without leaving the command line.

## Features

- **List Extensions**: View a comprehensive list of all installed GNOME extensions in the left pane.
- **Detailed Information**: See detailed information about a selected extension, including its Name, Status (Enabled/Disabled), Version, and Description.
- **Enable/Disable**: Quickly enable or disable extensions with a single button press.

## Prerequisites

- Python 3.x
- GNOME Desktop Environment (`gnome-extensions` CLI tool must be installed and accessible).

## How to run the release version
1. Download the appimage
2. cd to the path folder of file
3. run `chmod +x` to make it excutable
4. `./gnex_cli-x86_64.AppImage` to run it


## Installation
```bash
git clone https://github.com/lin3598197/gnex_cli.git && cd gnex_cli
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
#### After you install,next time you only have to do is:
```bash
cd gnex_cli #path to your folder in local
source .venv/bin/activate #if you didn't activate virtual enviroment
python app.py #run app
```
### Controls

- **Mouse**: Click on an extension in the list to view its details, and click the "Enable" or "Disable" buttons to change its status.
- **Keyboard**: Use the `Up` and `Down` arrow keys to navigate the extension list. Press `Tab` to switch focus between the list and the action buttons, and `Enter` to trigger a button.
- **Quit**: Press the `q` key at any time to exit the application.

### If there any question, please open the issue ticket, I will fix it as soon as I posible

### AI Using
I use AI to help me fix the code, debug the errors, and help me to translate chinese to english,AI also help me write the docs too :D
