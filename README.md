# Sistema de Visualização da Força Magnética

Este repositório contém um sistema de visualização interativo desenvolvido em Python, com o objetivo de ilustrar os conceitos da força magnética, com base na fórmula da Força Magnética. O sistema permite ao usuário explorar como a carga elétrica, a velocidade da partícula, o campo magnético e o ângulo entre eles influenciam a força magnética. O sistema combina gráficos 3D e animações para uma compreensão mais intuitiva dos fenômenos eletromagnéticos.

## Funcionalidades

- **Gráfico 3D Interativo**: O usuário pode visualizar a força magnética, o campo magnético e a velocidade da partícula através de um gráfico 3D. Os vetores são representados no gráfico para ilustrar as interações entre esses elementos.
- **Controles de Entrada**: O usuário pode ajustar a carga elétrica, a velocidade da partícula, a intensidade do campo magnético e o ângulo entre a velocidade e o campo magnético por meio de sliders, observando em tempo real as mudanças no gráfico.
- **Animações**: O sistema também oferece animações para representar diferentes trajetórias da carga elétrica, incluindo movimento perpendicular e movimento circular uniforme (MCU) com base nas variações do ângulo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para o desenvolvimento do sistema.
- **Tkinter**: Biblioteca utilizada para criar a interface gráfica do usuário (GUI).
- **Matplotlib**: Usada para gerar os gráficos 3D interativos.
- **Numpy**: Biblioteca para realizar cálculos numéricos e matemáticos.
- **Math**: Para funções matemáticas, como o cálculo de seno e cosseno.
- **mpl_toolkits.mplot3d**: Para visualizações 3D no matplotlib.

## Como Executar o Sistema

1. Clone este repositório:
    ```bash
    git clone https://github.com/usuario/repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Simulador-For-a-Magnetica
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install matplotlib numpy
    ```
4. Execute o script Python:
    ```bash
    python App.py
    ```

## Como Usar

- Ao abrir o sistema, os valores iniciais são definidos para: Carga = 1 C, Velocidade = 1 m/s, Campo Magnético = 1 T e Ângulo = 30°.
- O usuário pode modificar esses valores usando os sliders.
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
