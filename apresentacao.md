# Roteiro de Apresentação: Calculadora de Unidades TUI
**Disciplina:** Modelagem I (MSF I)
**Data da Apresentação:** 01/04/2026
**Professores:** Eduardo Cesar Amancio e Jackson Milano
**Tempo Estimado:** 5 a 10 Minutos

---

## 1. A Escolha da Interface: GUI vs TUI (Peso 1,5)
"Para o desenvolvimento visual, fugimos da maioria das aplicações tradicionais (GUI) que dependem de renderizadores pesados baseados em janelas. Nós optamos por uma abordagem direta, minimalista e de alta performance construindo uma **TUI** (*Terminal User Interface*). Tivemos três motivos técnicos centrais para escolher o terminal:

1. **Produtividade Nativa:** Em ambientes de trabalho focados em *Tiling Window Managers* (como o Hyprland no Linux), tirar a mão do teclado para usar o mouse quebra o ritmo. Nós implementamos atalhos clássicos do editor VIM (`h, j, k, l` e `ctrl+n`) para que a calculadora consiga ser operada apenas por teclas.
2. **Compatibilidade Headless:** Nossa calculadora roda perfeitamente em computadores sem nenhuma interface gráfica (como Servidores, instâncias SSH e terminais puros). Uma UI de janelas quebraria e não rodaria nesses sistemas.
3. **Usabilidade Universal:** Mesmo com a integração avançada de atalhos de teclado, precisávamos cumprir a métrica de facilidade de uso do trabalho. Por isso, habilitamos **suporte total ao Mouse nativo do terminal**. Isso permite rolagens, seleções e cliques suaves para qualquer pessoa que não esteja acostumada com navegação via terminal."

*(Dica: Neste momento, demonstre você navegando rápido com o teclado e em seguida dando um clique com o mouse no painel)*

## 2. Demonstração e Precisão Lógica (Pesos 3,0 e 1,5)
"Como vocês podem ver, a tela lida com exceções e não trava em cliques arbitrários. Se nenhuma Grandeza inicial é selecionada, todo o resto obedece o ciclo lógico e fica bloqueado.

*(Mostre as opções e cite as 4 grandezas implementadas: Comprimento, Massa, Temperatura e Volume, para garantir os 2,0 pontos de Abrangência. Em seguida, converta alguns valores ao vivo nas áreas testadas)*

Sobre a precisão matemática das equações, como de Fahrenheit para Celsius usando `(X - 32) * 5/9`: Nós construímos e rodamos **Testes Automatizados** isolados que valem baseados em asserções decimais. Isso significa que, se as fórmulas matemáticas estivessem erradas ou o cálculo não batesse exatamente com a margem do SI, o nosso projeto sequer conseguia ser executado e compilado."

## 3. Arquitetura do Código e Desafios (Peso 1,0)
"Na parte técnica, o código inteiro rodou em **Python** e usamos a biblioteca **Textual** para gerenciar a visão TUI. Para facilitar a distribuição, usamos o PyInstaller e unimos todo o projeto diretamente num único executável (`.exe`).

Nosso **maior desafio** foi manter o código organizado, estruturando-o de uma forma em que a própria lógica matemática não virasse bagunça no meio das linhas responsáveis por desenhar a tela.
Para resolver isso, nós aplicamos um Padrão de Projeto de engenharia estrutural: isolamos componentes matemáticos em *Plugins* (usando o Registry Pattern).
Criamos uma pasta separada (`core/units/`) onde cada grandeza vive num arquivo único e exclusivo. Como o nosso projeto é Open-Source e disponível no GitHub, essa arquitetura se mostra ideal. Se amanhã qualquer pessoa da comunidade quiser criar uma conversão de Densidade ou Velocidade, basta adicionar um novo arquivo lá e ele entrará na calculadora automaticamente, sem risco de quebrar a interface gráfica atual."

---

## 4. Encerramento (Peso 1,0)
"Sendo assim, encerramos por aqui a entrega da nossa Atividade Semestral de Modelagem. Estamos completamente abertos caso a turma ou os professores tenham alguma dúvida sobre o código ou a interface."