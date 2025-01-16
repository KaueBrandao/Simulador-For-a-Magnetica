import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import math
from vpython import *

# Função que exibe animações 3D representando diferentes trajetórias de partículas carregadas
# Cada trajetória depende da interação entre o campo magnético, velocidade da partícula e o ângulo entre eles
def teste():

    # Animação para o Movimento Retilíneo Uniforme (MRU)
    def mru():
        for obj in scene.objects:
            obj.visible = False  # Limpa objetos anteriores na cena

        # Cria uma esfera que se move em linha reta ao longo do eixo X
        sphere_mru = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.cyan)

        while sphere_mru.pos.x < 5:  # Movimento até alcançar a posição final
            rate(100)
            sphere_mru.pos.x += 0.1

    # Animação de uma espiral, representando trajetória com ângulo intermediário (0° < α < 90°)
    def spiral():
        for obj in scene.objects:
            obj.visible = False

        # Cria uma esfera que deixa um rastro enquanto segue uma trajetória em espiral
        sphere_spi = sphere(pos=vector(100, 0, 0), radius=10, color=color.red, make_trail=True)

        r = 100  # Raio inicial
        t = 1  # Tempo inicial
        w = (2 * pi) / t  # Frequência angular
        dt = 0.001  # Incremento de tempo

        while True:  # Movimento contínuo
            rate(150)
            t += dt
            p = vector(r * cos(w * t), r * sin(w * t), 20 * t)  # Atualiza posição
            sphere_spi.pos = p

    # Animação para o Movimento Circular Uniforme (MCU) com α = 90°
    def mcu():
        for obj in scene.objects:
            obj.visible = False

        # Cria uma esfera que se move ao longo de um anel representando o plano do movimento
        esfera = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.red)
        plano = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=5, thickness=0.1, color=color.gray(0.7))

        raio = 5
        velocidade_angular = 2
        omega = velocidade_angular  # Frequência angular
        t = 0  # Tempo inicial
        dt = 0.01  # Incremento de tempo
        tempo_total = 5  # Duração da animação

        while t < tempo_total:
            rate(100)
            t += dt
            x = raio * cos(omega * t)  # Coordenada X
            y = raio * sin(omega * t)  # Coordenada Y
            esfera.pos = vector(x, y, 0)

    # Botões para selecionar diferentes animações na interface 3D
    button(text="Perpendicular Â = 0 (MRU)", bind=mru, pos=scene.title_anchor)
    button(text="Espiral 0 > Â < 90", bind=spiral, pos=scene.title_anchor)
    button(text="MCU Â = 90", bind=mcu, pos=scene.title_anchor)

# Animação 3D para o Movimento Retilíneo Uniforme
def TresdMRU():
    scene.title = "Movimento Retilíneo Uniforme - Esfera"
    scene.width = 800
    scene.height = 600
    scene.center = vector(0, 0, 0)

    # Criação da esfera e do plano de movimento
    esfera = sphere(pos=vector(-10, 0, 0), radius=1, color=color.blue, make_trail=True)
    chao = box(pos=vector(0, -1.5, 0), size=vector(30, 0.2, 5), color=color.gray(0.5))

    velocidade = vector(2, 0, 0)  # Vetor velocidade
    dt = 0.01  # Incremento de tempo

    while esfera.pos.x < 10:  # Movimento em linha reta
        rate(100)
        esfera.pos += velocidade * dt

# Animação 3D para o Movimento Circular Uniforme
def TresdMCU():
    scene.title = "Movimento Circular Uniforme - Esfera"
    scene.width = 800
    scene.height = 600
    scene.center = vector(0, 0, 0)

    # Criação da esfera e do plano de movimento
    esfera = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.red, make_trail=True)
    plano = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=5, thickness=0.1, color=color.gray(0.7))

    raio = 5
    velocidade_angular = 2
    omega = velocidade_angular  # Frequência angular
    t = 0
    dt = 0.01
    tempo_total = 5

    while t < tempo_total:
        rate(100)
        t += dt
        x = raio * cos(omega * t)  # Coordenada X
        y = raio * sin(omega * t)  # Coordenada Y
        esfera.pos = vector(x, y, 0)

    scene.delete()  # Limpa a cena ao final

# Cálculo da força magnética com base nos parâmetros fornecidos
def calcular_forca(Q, v, B, alpha):
    return Q * v * B * np.sin(np.radians(alpha))

# Avaliação de expressões matemáticas fornecidas pelo usuário
def avaliar_expressao(expressao):
    try:
        expressao = expressao.replace('E', '**')  # Ajusta notação científica
        resultado = eval(expressao)  # Avalia a expressão
        return resultado
    except Exception as e:
        print(f"Erro ao avaliar a expressão: {e}")
        return 0

# Atualiza o gráfico 3D baseado nos parâmetros da força magnética
def atualizar_grafico():
    Q = avaliar_expressao(entry_Q.get())
    v = avaliar_expressao(entry_v.get())
    B = avaliar_expressao(entry_B.get())
    alpha = avaliar_expressao(entry_alpha.get())
    F = calcular_forca(Q, v, B, alpha)

    # Limpa o gráfico anterior
    ax.clear()

    # Plota a carga como um ponto azul
    ax.scatter(0, 0, 0, color='b', s=500, label=f'Carga (Q={Q:.5f} C)', marker='o')

    # Calcula e exibe as componentes da força magnética
    F_x = F * np.cos(np.radians(alpha))
    F_y = F * np.sin(np.radians(alpha))
    ax.quiver(0, 0, 0, F_x, F_y, 0, color='r', label=f"Força Magnética (F={F:.5f} N)")

    # Exibe o campo magnético e a velocidade
    ax.quiver(0, 0, 0, 0, 0, B, color='g', label=f"Campo Magnético (B={B:.5f} T)")
    ax.quiver(0, 0, 0, -v, 0, 0, color='orange', label=f"Velocidade (v={v:.5f} m/s)")

    # Ajusta os limites e exibe o gráfico
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.legend()
    ax.set_title(f"Força Magnética: {F:.5f} N")
    canvas.draw()

# Abre janela com animações 2D representando trajetórias
def abrir_janela_animacao():
    janela_animacao = tk.Toplevel(root)
    janela_animacao.title("Animação do Círculo")

    canvas_circulo = tk.Canvas(janela_animacao, width=400, height=400, bg="white")
    canvas_circulo.pack()

    circle = canvas_circulo.create_oval(180, 180, 220, 220, fill="blue")

    # Botões para movimentos 2D
    btn_perpendicular = tk.Button(janela_animacao, text="Perpendicular Â = 0",
                                  command=lambda: mover_perpendicular(canvas_circulo, circle))
    btn_perpendicular.pack(side=tk.LEFT, padx=10)

    btn_mcu = tk.Button(janela_animacao, text="MCU Â = 90",
                        command=lambda: mover_mcu(canvas_circulo, circle))
    btn_mcu.pack(side=tk.RIGHT, padx=10)

# Interface principal para entrada de parâmetros e visualização do gráfico 3D
root = tk.Tk()
root.title("Força Magnética 3D")

frame_principal = tk.Frame(root)
frame_principal.pack()

# Label explicativa sobre entradas matemáticas
label_explicacao = tk.Label(frame_principal, text="Insira expressões matemáticas usando: +, -, *, E (notação científica).", font=("Arial", 12))
label_explicacao.pack(pady=10)

frame_controles = tk.Frame(frame_principal)
frame_controles.pack(side='left', padx=20)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=frame_principal)
canvas.get_tk_widget().pack(side='left')

# Campos para entrada de valores
label_Q = tk.Label(frame_controles, text="Carga (Q) [Coulombs]")
label_Q.pack()
entry_Q = tk.Entry(frame_controles)
entry_Q.insert(0, "1")
entry_Q.pack()

label_v = tk.Label(frame_controles, text="Velocidade (v) [m/s]")
label_v.pack()
entry_v = tk.Entry(frame_controles)
entry_v.insert(0, "1")
entry_v.pack()

label_B = tk.Label(frame_controles, text="Campo Magnético (B) [T]")
label_B.pack()
entry_B = tk.Entry(frame_controles)
entry_B.insert(0, "1")
entry_B.pack()

label_alpha = tk.Label(frame_controles, text="Ângulo (α) [graus]")
label_alpha.pack()
entry_alpha = tk.Entry(frame_controles)
entry_alpha.insert(0, "30")
entry_alpha.pack()

# Botões para interagir com o sistema
button_atualizar = tk.Button(frame_controles, text="Atualizar Gráfico", command=atualizar_grafico)
button_atualizar.pack()

button_animacao = tk.Button(frame_controles, text="Trajetorias", command=abrir_janela_animacao)
button_animacao.pack()

button_animacao = tk.Button(frame_controles, text="Trajetorias 3D", command=teste)
button_animacao.pack()

# Exibição inicial do gráfico
atualizar_grafico()
root.mainloop()
