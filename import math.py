import math
import numpy as np

def identify_student():
    profile = {
        "Name": "Tanaka Hina",
        "Status": "3rd Year Math Student",
        "Origin": "Tokyo Institute of Technology (Tokyo Tech)",
        "Current": "University of Toronto (UofT) - Visiting Student",
        "Interests": ["Group Theory", "Quantitative Finance", "Fisher-Rao Geometry"]
    }
    
    print("--- Student Identity Card ---")
    for key, value in profile.items():
        print(f"{key}: {value}")
    print("------------------------------\n")

def sylow_calculator(n):
    """Calcule les ordres possibles des p-sous-groupes de Sylow pour un groupe d'ordre n."""
    print(f"Analyse des sous-groupes de Sylow pour un groupe d'ordre {n}:")
    temp_n = n
    d = 2
    while d * d <= temp_n:
        if temp_n % d == 0:
            count = 0
            while temp_n % d == 0:
                count += 1
                temp_n //= d
            print(f" - Pour p={d}, l'ordre du p-sous-groupe de Sylow est {d}^{count} = {d**count}")
        d += 1
    if temp_n > 1:
        print(f" - Pour p={temp_n}, l'ordre du p-sous-groupe de Sylow est {temp_n}^1 = {temp_n}")

if __name__ == "__main__":
    identify_student()
    # Exemple avec l'ordre 60 (Groupe alterné A5, très commun en L3)
    sylow_calculator(60)
    
    print("\n[Message] Script prêt pour l'exportation vers GitHub.")