# Calculadora Unitária TUI

Calculadora orientada a terminal (TUI) para conversões do Sistema Imperial para o Sistema Internacional (SI).

## Contexto Acadêmico

Projeto desenvolvido para o curso de **Engenharia Elétrica da Universidade Positivo**, como cumprimento da avaliação parcial da **Atividade Semestral 01 - Modelagem I**. 

A concepção da calculadora foi inteiramente voltada para o terminal (TUI) pela intenção do autor em priorizar a alta produtividade na navegação via teclado - ambiente altamente utilizado em *tiling window managers*, como o Hyprland. Porém, para cumprir integralmente os requisitos de **usabilidade** exigidos pelo escopo do trabalho (Slide 3), a interface também possui integração completa com interações via _mouse_.

## Estrutura do Projeto

A arquitetura do software assegura baixa dependência entre a lógica de aplicação e a sua representação em tela, baseando-se em dois pacotes fundamentais:

* `core/`: Motor matemático e dados. Trata estritamente a conversão (`conversions.py`) sem qualquer vínculo com a interação visual, contendo também testes (`test_conversions.py`) para confirmar as conversões do SI.
* `ui/`: Controlador de visualização e eventos (`app.py`), e seu respectivo escopo visual (`styles.tcss`).
* `main.py`: Ponto de execução do aplicativo.
* `build.py`: Auxiliar para exportação de um binário autônomo.

## Como as grandezas são convertidas e catalogadas?

Atualmente, o aplicativo contempla as seguintes quatro vertentes (Sistema Imperial -> SI):
- **Comprimento:** Polegada, Pé, Jarda, Milha -> Centímetro, Metro, Quilômetro.
- **Massa/Peso:** Onça, Libra -> Grama, Quilograma.
- **Volume:** Onça Fluida, Galão -> Mililitro, Litro.
- **Temperatura:** Fahrenheit -> Celsius.

### Como adicionar ou alterar mais conversões:

Para inserir uma grandeza ou novas modalidades em uma categoria já formatada, você precisa editar apenas uma única estrutura de dados, o dicionário `CONVERSIONS` no arquivo localizado em `core/conversions.py`.

```python
# Categoria -> { (Unidade de Origem, Unidade de Destino) : Expressão Lambda de Conversão }
UnitCategory.LENGTH: {
    ("Polegada (in)", "Centímetro (cm)"): lambda x: x * 2.54,
    ...
```
Qualquer alteração feita no dicionário `CONVERSIONS` será lida e automaticamente renderizada como um novo item de escolha na interface de terminal do próprio _app_, não sendo necessário alterar arquivos de configuração visual nem a arquitetura da UI.

## Ambiente de Desenvolvimento e Instalação

**1.** Realizar download de dependências (Requer Python 3.10 ou superior):
```bash
pip install -r requirements.txt
```

**2.** Executar a Calculadora em fonte `.py`:
```bash
python main.py
```

**3.** Criar um binário final (Executável) fechado para distribuição acadêmica/uso rápido:
```bash
python build.py
```
*(O artefato será gerado na pasta `dist/Calculadora_Unidades.exe`)*
