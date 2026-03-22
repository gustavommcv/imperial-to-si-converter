# Calculadora Unitária TUI

Calculadora orientada a terminal (TUI) para conversões do Sistema Imperial para o Sistema Internacional (SI).

<img width="1086" height="574" alt="image" src="https://github.com/user-attachments/assets/daa4fb27-1091-48cb-9d67-64c7e58bab80" />

<img width="1086" height="574" alt="image" src="https://github.com/user-attachments/assets/f7279d47-3f11-45ba-ba35-c52148f436ec" />

<img width="1086" height="578" alt="image" src="https://github.com/user-attachments/assets/a16006d7-5e5d-4d05-adbd-4828c5655548" />

## Contexto Acadêmico

Projeto desenvolvido para o curso de **Engenharia Elétrica da Universidade Positivo**, como cumprimento da avaliação parcial da **Atividade Semestral 01 - Modelagem I**. 

A concepção da calculadora foi inteiramente voltada para o terminal (TUI) pela intenção do autor em priorizar a alta produtividade na navegação via teclado - ambiente altamente utilizado em *tiling window managers*, como o Hyprland. Porém, para cumprir integralmente os requisitos de **usabilidade** exigidos pelo escopo do trabalho (Slide 3), a interface também possui integração completa com interações via _mouse_.

## Estrutura do Projeto

A arquitetura do software assegura baixa dependência entre a lógica de aplicação e a sua representação em tela, baseando-se em dois pacotes fundamentais:

* `core/`: Motor matemático e dados. Trata estritamente a conversão (`conversions.py`) sem qualquer vínculo com a interação visual, contendo também testes (`test_conversions.py`) para confirmar as conversões do SI.
  * `core/units/`: Subpacote de plugins — cada arquivo (`length.py`, `mass.py`, `temperature.py`, `volume.py`) é um conversor auto-registrável via decorador.
* `ui/`: Camada de visualização, dividida em três responsabilidades:
  * `app.py`: Composição da árvore de componentes visuais.
  * `events.py`: Callbacks de eventos (`EventsMixin`) — atualização de dropdowns e cálculo ao vivo.
  * `bindings.py`: Atalhos de teclado (`KeybindsMixin`) — navegação estilo Vim (h/j/k/l, Ctrl+n/p, Esc).
  * `styles.tcss`: Estilos visuais da TUI.
* `main.py`: Ponto de execução do aplicativo.
* `build.py`: Auxiliar para exportação de um binário autônomo.

## Como as grandezas são convertidas e catalogadas?

Atualmente, o aplicativo contempla as seguintes quatro vertentes (Sistema Imperial -> SI):
- **Comprimento:** Polegada, Pé, Jarda, Milha -> Milímetro, Centímetro, Metro, Quilômetro.
- **Massa/Peso:** Onça, Libra -> Grama, Quilograma.
- **Volume:** Onça Fluida, Galão -> Mililitro, Litro.
- **Temperatura:** Fahrenheit -> Celsius.

### Como adicionar mais grandezas (Design Pattern)

A arquitetura do projeto evoluiu para ser infinitamente escalável sem esforço! Utilizamos implementações dos padrões de projeto de **Strategy** e **Registry**.  Cada grandeza reside na sua classe isolada e independente como um "Plugin" dentro da pasta `core/units/` (ex: `core/units/length.py`, `core/units/mass.py`). 

Se a sua equipe quiser adicionar conversores de **Velocidade** amanhã, você sequer precisa tocar no código das outras grandezas ou configurar telas. Basta criar um novo arquivo `core/units/speed.py`:

```python
from core.conversions import ConversionRegistry

# O decorador auto-registra sua classe nas telas da UI e nos cálculos internos magicamente!
@ConversionRegistry.register("Velocidade")
class SpeedConverter:
    def __init__(self):
        self.conversions = {
            ("Milha por hr (mph)", "Km por hr (km/h)"): lambda x: x * 1.60934,
        }
    ...
```
Qualquer novo arquivo é lido e estende as capacidades da TUI sem risco de interrupção do sistema. Um benefício massivo para o princípio do **Aberto - Fechado** do *SOLID*.

## Ambiente de Desenvolvimento e Instalação

**1.** Realizar download de dependências (Requer Python 3.10 ou superior):
```bash
pip install -r requirements.txt
```

**2.** Executar a Calculadora em fonte `.py`:
```bash
python main.py
```

**3.** Executar a Bateria de Testes Automatizados (Opcional):
Devido à arquitetura baseada em subpacotes conectáveis (`core/units`), você invoca o verificador rigoroso usando o Python em modo módulo (`-m`):
```bash
python -m core.test_conversions
```

**4.** Criar um binário final (Executável) fechado para distribuição acadêmica/uso rápido:
```bash
python build.py
```
*(O artefato será gerado na pasta `dist/imperial-to-si-converter.exe`)*
