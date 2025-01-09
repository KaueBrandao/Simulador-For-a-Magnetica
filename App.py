import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import math

# Função para calcular a força magnética
def calcular_forca(Q, v, B, alpha):
    return Q * v * B * np.sin(np.radians(alpha))

# Função para atualizar o gráfico
def atualizar_grafico():
    Q = slider_Q.get()
    v = slider_v.get()
    B = slider_B.get()
    alpha = slider_alpha.get()
    F = calcular_forca(Q, v, B, alpha)
    
    ax.clear()
    
    # Representando a carga no centro do gráfico
    ax.scatter(0, 0, 0, color='b', s=500, label=f'Carga (Q={Q:.2f} C)', marker='o')
    5
    # Representando a força magnética como uma seta
    F_x = F * np.cos(np.radians(alpha))
    F_y = F * np.sin(np.radians(alpha))
    ax.quiver(0, 0, 0, F_x, F_y, 0, color='r', label=f"Força Magnética (F={F:.2f} N)")
    
    # Representando o campo magnético como uma seta no eixo Z
    ax.quiver(0, 0, 0, 0, 0, B, color='g', label=f"Campo Magnético (B={B:.2f} T)")
    
    # Representando a velocidade como uma seta no eixo X
    ax.quiver(0, 0, 0, -v, 0, 0, color='orange', label=f"Velocidade (v={v:.2f} m/s)")
    
    # Configurações do gráfico
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    ax.set_title(f"Força Magnética: {F:.2f} N")
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

# Criando a janela principal
root = tk.Tk()
root.title("Força Magnética 3D")

frame_principal = tk.Frame(root)
frame_principal.pack()

frame_controles = tk.Frame(frame_principal)
frame_controles.pack(side='left', padx=20)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=frame_principal)
canvas.get_tk_widget().pack(side='left')

label_Q = tk.Label(frame_controles, text="Carga (Q) [Coulombs]")
label_Q.pack()
slider_Q = tk.Scale(frame_controles, from_=0, to_=10, orient='horizontal')
slider_Q.set(1)
slider_Q.pack()

label_v = tk.Label(frame_controles, text="Velocidade (v) [m/s]")
label_v.pack()
slider_v = tk.Scale(frame_controles, from_=0, to_=10, orient='horizontal')
slider_v.set(1)
slider_v.pack()

label_B = tk.Label(frame_controles, text="Campo Magnético (B) [T]")
label_B.pack()
slider_B = tk.Scale(frame_controles, from_=0, to_=10, orient='horizontal')
slider_B.set(1)
slider_B.pack()

label_alpha = tk.Label(frame_controles, text="Ângulo (α) [graus]")
label_alpha.pack()
slider_alpha = tk.Scale(frame_controles, from_=0, to_=90, orient='horizontal')
slider_alpha.set(30)
slider_alpha.pack()

button_atualizar = tk.Button(frame_controles, text="Atualizar Gráfico", command=atualizar_grafico)
button_atualizar.pack()

button_animacao = tk.Button(frame_controles, text="Trajetorias", command=abrir_janela_animacao)
button_animacao.pack()

atualizar_grafico()
root.mainloop()
