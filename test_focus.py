from textual.app import App, ComposeResult
from textual.widgets import Input, Select, Label
from textual.binding import Binding

class TestApp(App):
    BINDINGS = [
        Binding("escape", "app.clear_focus", "Clear Focus", show=True),
        Binding("h", "focus_left", "Left"),
        Binding("l", "focus_right", "Right"),
    ]

    def compose(self) -> ComposeResult:
        yield Select[str]([("A", "A")], id="sel1")
        yield Select[str]([("B", "B")], id="sel2")
        yield Input(id="in1")
        yield Label("Press Esc to unfocus, then h/l to move.")

    def action_clear_focus(self):
        self.screen.set_focus(None)
        self.notify("Focus cleared!")

    def action_focus_left(self):
        self.notify("Left pressed")

    def action_focus_right(self):
        self.notify("Right pressed")

if __name__ == "__main__":
    app = TestApp()
    # We won't run it interactively, just import to ensure it parses without errors
    # app.run()
