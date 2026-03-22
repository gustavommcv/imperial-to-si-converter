from textual.binding import Binding
from typing import Any

class KeybindsMixin:
    """
    Mixin contendo toda a lógica de manipulação de atalhos e suporte ao teclado.
    Projetado para abstrair os Motion do VIM e interações fluídas para Tiling Window Managers.
    """
    
    BINDINGS = [
        Binding("h", "vim_left", "Esquerda (Vim-h)", show=False),
        Binding("j", "vim_down", "Baixo (Vim-j)", show=False),
        Binding("k", "vim_up", "Cima (Vim-k)", show=False),
        Binding("l", "vim_right", "Direita (Vim-l)", show=False),
        Binding("escape", "escape_vim", "Normal Mode (Vim-Esc)", show=True),
        Binding("ctrl+n", "cursor_down_vim", "Para Baixo Lista (Vim)", priority=True, show=False),
        Binding("ctrl+p", "cursor_up_vim", "Para Cima Lista (Vim)", priority=True, show=False),
        Binding("q", "quit", "Sair")
    ]

    FOCUS_MAP = {
        "left": {
            "to-unit-select": "from-unit-select",
            "output-value": "input-value"
        },
        "right": {
            "from-unit-select": "to-unit-select",
            "input-value": "output-value"
        },
        "up": {
            "from-unit-select": "category-select",
            "to-unit-select": "category-select",
            "input-value": "from-unit-select",
            "output-value": "to-unit-select"
        },
        "down": {
            "category-select": "from-unit-select",
            "from-unit-select": "input-value",
            "to-unit-select": "output-value"
        }
    }

    def _move_focus(self: Any, direction: str) -> None:
        focused = self.screen.focused
        if not focused:
            try:
                self.query_one("#category-select").focus()
            except Exception:
                pass
            return
            
        current_id = focused.id if focused else None
        next_id = self.FOCUS_MAP.get(direction, {}).get(current_id)
        
        if next_id:
            try:
                target = self.query_one(f"#{next_id}")
                if target and getattr(target, "disabled", False) == False:
                    target.focus()
            except Exception:
                pass

    def action_vim_left(self: Any) -> None:
        self._move_focus("left")

    def action_vim_right(self: Any) -> None:
        self._move_focus("right")

    def action_vim_up(self: Any) -> None:
        self._move_focus("up")

    def action_vim_down(self: Any) -> None:
        self._move_focus("down")

    def action_escape_vim(self: Any) -> None:
        """Sai de campos de input voltando o foco para o seletor correspondente (emula Esc do Vim)."""
        focused = self.screen.focused
        if focused:
            if focused.id == "input-value":
                try:
                    self.query_one("#from-unit-select").focus()
                except Exception:
                    pass
            elif focused.id == "output-value":
                try:
                    self.query_one("#to-unit-select").focus()
                except Exception:
                    pass
            else:
                self.screen.set_focus(None)

    def action_cursor_down_vim(self: Any):
        """Ação para ctrl+n descer listas de opção suspensas como no VIM."""
        focused = self.screen.focused
        if hasattr(focused, "action_cursor_down"):
            focused.action_cursor_down()
            
    def action_cursor_up_vim(self: Any):
        """Ação para ctrl+p subir listas de opção suspensas como no VIM."""
        focused = self.screen.focused
        if hasattr(focused, "action_cursor_up"):
            focused.action_cursor_up()
