# Snake Game em Pygame e OpenGL

Este é um exemplo de código em Python que implementa o clássico jogo Snake
usando as bibliotecas Pygame e OpenGL. O jogo é executado em uma janela de
tamanho fixo e utiliza retângulos para representar a cobra e a comida. A
cobra cresce ao comer a comida e o jogo termina se a cobra colidir com as
bordas da janela ou com seu próprio corpo.

## Requisitos

- Python 3.x
- Pygame
- PyOpenGL

Certifique-se de ter as bibliotecas Pygame e PyOpenGL instaladas em seu
ambiente Python antes de executar o código.

## Instalação das bibliotecas Pygame e PyOpenGL

Para instalar as bibliotecas Pygame e PyOpenGL usando o pip, siga os
passos abaixo:

1. Abra o terminal ou prompt de comando.

2. Certifique-se de que você tenha o Python e o pip instalados corretamente
em seu sistema.

3. Para instalar o Pygame, execute o seguinte comando:
    
    ```sh
    pip install pygame
    ```

4. Para instalar o PyOpenGL, execute o seguinte comando:

    ```sh
    pip install PyOpenGL
    ```


## Como Jogar

- Use as setas do teclado para mover a cobra para cima, para baixo, para a
esquerda ou para a direita.
- O objetivo é comer a comida para fazer a cobra crescer e evitar colidir com
as bordas da janela ou com o próprio corpo.
- O jogo termina quando a cobra colide com uma dessas condições e exibe uma
tela de game over por 1 segundo antes de reiniciar.

## Executando o Jogo

Para executar o jogo, certifique-se de ter as bibliotecas Pygame e PyOpenGL
instaladas e execute o arquivo Python:

```sh 
python3 snake.py
```

A janela do jogo será aberta e você poderá começar a jogar usando as setas
do teclado.

**Observação:** Lembre-se de que este código é apenas um exemplo e pode ser
expandido e aprimorado de várias maneiras, como adicionar níveis de
dificuldade, pontuação e melhorar a experiência do usuário.