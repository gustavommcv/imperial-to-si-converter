from core.conversions import ConversionRegistry

@ConversionRegistry.register("Temperatura")
class TemperatureConverter:
    def __init__(self):
        self.conversions = {
            ("Fahrenheit (°F)", "Celsius (°C)"): lambda x: (x - 32) * 5.0 / 9.0,
        }

    def get_available_conversions(self):
        return list(self.conversions.keys())

    def convert(self, from_unit: str, to_unit: str, value: float):
        func = self.conversions.get((from_unit, to_unit))
        if func:
            return func(value)
        raise ValueError(f"Conversão de '{from_unit}' para '{to_unit}' em Temperatura não suportada.")
