from core.conversions import ConversionRegistry


@ConversionRegistry.register("Comprimento")
class LengthConverter:
    def __init__(self):
        # Conversão para unidade base (metro)
        self.to_meter = {
            "Polegada (in)": lambda x: x * 0.0254,
            "Pé (ft)": lambda x: x * 0.3048,
            "Jarda (yd)": lambda x: x * 0.9144,
            "Milha (mi)": lambda x: x * 1609.34,
        }

        # Conversão da base para SI
        self.from_meter = {
            "Quilômetro (km)": lambda x: x / 1000,
            "Metro (m)": lambda x: x,
            "Centímetro (cm)": lambda x: x * 100,
            "Milímetro (mm)": lambda x: x * 1000,
        }

    def get_available_conversions(self):
        return [(f, t) for f in self.to_meter for t in self.from_meter]

    def convert(self, from_unit, to_unit, value):
        if from_unit in self.to_meter and to_unit in self.from_meter:
            base = self.to_meter[from_unit](value)
            return self.from_meter[to_unit](base)
        raise ValueError("Conversão não suportada")
