# Registry Base
class ConversionRegistry:
    """Implementa o padrão de projeto Registry e Strategy para escalar novas Grandezas"""

    _strategies = {}

    @classmethod
    def register(cls, category_name: str):
        """Decorador para auto-registrar uma grandeza nova na inicialização."""

        def decorator(converter_class):
            cls._strategies[category_name] = converter_class()
            return converter_class

        return decorator

    @classmethod
    def get_categories(cls):
        return list(cls._strategies.keys())

    @classmethod
    def get_conversions_for_category(cls, category_name: str):
        converter = cls._strategies.get(category_name)
        if converter:
            return converter.get_available_conversions()
        return []

    @classmethod
    def convert(
        cls, category_name: str, from_unit: str, to_unit: str, value: float
    ) -> float:
        converter = cls._strategies.get(category_name)
        if converter:
            return converter.convert(from_unit, to_unit, value)
        raise ValueError(
            f"A Categoria '{category_name}' não foi registrada com sucesso."
        )


# Para não quebrar NADA da nossa Interface Gráfica (ui/app.py) que importa métodos puros,
# mantemos uma "casca/interface" (API pública) ligando ao nosso Registry Singleton:
get_categories = ConversionRegistry.get_categories
get_conversions_for_category = ConversionRegistry.get_conversions_for_category
convert = ConversionRegistry.convert

# Autodiscover (Módulos Plugáveis / Plugins)
# Importa-se localmente da subpasta 'units' para prevenir circular-imports.
from .units import length, mass, temperature, volume
