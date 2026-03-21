from textual.binding import Binding

class KeybindsMixin:
    """
    Mixin contendo toda a lógica de manipulação de atalhos e suporte ao teclado.
    Projetado para abstrair os Motion do VIM e interações fluídas para Tiling Window Managers.
    """
    
    BINDINGS = [
        Binding("h", "focus_previous", "Anterior (Vim-h)", show=False),
        Binding("j", "focus_next", "Próximo (Vim-j)", show=False),
        Binding("k", "focus_previous", "Anterior (Vim-k)", show=False),
        Binding("l", "focus_next", "Próximo (Vim-l)", show=False),
        Binding("ctrl+n", "cursor_down_vim", "Para Baixo Lista (Vim)", priority=True, show=False),
        Binding("ctrl+p", "cursor_up_vim", "Para Cima Lista (Vim)", priority=True, show=False),
        Binding("q", "quit", "Sair")
    ]

    def action_focus_next(self):
        """Ação para ir ao proximo campo usando atalhos vim"""
        self.screen.focus_next()
        
    def action_focus_previous(self):
        """Ação para ir ao campo anterior usando atalhos vim"""
        self.screen.focus_previous()

    def action_cursor_down_vim(self):
        """Ação para ctrl+n descer listas de opção suspensas como no VIM."""
        focused = self.screen.focused
        if hasattr(focused, "action_cursor_down"):
            focused.action_cursor_down()
            
    def action_cursor_up_vim(self):
        """Ação para ctrl+p subir listas de opção suspensas como no VIM."""
        focused = self.screen.focused
        if hasattr(focused, "action_cursor_up"):
            focused.action_cursor_up()
