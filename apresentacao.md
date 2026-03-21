# Roteiro de Apresentação: Calculadora de Unidades TUI
**Disciplina:** Modelagem I (MSF I)
**Data da Apresentação:** 01/04/2026
**Professores:** Eduardo Cesar Amancio e Jackson Milano
**Tempo Estimado:** 5 a 10 Minutos

---

## 1. A Escolha da Interface: GUI vs TUI (Peso 1,5)
"No gigantesco mundo dos softwares, a maioria das aplicações visuais tradicionais (GUI *Graphical User Interface*) depende de motores de renderização pesados baseados em janelas. Nós optamos por uma abordagem mais minimalista e performática construindo uma **TUI** (*Terminal User Interface*). Tivemos três grandes motivos técnicos para escolher o terminal em vez das janelas comuns:

1. **Produtividade:** Em ambientes de trabalho focados em *Tiling Window Managers* (como o Hyprland no Linux), tirar a mão do teclado para usar o mouse quebra o ritmo. Nós implementamos atalhos clássicos do editor de código VIM (`h, j, k, l` e `ctrl+n`) para que a calculadora consiga ser operada apenas por teclas.
2. **Compatibilidade:** Nossa calculadora roda perfeitamente em computadores sem nenhuma interface gráfica (Servidores, SSH e terminais puros). Uma UI tradicional de janelas não rodaria nesses sistemas.
3. **Usabilidade:** Mesmo com toda essa integração mais avançada de atalhos de teclado, para cumprir perfeitamente o requisito de facilidade de uso do trabalho, nós habilitamos **suporte total ao Mouse natural do terminal**, permitindo rolagens, seleções e cliques suaves para qualquer usuário que não está familiarizado com este tipo de aplicação."
*(Neste momento, demonstre você navegando rápido com o teclado e em seguida dando um clique com o mouse no painel)*

## 2. Demonstração e Precisão Lógica (Pesos 3,0 e 1,5)
"Vocês podem notar que o funcionamento da tela não trava. Se a Grandeza não for selecionada, o resto obedece o ciclo e fica bloqueado.
*(Mostre e cite em voz alta as 4 grandezas implementadas: Comprimento, Massa, Temperatura e Volume para garantir os 2,0 pontos de Abrangência. Em seguida, converta alguns valores ao vivo!)*
Para a precisão matemática das equações, como Fahrenheit para Celsius utilizando `(X - 32) * 5/9`, nós fizemos um roteiro que roda **Testes Automatizados de Código** durante a compilação do arquivo. Eles forçam conversores contra gabaritos reais do SI com verificação decimal. Se os valores do nosso código fossem incoerentes, o programa sequer aceitaria ser gerado."

## 3. O Código: Arquitetura e Desafios (Peso 1,0)
"O back-end do software foi inteiro feito em **Python**, e a TUI gráfica usou a biblioteca **Textual**. Nós empacotamos tudo em um único `.exe` solto via PyInstaller para facilitar a distribuição.
A **maior dificuldade** da equipe foi não misturar a imensa carga de linhas que desenham o visual com a matemática de conversão. 
Nossa solução definitiva foi aplicar **Padrões de Projeto (Os famosos Design Patterns)**: A calculadora opera via *Plugins* Automáticos (*Registry Pattern*). Desenvolvemos um pacote separado (`core/units/`) onde cada arquivo abriga apenas uma grandeza única.
Se a equipe ou qualquer pessoa (O projeto é open source) quiser adicionar 'Velocidade', basta jogar um arquivo solto nessa pasta sem mudar nenhuma linha do código-fonte visual, e a calculadora injeta ele nativamente na tela."

---

## 4. Encerramento (Peso 1,0)
"Com essa arquitetura robusta entregamos a Atividade Semestral 01. Gostaríamos de encerrar por aqui e abrir para dúvidas da turma ou dos professores."