# Symmetry Analysis & Integral Verification Tool
*Tokyo Tech - University of Toronto Research Collaboration*

This repository contains a specialized Python tool developed to bridge algebraic group theory and numerical analysis. It was designed to support structural research involving order-60 groups (notably the $A_5$ group case) and high-precision verification of research-based integrals.

## Core Features
* **Algebraic Analysis**: Automates prime factorization and calculates Sylow $n_p$ candidates for a given mathematical group order.
* **Symmetry Detection**: Evaluates structural stability based on order parity (Symmetric vs. Asymmetric detection).
* **Numerical Verification**: Includes a dedicated high-precision verification module for complex integral results, utilizing the `math` library for 6-decimal precision.

## Current Results (Order 60 Case)
* **Sylow Candidates**: $n_2 \in \{1, 3, 5, 15\}$, $n_3 \in \{1, 4, 10\}$, $n_5 \in \{1, 6\}$.
* **Integral Verification**: Successfully computed value: **0.607435**.
