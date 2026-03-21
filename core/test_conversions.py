import math

# A importação deve puxar do escopo global 'core.X' para que o Padrão Registry não possua erros de "Importações Relativas" ao rodar.
from core.conversions import convert, get_categories, get_conversions_for_category

def test_length_conversions():
    # 1 in = 2.54 cm
    assert math.isclose(convert("Comprimento", "Polegada (in)", "Centímetro (cm)", 10), 25.4)
    # 1 ft = 0.3048 m
    assert math.isclose(convert("Comprimento", "Pé (ft)", "Metro (m)", 1), 0.3048)
    print("Test length conversions passed.")

def test_mass_conversions():
    assert math.isclose(convert("Massa/Peso", "Onça (oz)", "Grama (g)", 1), 28.3495)
    print("Test mass conversions passed.")

def test_temperature_conversions():
    # 32F = 0C
    assert math.isclose(convert("Temperatura", "Fahrenheit (°F)", "Celsius (°C)", 32), 0.0)
    # 212F = 100C
    assert math.isclose(convert("Temperatura", "Fahrenheit (°F)", "Celsius (°C)", 212), 100.0)
    print("Test temperature conversions passed.")

def test_volume_conversions():
    assert math.isclose(convert("Volume", "Galão (gal)", "Litro (L)", 1), 3.78541)
    print("Test volume conversions passed.")

if __name__ == "__main__":
    test_length_conversions()
    test_mass_conversions()
    test_temperature_conversions()
    test_volume_conversions()
    print("All core conversion tests passed!")
