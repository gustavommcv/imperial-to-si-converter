from core.conversions import ConversionRegistry


@ConversionRegistry.register("Temperatura")
class TemperatureConverter:
    def __init__(self):
        self.conversions = {
            ("Fahrenheit (°F)", "Celsius (°C)"): lambda x: (x - 32) * 5 / 9,
            ("Fahrenheit (°F)", "Kelvin (K)"): lambda x: (x - 32) * 5 / 9 + 273.15,
        }

    def get_available_conversions(self):
        return list(self.conversions.keys())

    def convert(self, from_unit, to_unit, value):
        func = self.conversions.get((from_unit, to_unit))
        if func:
            return func(value)
        raise ValueError("Conversão não suportada")
