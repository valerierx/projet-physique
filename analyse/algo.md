---
author:
- Yanis KASSOU, Gweltaz COLLIN et Valérie ROUX
date: Juin 2025
title: |
  **CY Tech\
  Projet numérique**
---

On cherche une solution particulière de:

$$\psi(x,t) = \phi(x)e^{-\frac{iEt}{\hbar}}$$

En injectant dans l'équation de Schrödinger:

$$i\hbar\left(-\frac{iE}{\hbar}\right)\phi(x)e^{-\frac{iEt}{\hbar}} = H\phi(x)e^{-\frac{iEt}{\hbar}}$$

$$\Rightarrow E\phi(x) = H\phi(x)$$
$$\Rightarrow E\phi(x) = -\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2} + V(x)\phi(x)$$

$\phi(x)$ est vecteur propre donc un état propre de l'énergie, et $E$
est valeur propre (l'énergie associée).

H opérateur ou matrice

On pose le développement de Taylor autour de $x_i$:
$$\phi(x_i+dx) = \phi(x_i) + dx\,\phi'(x_i) + \frac{dx^2}{2}\phi''(x_i)$$
$$\phi(x_i-dx) = \phi(x_i) - dx\,\phi'(x_i) + \frac{dx^2}{2}\phi''(x_i)$$

Somme des deux:
$$\phi(x_i+dx) + \phi(x_i-dx) = 2\phi(x_i) + dx^2\phi''(x_i)$$

$$\phi''(x_i) = \frac{\phi(x_i+dx)-2\phi(x_i)+\phi(x_i-dx)}{dx^2}$$

On approxime $\frac{d^2\phi}{dx^2}$ par
$\frac{\phi_{i+1}-2\phi_i+\phi_{i-1}}{dx^2}$
$$H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$$

On obtient:

$$E\phi(x) = -\frac{\hbar}{2m}\cdot\frac{\phi(x_i+dx)-2\phi(x_i)+\phi(x_i-dx)}{dx^2}+V(x)\phi(x)$$

$$\Rightarrow -E\phi(x_i) = -\frac{\hbar^2}{2mdx^2}\phi(x_{i+1})+(\frac{\hbar^2}{mdx^2}+V_i)\phi(x_i)-\frac{\hbar^2}{2mdx^2}\phi(x_{i-1})$$

Matrice diagonale principale $$H_{ii} = \frac{\hbar^2}{mdx^2}+V(x_i)$$

Matrice diagonale inférieure et supérieure
$$H_{i,i\pm1} = -\frac{\hbar^2}{2mdx^2}$$

[Remarque]{.underline}: dans le code Python, on a mis $\hbar$ et m égal
à 1 pour simplifier.
