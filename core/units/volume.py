from core.conversions import ConversionRegistry


@ConversionRegistry.register("Volume")
class VolumeConverter:
    def __init__(self):
        self.to_liter = {
            "Onça Fluida (fl oz)": lambda x: x * 0.0295735,
            "Galão (gal)": lambda x: x * 3.78541,
        }

        self.from_liter = {
            "Litro (L)": lambda x: x,
            "Mililitro (ml)": lambda x: x * 1000,
        }

    def get_available_conversions(self):
        return [(f, t) for f in self.to_liter for t in self.from_liter]

    def convert(self, from_unit, to_unit, value):
        if from_unit in self.to_liter and to_unit in self.from_liter:
            base = self.to_liter[from_unit](value)
            return self.from_liter[to_unit](base)
        raise ValueError("Conversão não suportada")
