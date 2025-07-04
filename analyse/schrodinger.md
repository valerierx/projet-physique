---
author:
- ROUX
- Yanis KASSOU, Gweltaz COLLIN et Valérie ROUX
date: Juin 2025
title: |
  **CY Tech\
  Projet numérique**
---

# Résolution analytique

$$V(x) = \begin{cases}
-V_0 & \text{si } 0 \leq x \leq a \\
0 & \text{sinon}
\end{cases}$$

Equation de Schrödinger indépendante du temps
$$\frac{d^2\Psi}{dx^2} + \frac{2m}{\hbar^2}(E-V(x))\Psi = 0$$

## Région 1: $x < 0$ (Avant le puits)

Soit $k_1 = \sqrt{\frac{2mE}{\hbar^2}}$

$$\Rightarrow \frac{d^2\Psi}{dx^2} + k_1^2\Psi = 0$$

Soit $\tilde{\Psi} = \tilde{\Psi_0}e^{rx}$

$$\Rightarrow \tilde{\Psi_0}e^{rx}(r^2 + k_1^2) = 0$$

or $\forall x \in \mathbb{R}, \tilde{\Psi_0}e^{rx} \neq 0$

$$\Rightarrow r^2 + k_1^2 = 0$$

$$\Rightarrow r = \pm ik_1$$

Ainsi les deux solutions de l'Ansatz sont

$$\tilde{\Psi_1}(x) = e^{ik_1x}, \tilde{\Psi_2}(x) = e^{-ik_1x}$$

La solution générale est une combinaison linéaire entre $\tilde{\Psi_1}$
et $\tilde{\Psi_2}$

$$\tilde{\Psi_1}(x) = \tilde{A_1}e^{ik_1x} + \tilde{B_1}e^{-ik_1x}, k_1 = \sqrt{\frac{2mE}{\hbar^2}}$$

$$\Rightarrow \Psi_I(x) = A_1e^{ik_1x} + B_1e^{-ik_1x}$$

## Région 2: $0 \leq x \leq a$

$$V(x) = -V_0 \Rightarrow \frac{d^2\Psi}{dx^2} + \frac{2m(E+V_0)}{\hbar^2}\Psi = 0$$

$$\text{Soit } k_2^2 = \frac{2m(E+V_0)}{\hbar^2}$$

$$\tilde{\Psi}(x) = \tilde{\Psi_0}e^{rx}$$

$$\Rightarrow \tilde{\Psi_0}e^{rx}(r^2 + k_2^2) = 0$$

$$\forall x \in \mathbb{R}, \tilde{\Psi_0}e^{rx} \neq 0$$

$$\Rightarrow r^2 + k_2^2 = 0$$

$$\Rightarrow r = \pm ik_2$$

Ainsi, les deux solutions sont :

$$\tilde{\Psi}_3(x) = e^{ik_2x}, \tilde{\Psi}_4(x) = e^{-ik_2x}$$

La solution générale est une combinaison linéaire

$$\tilde{\Psi}_{II}(x) = \tilde{A}_2 e^{ik_2x} + \tilde{B}_2 e^{-ik_2x}$$

$$\Rightarrow \Psi_{II}(x) = A_2 e^{ik_2x} + B_2 e^{-ik_2x}$$

## Région 3: $x > a$

$$V(x) = 0 \Rightarrow \frac{d^2\Psi}{dx^2} + k_1^2\Psi = 0$$

$$\tilde{\Psi}(x) = \tilde{\Psi}_0 e^{rx}$$

$$\Rightarrow \tilde{\Psi}_0 e^{rx}(r^2 + k_1^2) = 0$$

$$\forall x \in \mathbb{R}, \tilde{\Psi}_0 e^{rx} \neq 0$$

$$\Rightarrow r^2 + k_1^2 = 0$$

$$\Rightarrow r = \pm ik_1$$

$$\tilde{\Psi}_5(x) = e^{ik_1x}, \tilde{\Psi}_6(x) = e^{-ik_1x}$$

Or il n'y a pas d'ondes incidentes venant de $+\infty$. On a:

$$\Rightarrow \tilde{\Psi}_{III}(x) = \tilde{A}_3 e^{ik_1x}$$

$$\Rightarrow \Psi_{III}(x) = A_3 e^{ik_1x}$$

# Conditions de continuité

$$\begin{aligned}
\Psi_I(x\to0) &= \Psi_{II}(x\to0) \\
A_1 + B_1 &= A_2 + B_2 \\
\left.\frac{\partial \Psi_I}{\partial x}\right|_{x=0} &= \left.\frac{\partial \Psi_{II}}{\partial x}\right|_{x=0} \\
k_1 A_1 - k_1 B_1 &= k_2 A_2 - k_2 B_2 \\
\Psi_{II}(x\to a) &= \Psi_{III}(x\to a) \\
A_2 e^{ik_2a} + B_2 e^{-ik_2a} &= A_3 e^{ik_1a} \\
\left.\frac{\partial \Psi_{II}}{\partial x}\right|_{x=a} &= \left.\frac{\partial \Psi_{III}}{\partial x}\right|_{x=a} \\
ik_2(A_2e^{ik_2a} - B_2e^{-ik_2a}) &= ik_1A_3e^{ik_1a}
\end{aligned}$$

$$\begin{cases}
A_1 + B_1 = A_2 + B_2 & (1) \\
k_1A_1 - k_1B_1 = k_2A_2 - k_2B_2 & (2) \\
A_2e^{ik_2a} + B_2e^{-ik_2a} = A_3e^{ik_1a} & (3) \\
k_2A_2e^{ik_2a} - B_2e^{-ik_2a} = k_1A_3e^{ik_1a} & (4)
\end{cases}$$

Le but est de trouver les amplitudes:

$$\frac{A_2}{A_1}, \frac{B_2}{A_2}, \frac{A_3}{A_2}, \frac{B_2}{A_2}$$

Dans le cadre de l'effet Ramsauer-Townsend on observe que l'électron
traverse l'atome sans être dévié pour certaines énergies. Cela signifie
qu'il n'y a pas d'onde réfléchie. Ainsi,

$$R = \frac{|B_1|^2}{|A_1|^2} = 0$$

$$\Rightarrow |B_1|^2 = 0 \Rightarrow B_1 = 0$$

Donc:

$$\begin{cases}
A_1 = A_2 + B_2 & (1) \\
k_1 A_1 = k_2 A_2 - k_2 B_2 & (2) \quad L_2 \leftarrow \frac{1}{k_2}L_2
\end{cases}$$

$$\Leftrightarrow \begin{cases}
A_1 = A_2 + B_2 \\
\frac{k_1}{k_2} A_1 = A_2 - B_2 \quad L_2 \leftarrow L_2 + L_1
\end{cases}$$

$$\Leftrightarrow \begin{cases}
B_2 = A_1 - A_2 \\
2A_2 = A_1(1 + \frac{k_1}{k_2})
\end{cases}$$

$$\Leftrightarrow \begin{cases}
B_2 = A_1 - A_2 \\
A_2 = \frac{1}{2}A_1(1 + \frac{k_1}{k_2})
\end{cases}$$

$$\Leftrightarrow \begin{cases}
B_2 = -\frac{1}{2}A_1\left[1-2+\frac{k_1}{k_2}\right] = \frac{1}{2}A_1\left(1-\frac{k_1}{k_2}\right) \\
A_2 = \frac{1}{2}A_1\left(1+\frac{k_1}{k_2}\right)
\end{cases}$$

$$\begin{aligned}
A_3 e^{ik_1a} &= \frac{1}{2}A_1\left(1+\frac{k_1}{k_2}\right)e^{ik_2a} + \frac{1}{2}A_1\left(1-\frac{k_1}{k_2}\right)e^{-ik_2a} \\
A_3 &= \frac{1}{2}A_1\frac{\left[\left(1+\frac{k_1}{k_2}\right)e^{ik_2a} + \left(1-\frac{k_1}{k_2}\right)e^{-ik_2a}\right]}{e^{ik_1a}}
\end{aligned}$$

T=1 $\Rightarrow \left|\frac{A_3}{A_1}\right|^2 = 1$

$$\begin{aligned}
\frac{A_3}{A_1} &= \frac{1}{e^{ik_1a}}\left[\frac{e^{ik_2a}+e^{-ik_2a}}{2} + \frac{k_1}{k_2}\left(\frac{e^{ik_2a}-e^{-ik_2a}}{2}\right)\right] \\
&= \frac{1}{e^{ik_1a}}\left[\cos(k_2a) + \frac{k_1}{k_2}i\sin(k_2a)\right]
\end{aligned}$$

$$\begin{aligned}
\left|\frac{A_3}{A_1}\right|^2 &= \frac{\left|\cos(k_2a) + \frac{k_1}{k_2}i\sin(k_2a)\right|^2}{|e^{ik_1a}|^2} \\
&= \cos^2(k_2a) + \left(\frac{k_1}{k_2}\right)^2\sin^2(k_2a)
\end{aligned}$$

$$\begin{aligned}
\text{car }|e^{ik_1a}|^2 &= |\cos(k_1a) + i\sin(k_1a)|^2 \\
&= \cos^2(k_1a) + \sin^2(k_1a) = 1
\end{aligned}$$

$$\left(\frac{k_1}{k_2}\right)^2 = \frac{2mE/\hbar^2}{2m(E+V_0)/\hbar^2} = \frac{2mE}{2m(E+V_0)} = 1+ \frac{2mE}{2mV_0} = 1+ \frac{E}{V_0} \text{ si } V_0 \neq 0$$

$$\left(\frac{k_1}{k_2}\right)^2 = 1 \text{ si } V_0 = 0 \Rightarrow A_1 = A_2 = A_3$$

Il s'agit de la solution d'onde plane progressive

On sait que $1-\sin^2(k_2 a) = \cos^2(k_2 a)$

$$\Rightarrow \left|\frac{A_3}{A_1}\right|^2 = 1-\sin^2(k_2 a) + \left(\frac{k_1}{k_2}\right)^2\sin^2(k_2 a) = 1$$

$$\Rightarrow \left[\left(\frac{k_1}{k_2}\right)^2 - 1\right]\sin(k_2 a) = 0$$

$$\left(\frac{k_1}{k_2}\right)^2 - 1 = 0 \Rightarrow k_1^2 = k_2^2$$

$$\Rightarrow \frac{2mE}{\hbar^2} = \frac{2m(E+V_0)}{\hbar^2} \Rightarrow V_0 = 0$$

Sans potentiel, il n'y a rien à diffuser. L'onde incidente continue sans
jamais être perturbée. La section efficace est donc nulle partout.

$$\sin(k_2 a) = 0$$

$$\Rightarrow k_2 a = n\pi \text{ avec } n \in \mathbb{N}^*$$

$$\Rightarrow k_2 = \frac{n\pi}{a} = \sqrt{\frac{2m(E+V_0)}{\hbar^2}}$$
$$\Rightarrow 2m(E+V_0) = \left(\frac{n\pi\hbar}{a}\right)^2$$

$$\Rightarrow E_n = \frac{1}{2m}\left(\frac{n\pi\hbar}{a}\right)^2 - V_0$$

Ainsi, il s'agit de l'énergie pour laquelle l'électron peut traverser le
puits sans être réfléchi.

$$\psi(x) = \begin{cases}
\psi_I(x) = A_1e^{ik_1x} + B_1e^{-ik_1x} \\
\psi_{II}(x) = A_2e^{ik_2x} + B_2e^{-ik_2x} \\
\psi_{III}(x) = A_3e^{ik_1x}
\end{cases}$$

Si le puits commence pas en 0 mais en b\
alors $X = x-b$

$$\psi(x) = \begin{cases}
\psi_I(x) = A_1e^{ik_1(x-b)} + B_1e^{-ik_1(x-b)} \\
\psi_{II}(x) = A_2e^{ik_2(x-b)} + B_2e^{-ik_2(x-b)} \\
\psi_{III}(x) = A_3e^{ik_1(x-b)}
\end{cases}$$
