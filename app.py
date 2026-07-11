import subprocess
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, OptionList, Button, Static, Input
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
class gnex_cli(App):
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
    #search-box{
        dock:bottom;
    }
    """
    BINDINGS = [("q", "quit")]

    def __init__(self):
        super().__init__()
        self.current_uuid = None
        self.all_uuids = []

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            with Vertical(id="left-pane"):
                yield OptionList(id = "ext-list")
                yield Input(placeholder = "input something to search", id = "search-box")
            with Vertical(id="right-pane"):
                yield ExtensionDetails("Choose an extension from left pane", id="ext-details")
                with Horizontal(id="action-buttons"):
                    yield Button("Enable", id="btn-enable", variant="success")
                    yield Button("Disable", id="btn-disable", variant="error")
                    
        yield Footer()
    def update_list(self, uuids_to_show):
        ext_list = self.query_one("#ext-list", OptionList)

        ext_list.clear_options()
        for uuid in uuids_to_show:
            ext_list.add_option(Option(uuid, id = uuid))
    
    def on_mount(self):
        self.all_uuids = get_installed_extensions()
        self.update_list(self.all_uuids)

    def on_input_changed(self, event: Input.Changed):
        search_text = event.value.lower()
        if not search_text:
            self.update_list(self.all_uuids)
        else:
            filtered_uuids = [uuid for uuid in self.all_uuids if search_text in uuid.lower()]
            self.update_list(filtered_uuids)
    
    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        self.current_uuid = event.option.id
        info = get_extensions_info(self.current_uuid)
        self.query_one("#ext-details", ExtensionDetails).update_info(info)
    
    def on_button_pressed(self, event: Button.Pressed):
        if not self.current_uuid:
            self.notify("Choose a extensions from left pane", severity = "warning")
            return
        button_id = event.button.id
        try:
            if button_id == "btn-enable":
                subprocess.run(['gnome-extensions','enable', self.current_uuid], check = True)
                self.notify(f"successful enabled {self.current_uuid}", title = "Enabled")
            elif button_id == "btn-disable":
                subprocess.run(['gnome-extensions','disable', self.current_uuid], check = True)
                self.notify(f"successful disabled {self.current_uuid}", title = "Disabled", severity = "error")
        except Exception as e:
            self.notify(f"Operation failed:{e}", severity = "warning", title = "error")
        
        info = get_extensions_info(self.current_uuid)
        self.query_one("#ext-details", ExtensionDetails).update_info(info)




if __name__ == "__main__":
    app = gnex_cli()
    app.run()   