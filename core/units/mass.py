from core.conversions import ConversionRegistry


@ConversionRegistry.register("Massa/Peso")
class MassConverter:
    def __init__(self):
        self.to_kg = {
            "Onça (oz)": lambda x: x * 0.0283495,
            "Libra (lb)": lambda x: x * 0.453592,
        }

        self.from_kg = {
            "Quilograma (kg)": lambda x: x,
            "Grama (g)": lambda x: x * 1000,
            "Miligrama (mg)": lambda x: x * 1_000_000,
        }

    def get_available_conversions(self):
        return [(f, t) for f in self.to_kg for t in self.from_kg]

    def convert(self, from_unit, to_unit, value):
        if from_unit in self.to_kg and to_unit in self.from_kg:
            base = self.to_kg[from_unit](value)
            return self.from_kg[to_unit](base)
        raise ValueError("Conversão não suportada")
