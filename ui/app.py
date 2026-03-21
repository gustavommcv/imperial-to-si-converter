from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Select, Input, Label
from textual.binding import Binding

from core.conversions import get_categories, get_conversions_for_category, convert

class CalculatorApp(App):
    """Aplicativo de Calculadora de Conversão com TUI Moderna."""
    
    # Referência correta ao CSS que criaremos
    CSS_PATH = "styles.tcss"
    TITLE = "Conversor de Medidas | Sistema Imperial p/ SI"
    ENABLE_COMMAND_PALETTE = False

    # Atalhos exigidos pelo usuário: q para Sair e h/j/k/l para navegar + setas.
    # Setas e suporte ao mouse vêm nativamente nos componentes do Textual!
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

    def compose(self) -> ComposeResult:
        """Monta os componentes da UI."""
        yield Header()
        
        with Container(id="main-container"):
            yield Label("Atividade Semestral 01 - Selecione a Grandeza", id="title-label")
            
            # Carrega a lista com Comprimento, Massa, Temperatura, Volume
            categories_options = [(c, c) for c in get_categories()]
            yield Select(categories_options, id="category-select", prompt="Escolha a Grandeza")

            with Horizontal(id="conversion-container"):
                # Coluna Origem
                with Vertical(classes="column"):
                    yield Label("De (Imperial):", classes="col-label")
                    yield Select([], id="from-unit-select", prompt="Unidade Origem", disabled=True)
                    yield Input(placeholder="Digite o valor", id="input-value", type="number")

                # Coluna Destino
                with Vertical(classes="column"):
                    yield Label("Para (SI):", classes="col-label")
                    yield Select([], id="to-unit-select", prompt="Unidade Destino", disabled=True)
                    yield Input(placeholder="Resultado da conversão", id="output-value", disabled=True)
            
            yield Label("", id="error-message")

        yield Footer()

    # Eventos de seleção
    def on_select_changed(self, event: Select.Changed) -> None:
        """Lida com as mudanças de valores nas caixas de seleção."""
        select_id = event.control.id
        
        if select_id == "category-select":
            self.update_from_select(event.value)
        elif select_id == "from-unit-select":
            self.update_to_select(event.value)
        
        # Qualquer mudança recálcula para ser reativo.
        self.calculate()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Se o usuário digita nos valores de entrada..."""
        if event.control.id == "input-value":
            self.calculate()

    def update_from_select(self, category_value: str) -> None:
        """Atualiza o menu de origem com base na grandeza escolhida."""
        from_select = self.query_one("#from-unit-select", Select)
        to_select = self.query_one("#to-unit-select", Select)
        
        if category_value == Select.BLANK:
            from_select.disabled = True
            to_select.disabled = True
            from_select.set_options([])
            to_select.set_options([])
            return

        conversions = get_conversions_for_category(category_value)
        unique_origins = list(set([c[0] for c in conversions]))
        
        from_select.set_options([(o, o) for o in unique_origins])
        from_select.disabled = False
        to_select.disabled = True  # Desativado até escolherem a origem
        to_select.set_options([])
        from_select.clear()

    def update_to_select(self, from_unit_value: str) -> None:
        """Atualiza as unidades de destino posíveis baseadas na de origem."""
        to_select = self.query_one("#to-unit-select", Select)
        category_value = self.query_one("#category-select", Select).value
        
        if from_unit_value == Select.BLANK or category_value == Select.BLANK:
            to_select.disabled = True
            to_select.set_options([])
            return

        conversions = get_conversions_for_category(category_value)
        possible_destinations = [c[1] for c in conversions if c[0] == from_unit_value]
        
        to_select.set_options([(d, d) for d in possible_destinations])
        to_select.disabled = False
        to_select.clear()

    def calculate(self) -> None:
        """Aplica a regra de conversão de fato no input que foi digitado e preenche"""
        error_label = self.query_one("#error-message", Label)
        output_input = self.query_one("#output-value", Input)
        
        error_label.update("")
        output_input.value = ""

        try:
            category = self.query_one("#category-select", Select).value
            from_unit = self.query_one("#from-unit-select", Select).value
            to_unit = self.query_one("#to-unit-select", Select).value
            raw_val = self.query_one("#input-value", Input).value

            if category == Select.BLANK or from_unit == Select.BLANK or to_unit == Select.BLANK or not raw_val:
                return

            if raw_val in ("-", ".", "-."):
                return

            val_float = float(raw_val)
            result = convert(category, from_unit, to_unit, val_float)
            
            output_input.value = f"{result:g}" # Formatando sem casa decimal desnecessaria
            
        except ValueError as e:
            if "não suportada" in str(e):
                error_label.update("Conversão não mapeada.")
            else:
                error_label.update("Valor inválido inserido.")
        except Exception as e:
            error_label.update(f"Falha inesperada: {str(e)}")
