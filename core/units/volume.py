from core.conversions import ConversionRegistry

@ConversionRegistry.register("Volume")
class VolumeConverter:
    def __init__(self):
        self.conversions = {
            ("Onça Fluida (fl oz)", "Mililitro (ml)"): lambda x: x * 29.5735,
            ("Galão (gal)", "Litro (L)"): lambda x: x * 3.78541,
        }

    def get_available_conversions(self):
        return list(self.conversions.keys())

    def convert(self, from_unit: str, to_unit: str, value: float):
        func = self.conversions.get((from_unit, to_unit))
        if func:
            return func(value)
        raise ValueError(f"Conversão de '{from_unit}' para '{to_unit}' em Volume não suportada.")
