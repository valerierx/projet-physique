import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

from numba.scripts.generate_lower_listing import description

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--realiste',
                    action='store_true', help="Utilise un potentiel plus réaliste")
args = parser.parse_args()


# Variable 
dt = 1e-7
dx = 0.001
nx = int(1 / dx) * 2
nt = 90000 #durée de la simulation
nd = int(nt / 1000) + 1  # nombre d'images dans l'animation
s = dt / (dx ** 2)
xc = 0.6 #Position du paquet d'onde au depart
sigma = 0.05 #largeur du paquet (décrit sa dispersion spatiale)
A = 1 / (math.sqrt(sigma * math.sqrt(math.pi))) # Constante de normalisation
v0 = -4000 # puit
h_bar= 1.054571817e-34 # Constante de planck de réduite 
e = (1/2)*(pow((np.pi*h_bar)/0.1, 2)*v0) #Niveau d'énergie trouver analytiquement pour n = 1
E = e * v0 - v0 #energie cinétique 
k = math.sqrt(2 * abs(E)) #Nombre d'onde

#  Initialisation des tableaux
def init_simulation():
    o = np.linspace(0, (nx - 1) * dx, nx) #Vecteur des positions x de taille nx
    V = np.zeros(nx)
    if args.realiste:
        V = v0 * np.exp(-((o - 0.85) ** 2) / (2 * 0.02 ** 2)) # ici on utilise un potentiel dit plus réaliste
    else:
        V[(o >= 0.8) & (o <= 0.9)] = v0 # potentiel = V0 si x appartenant à [0.8, 0.9]

    
    cpt = A * np.exp(1j * k * o - ((o - xc) ** 2) / (2 * sigma ** 2)) #Equation d'onde 
    re = np.real(cpt)
    im = np.imag(cpt)
    densite = np.zeros((nt, nx))
    densite[0, :] = np.abs(cpt) ** 2
    return o, V, re, im, densite

# Evolution du paquet d'onde
def paquet_onde(V, re, im, densite):
    b = np.zeros(nx)
    for i in range(1, nt):
        if i % 2 != 0:
            b[1:-1] = im[1:-1]
            im[1:-1] += s * (re[2:] + re[:-2]) - 2 * re[1:-1] * (s + V[1:-1] * dt)
            densite[i, 1:-1] = re[1:-1] ** 2 + im[1:-1] * b[1:-1]
        else:
            re[1:-1] -= s * (im[2:] + im[:-2]) - 2 * im[1:-1] * (s + V[1:-1] * dt)
    return densite

# Récupération de donné pour l'animation 
def Compil_animation(densite):
    final_densite = np.zeros((nd, nx))
    for i in range(1, nt):
        if (i - 1) % 1000 == 0:
            frame = int((i - 1) / 1000)
            final_densite[frame][:] = densite[i][:]
    return final_densite

# Animation 
def animate(j):
    line.set_data(o, final_densite[j, :])
    return line,

def init_plot():
    line.set_data([], [])
    return line,

# Main
def main():
    global o, final_densite, line

    o, V, re, im, densite = init_simulation()
    densite = paquet_onde(V, re, im, densite)
    final_densite = Compil_animation(densite)

    plot_title = f"Marche Ascendante avec E/V0 = {e}"
    fig = plt.figure()
    line, = plt.plot([], [])
    plt.ylim(-13, 13)
    plt.xlim(0, 2)
    plt.plot(o, V, label="Potentiel")
    plt.title(plot_title)
    plt.xlabel("x")
    plt.ylabel("Densité de probabilité de présence")
    plt.legend()

    ani = animation.FuncAnimation(fig, animate, init_func=init_plot, frames=nd, blit=False, interval=100, repeat=False)
    plt.show()

# Lancement 
if __name__ == "__main__":
    main()
