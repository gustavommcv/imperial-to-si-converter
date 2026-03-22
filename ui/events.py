from textual.widgets import Select, Input, Label
from core.conversions import get_conversions_for_category, convert
from typing import Any


class EventsMixin:
    """
    Mixin estrutural com todas as funções de callback disparadas pelo usuário.
    Garante que os dropdowns carreguem a próxima dependência logicamente.
    """

    def on_select_changed(self: Any, event: Select.Changed) -> None:
        """Lida com as mudanças de valores nas caixas de seleção."""
        select_id = event.control.id

        if select_id == "category-select":
            self.update_from_select(event.value)
        elif select_id == "from-unit-select":
            self.update_to_select(event.value)

        # Qualquer mudança nas dropdowns também atualiza a equação ao vivo.
        self.calculate()

    def on_input_changed(self: Any, event: Input.Changed) -> None:
        """Monitora digitação numérica do campo para invocar o cálculo."""
        if event.control.id == "input-value":
            self.calculate()

    def update_from_select(self: Any, category_value: Any) -> None:
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
        to_select.disabled = (
            True  # Reseta o terceiro Select até ele preencher o segundo
        )
        to_select.set_options([])
        from_select.clear()

    def update_to_select(self: Any, from_unit_value: Any) -> None:
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

    def calculate(self: Any) -> None:
        """Consome o motor do pacote Core para performar conversão e desenhar no input"""
        error_label = self.query_one("#error-message", Label)
        output_input = self.query_one("#output-value", Input)

        error_label.update("")
        output_input.value = ""

        try:
            category = self.query_one("#category-select", Select).value
            from_unit = self.query_one("#from-unit-select", Select).value
            to_unit = self.query_one("#to-unit-select", Select).value
            raw_val = self.query_one("#input-value", Input).value

            if (
                category == Select.BLANK
                or from_unit == Select.BLANK
                or to_unit == Select.BLANK
                or not raw_val
            ):
                return

            # Validações caso esteja digitando floats de sinal
            if raw_val in ("-", ".", "-."):
                return

            val_float = float(raw_val)
            result = convert(category, from_unit, to_unit, val_float)

            output_input.value = f"{result:g}"

        except ValueError as e:
            if "não suportada" in str(e):
                error_label.update("Conversão não mapeada.")
            else:
                error_label.update("Valor inválido inserido.")
        except Exception as e:
            error_label.update(f"Falha inesperada: {str(e)}")
