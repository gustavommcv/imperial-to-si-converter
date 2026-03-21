from core.conversions import ConversionRegistry

@ConversionRegistry.register("Comprimento")
class LengthConverter:
    def __init__(self):
        # Dicionário interno de lógicas restrito desta classe
        self.conversions = {
            ("Polegada (in)", "Centímetro (cm)"): lambda x: x * 2.54,
            ("Pé (ft)", "Metro (m)"): lambda x: x * 0.3048,
            ("Jarda (yd)", "Metro (m)"): lambda x: x * 0.9144,
            ("Milha (mi)", "Quilômetro (km)"): lambda x: x * 1.60934,
        }

    def get_available_conversions(self):
        return list(self.conversions.keys())

    def convert(self, from_unit: str, to_unit: str, value: float):
        func = self.conversions.get((from_unit, to_unit))
        if func:
            return func(value)
        raise ValueError(f"Conversão de '{from_unit}' para '{to_unit}' em Comprimento não suportada.")
