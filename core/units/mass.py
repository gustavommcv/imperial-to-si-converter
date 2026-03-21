from core.conversions import ConversionRegistry

@ConversionRegistry.register("Massa/Peso")
class MassConverter:
    def __init__(self):
        self.conversions = {
            ("Onça (oz)", "Grama (g)"): lambda x: x * 28.3495,
            ("Libra (lb)", "Quilograma (kg)"): lambda x: x * 0.453592,
        }

    def get_available_conversions(self):
        return list(self.conversions.keys())

    def convert(self, from_unit: str, to_unit: str, value: float):
        func = self.conversions.get((from_unit, to_unit))
        if func:
            return func(value)
        raise ValueError(f"Conversão de '{from_unit}' para '{to_unit}' em Massa não suportada.")
