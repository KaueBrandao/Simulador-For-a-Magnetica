# Sistema de Visualização da Força Magnética

Este repositório contém um sistema interativo que simula o movimento de partículas carregadas sob a influência de um campo magnético. O sistema é desenvolvido em Python, utilizando bibliotecas como `vpython` para animações 3D, `matplotlib` para gráficos e `tkinter` para a interface gráfica de usuário (GUI).

# Telas do Sistema
![Tela1](/tela1.PNG)
![Tela1](/tela2.PNG)

## Descrição

O sistema visualiza diferentes tipos de trajetórias de partículas carregadas em um campo magnético, incluindo:

- **Movimento Retilíneo Uniforme (MRU)**
- **Movimento Circular Uniforme (MCU)**
- **Movimento Espiral (ângulo intermediário entre 0° e 90°)**

Além disso, o código permite o cálculo da força magnética aplicada a uma carga em movimento através da fórmula:

F = Q V B sin(alpha)

Onde:
- \( Q \) é a carga elétrica (Coulombs)
- \( v \) é a velocidade da partícula (m/s)
- \( B \) é a intensidade do campo magnético (Tesla)
- \( \alpha \) é o ângulo entre a direção da velocidade e a do campo magnético (graus)

## Funcionalidades

- **Interface Gráfica**: Uma interface com entradas para os parâmetros físicos da força magnética.
- **Animações 3D**: Exibição de movimentos de partículas, incluindo MRU, MCU e espiral.
- **Gráficos Interativos**: Visualização da força magnética em um gráfico 3D.
- **Cálculos Automáticos**: Cálculo da força magnética baseado nas entradas fornecidas pelo usuário.

## Pré-requisitos

Para rodar o sistema, é necessário ter as seguintes bibliotecas instaladas:

- Python 3.x
- vpython
- matplotlib
- tkinter
- numpy

Você pode instalar as dependências utilizando o `pip`:

```bash
pip install vpython matplotlib numpy


## Como Executar o Sistema

1. Clone este repositório:
    ```bash
    git clone https://github.com/KaueBrandao/Simulador-For-a-Magnetica.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Simulador-For-a-Magnetica
    ```
3. Execute o script Python:
    ```bash
    python App.py
    ```

## Como Usar

- Ao abrir o sistema, os valores iniciais são definidos para: Carga = 1 C, Velocidade = 1 m/s, Campo Magnético = 1 T e Ângulo = 30°.
- O usuário pode modificar esses valores usando os campos de entrada.
- Após ajustar os valores, clique em "Atualizar Gráfico" para visualizar a alteração no gráfico 3D.
- O botão "Trajetórias" permite visualizar animações com diferentes ângulos, representando o movimento da carga elétrica.

## Contribuições

Se você deseja contribuir com melhorias para o projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch para suas modificações.
3. Faça suas alterações e commit com uma mensagem clara.
4. Abra um pull request para revisão.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
