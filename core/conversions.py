from enum import Enum
from typing import Callable, Dict, Tuple, List

class UnitCategory(Enum):
    LENGTH = "Comprimento"
    MASS = "Massa/Peso"
    TEMPERATURE = "Temperatura"
    VOLUME = "Volume"

# Estrutura de conversões do Sistema Imperial para o Internacional (SI)
# Categoria -> { (Unidade de Origem, Unidade de Destino) : Função de Conversão }
CONVERSIONS: Dict[UnitCategory, Dict[Tuple[str, str], Callable[[float], float]]] = {
    UnitCategory.LENGTH: {
        ("Polegada (in)", "Centímetro (cm)"): lambda x: x * 2.54,
        ("Pé (ft)", "Metro (m)"): lambda x: x * 0.3048,
        ("Jarda (yd)", "Metro (m)"): lambda x: x * 0.9144,
        ("Milha (mi)", "Quilômetro (km)"): lambda x: x * 1.60934,
    },
    UnitCategory.MASS: {
        ("Onça (oz)", "Grama (g)"): lambda x: x * 28.3495,
        ("Libra (lb)", "Quilograma (kg)"): lambda x: x * 0.453592,
    },
    UnitCategory.TEMPERATURE: {
        ("Fahrenheit (°F)", "Celsius (°C)"): lambda x: (x - 32) * 5.0 / 9.0,
    },
    UnitCategory.VOLUME: {
        ("Onça Fluida (fl oz)", "Mililitro (ml)"): lambda x: x * 29.5735,
        ("Galão (gal)", "Litro (L)"): lambda x: x * 3.78541,
    }
}

def get_categories() -> List[str]:
    """Retorna uma lista de strings com todas as categorias disponíveis."""
    return [c.value for c in UnitCategory]

def get_conversions_for_category(category_name: str) -> List[Tuple[str, str]]:
    """
    Dado o nome de uma categoria, retorna uma lista de tuplas
    com as possíveis conversões (De, Para).
    """
    for c in UnitCategory:
        if c.value == category_name:
            return list(CONVERSIONS[c].keys())
    return []

def convert(category_name: str, from_unit: str, to_unit: str, value: float) -> float:
    """
    Realiza a conversão de uma unidade para outra.
    Lança ValueError caso não encontre a operação.
    """
    for c in UnitCategory:
        if c.value == category_name:
            func = CONVERSIONS[c].get((from_unit, to_unit))
            if func:
                return func(value)
    raise ValueError(f"Conversão de '{from_unit}' para '{to_unit}' em '{category_name}' não suportada.")
