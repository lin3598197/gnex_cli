# Gnex_cli - A new way to manage your GNOME Extensions

Gnex_cli is a Terminal User Interface (TUI) application designed to manage your GNOME Shell extensions easily and efficiently directly from your terminal. Built with Python and the [Textual](https://textual.textualize.io/) framework, it provides a clean, intuitive interface to view, enable, and disable your GNOME extensions without leaving the command line.

## Features

- **List Extensions**: View a comprehensive list of all installed GNOME extensions in the left pane.
- **Detailed Information**: See detailed information about a selected extension, including its Name, Status (Enabled/Disabled), Version, and Description.
- **Enable/Disable**: Quickly enable or disable extensions with a single button press.

## Prerequisites

- Python 3.x
- GNOME Desktop Environment (`gnome-extensions` CLI tool must be installed and accessible).

## Installation

1. Clone the repository or navigate to the project directory:
   ```bash
   cd gnex_cli
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install textual
   ```

## Usage

Run the application using Python:

```bash
python3 app.py
```

### Controls

- **Mouse**: Click on an extension in the list to view its details, and click the "Enable" or "Disable" buttons to change its status.
- **Keyboard**: Use the `Up` and `Down` arrow keys to navigate the extension list. Press `Tab` to switch focus between the list and the action buttons, and `Enter` to trigger a button.
- **Quit**: Press the `q` key at any time to exit the application.
