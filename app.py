import subprocess
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, OptionList, Button, Static
from textual.widgets.option_list import Option

def get_installed_extensions():
    try:
        output = subprocess.check_output(['gnome-extensions', 'list'], text = True)
        return [line.strip() for line in output.split('\n') if line.strip()]
    except Exception:
        return []

def get_extensions_info(uuid):
    try:
        output = subprocess.check_output(['gnome-extensions', 'info', uuid], text = True)
        info = {}
        for line in output.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                info[key.strip()] = val.strip()
        return info
    except Exception:
        return {"Name": uuid, "State": "UNKNOWN", "Description": "ERR While fetch info ><"}

#-------UI Elements---------

class ExtensionDetails(Static):
    def update_info(self, info):
        name = info.get("Name", "Unknown")
        state = info.get("State", "Unknown")
        desc = info.get("Description", "No Description")
        version = info.get("Version", "N/A")
        
        state_color = "green" if state == "ENABLED" else "red"

        content = f"[b]{name}[/b]\n\n"
        content += f"[b]Status:[/b] [{state_color}]{state}[/{state_color}]\n"
        content += f"[b]Version:[/b] {version}\n\n"
        content += f"{desc}"

        self.update(content)

#-------Main Code---------------
    CSS = """
    #left-pane {
        width: 40%;
        border-right: solid ascii;
    }
    #right-pane {
        width: 60%;
        padding: 1 2;
    }
    #action-buttons {
        height: 3;
        margin-top: 2;
    }
    Button {
        margin-right: 2;
    }
    """

class GnomeExtensionApp(App):
    BINDINGS = [("q", "quit")]

    def __init__(self):
        super().__init__()
        self.current_uuid = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            yield OptionList(id="left-pane")
            with Vertical(id="right-pane"):
                yield ExtensionDetails("Choose an extension from left pane", id="ext-details")
                with Horizontal(id="action-buttons"):
                    yield Button("Enable", id="btn-enable", variant="success")
                    yield Button("Disable", id="btn-disable", variant="error")
                    
        yield Footer()
    def on_mount(self):
        ext_list = self.query_one("#left-pane", OptionList)
        uuids = get_installed_extensions()
        for uuid in uuids:
            ext_list.add_option(Option(uuid, id = uuid))
    
    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        self.current_uuid = event.option.id
        info = get_extensions_info(self, current_uuid)
        self.query_one("#ext-details", ExtensionDetails).update_info(info)
    
    def on_button_pressed(self, event: Button.Pressed):
        if not self.current_uuid:
            return
        button_id = event.button.id
        if button_id == "btn-enable":
            subprocess.run(['gnome-extensions', 'enable', self.current_uuid])
        elif button_id == "btn-disable":
            subprocess.run(['gnome-extensions', 'disable', self.current_uuid])

        info = get_extensions_info(self.current_uuid)
        self.query_one("#ext-details", ExtensionDetails).update_info(info)

if __name__ == "__main__":
    app = GnomeExtensionApp()
    app.run()