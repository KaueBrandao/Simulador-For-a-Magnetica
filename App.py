import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import math
from vpython import *

# texte
def teste():

    def mru():
        for obj in scene.objects:
            obj.visible = False

        sphere_mru = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.cyan)
        
        while sphere_mru.pos.x < 5:
            rate(100)
            sphere_mru.pos.x += 0.1

    def spiral():
        for obj in scene.objects:
            obj.visible = False

        sphere_spi = sphere(pos=vector(100,0,0), radius=10, color = color.red, make_trail=True)

        r = 100
        t= 1
        w = (2*pi)/t

        dt = 0.001
        
        while True:
            rate(150)
            t = t+dt
            p=vector(r*cos(w*t), r*sin(w*t), 20*t)
            sphere_spi.pos = p


    def mcu():
    
        for obj in scene.objects:
            obj.visible = False

        esfera = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.red)

        plano = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=5, thickness=0.1, color=color.gray(0.7))

        raio = 5 
        velocidade_angular = 2  
        omega = velocidade_angular
        t = 0  
        dt = 0.01 
        tempo_total = 5 

        while t < tempo_total:
            rate(100)  
            t += dt 
            x = raio * cos(omega * t)  
            y = raio * sin(omega * t) 
            esfera.pos = vector(x, y, 0)


    button(text="Perpendicular Â = 0 (MRU)", bind=mru, pos=scene.title_anchor)
    button(text="Espiral 0 > Â < 90", bind=spiral, pos=scene.title_anchor)
    button(text="MCU Â = 90", bind=mcu, pos=scene.title_anchor)


def TresdMRU():
    scene.title = "Movimento Retilíneo Uniforme - Esfera"
    scene.width = 800
    scene.height = 600
    scene.center = vector(0, 0, 0)

    esfera = sphere(pos=vector(-10, 0, 0), radius=1, color=color.blue, make_trail=True)

    chao = box(pos=vector(0, -1.5, 0), size=vector(30, 0.2, 5), color=color.gray(0.5))

    velocidade = vector(2, 0, 0)

    dt = 0.01  
    while esfera.pos.x < 10: 
        rate(100) 
        esfera.pos += velocidade * dt  

def TresdMCU():
    scene.title = "Movimento Circular Uniforme - Esfera"
    scene.width = 800
    scene.height = 600
    scene.center = vector(0, 0, 0)

    esfera = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.red, make_trail=True)

    plano = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=5, thickness=0.1, color=color.gray(0.7))

    raio = 5 
    velocidade_angular = 2  
    omega = velocidade_angular 
    t = 0 
    dt = 0.01
    tempo_total = 5

    while t < tempo_total:
        rate(100)
        t += dt
        x = raio * cos(omega * t)  
        y = raio * sin(omega * t) 
        esfera.pos = vector(x, y, 0)

    scene.delete()

def calcular_forca(Q, v, B, alpha):
    return Q * v * B * np.sin(np.radians(alpha))

def avaliar_expressao(expressao):
    try:
        # Substituir 'E' por '**' para notação científica e garantir que a expressão esteja em formato correto
        expressao = expressao.replace('E', '**')
        # Avaliar a expressão de forma segura
        resultado = eval(expressao)
        return resultado
    except Exception as e:
        print(f"Erro ao avaliar a expressão: {e}")
        return 0

def atualizar_grafico():
    Q = avaliar_expressao(entry_Q.get())
    v = avaliar_expressao(entry_v.get())
    B = avaliar_expressao(entry_B.get())
    alpha = avaliar_expressao(entry_alpha.get())
    F = calcular_forca(Q, v, B, alpha)

    # Limpar o gráfico anterior
    ax.clear()

    # Exibindo a carga no gráfico com até 5 casas decimais
    ax.scatter(0, 0, 0, color='b', s=500, label=f'Carga (Q={Q:.5f} C)', marker='o')

    # Calculando as componentes da força
    F_x = F * np.cos(np.radians(alpha))
    F_y = F * np.sin(np.radians(alpha))
    ax.quiver(0, 0, 0, F_x, F_y, 0, color='r', label=f"Força Magnética (F={F:.5f} N)")

    # Campo magnético
    ax.quiver(0, 0, 0, 0, 0, B, color='g', label=f"Campo Magnético (B={B:.5f} T)")

    # Velocidade
    ax.quiver(0, 0, 0, -v, 0, 0, color='orange', label=f"Velocidade (v={v:.5f} m/s)")

    # Ajustar os limites para a visualização
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Atualizar título e legenda
    ax.legend()
    ax.set_title(f"Força Magnética: {F:.5f} N")

    # Atualizar a exibição do gráfico
    canvas.draw()

# Funções de animação
def mover_perpendicular(canvas_circulo, circle):
    for _ in range(200):
        canvas_circulo.move(circle, 5, 0)  # Move o círculo para a direita
        canvas_circulo.update()
        canvas_circulo.after(10)
        if canvas_circulo.coords(circle)[2] >= 400:  # Reinicia quando atinge a borda
            canvas_circulo.coords(circle, 10, 190, 50, 230)

def mover_mcu(canvas_circulo, circle, t=0):
    x = 200 + 100 * math.cos(math.radians(t))
    y = 200 + 100 * math.sin(math.radians(t))
    canvas_circulo.coords(circle, x-20, y-20, x+20, y+20)
    canvas_circulo.update()
    if t < 360:
        canvas_circulo.after(50, mover_mcu, canvas_circulo, circle, t + 5)

# Função para abrir a janela de animação
def abrir_janela_animacao():
    janela_animacao = tk.Toplevel(root)
    janela_animacao.title("Animação do Círculo")
    
    canvas_circulo = tk.Canvas(janela_animacao, width=400, height=400, bg="white")
    canvas_circulo.pack()
    
    circle = canvas_circulo.create_oval(180, 180, 220, 220, fill="blue")
    
    btn_perpendicular = tk.Button(janela_animacao, text="Perpendicular Â = 0", 
                                  command=lambda: mover_perpendicular(canvas_circulo, circle))
    btn_perpendicular.pack(side=tk.LEFT, padx=10)
    
    btn_mcu = tk.Button(janela_animacao, text="MCU Â = 90", 
                        command=lambda: mover_mcu(canvas_circulo, circle))
    btn_mcu.pack(side=tk.RIGHT, padx=10)


root = tk.Tk()
root.title("Força Magnética 3D")

frame_principal = tk.Frame(root)
frame_principal.pack()

# Adicionar Label explicativo no topo
label_explicacao = tk.Label(frame_principal, text="Nos campos de entrada, você pode inserir expressões matemáticas usando: +, -, *, E (para notação científica).", font=("Arial", 12))
label_explicacao.pack(pady=10)

frame_controles = tk.Frame(frame_principal)
frame_controles.pack(side='left', padx=20)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=frame_principal)
canvas.get_tk_widget().pack(side='left')

# Campos de entrada
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

button_atualizar = tk.Button(frame_controles, text="Atualizar Gráfico", command=atualizar_grafico)
button_atualizar.pack()

button_animacao = tk.Button(frame_controles, text="Trajetorias", command=abrir_janela_animacao)
button_animacao.pack()

button_animacao = tk.Button(frame_controles, text="Trajetorias 3D", command=teste)
button_animacao.pack()

# Atualizar o gráfico inicial
atualizar_grafico()
root.mainloop()
