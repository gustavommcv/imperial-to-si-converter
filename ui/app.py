from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Select, Input, Label

from core.conversions import get_categories
from ui.bindings import KeybindsMixin
from ui.events import EventsMixin

# Nossa Classe herda os Eventos (on_select) e os Atalhos (h, j, k, l) via Mixin
class CalculatorApp(EventsMixin, KeybindsMixin, App):
    """Aplicativo de Calculadora de Conversão com TUI Moderna e Modular."""
    
    # Textual MetaClasses exigem declaração estática na própria DOMNode:
    BINDINGS = KeybindsMixin.BINDINGS

    CSS_PATH = "styles.tcss"
    TITLE = "Conversor de Medidas | Sistema Imperial p/ SI"
    ENABLE_COMMAND_PALETTE = False

    def compose(self) -> ComposeResult:
        """Monta a Árvore de Componentes da Interface (Sem Lógica aqui)."""
        yield Header()
        
        with Container(id="main-container"):
            yield Label("Atividade Semestral 01 - Selecione a Grandeza", id="title-label")
            
            # Carrega listas limpas
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
