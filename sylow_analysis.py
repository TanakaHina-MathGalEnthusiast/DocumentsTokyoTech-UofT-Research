import math

def display_student_identity():
    """Displays the academic profile of the researcher."""
    identity = {
        "Full Name": "Tanaka Hina",
        "Academic Level": "Junior (3rd Year) Mathematics Student",
        "Home Institution": "Tokyo Institute of Technology (Tokyo Tech)",
        "Host Institution": "University of Toronto (UofT)",
        "Research Focus": ["Group Theory", "Quantitative Finance", "Information Geometry"]
    }
    
    print("--- ACADEMIC IDENTITY CARD ---")
    for key, value in identity.items():
        print(f"{key}: {value}")
    print("-" * 30 + "\n")

def get_sylow_orders(group_order):
    """
    Computes the orders of p-Sylow subgroups for a given group order.
    Essential for 3rd-year Abstract Algebra.
    """
    print(f"Analyzing Sylow subgroups for a group of order: {group_order}")
    n = group_order
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                exponent += 1
                n //= p
            print(f"  > p={p}: The p-Sylow subgroup has order {p}^{exponent} = {p**exponent}")
        p += 1
    if n > 1:
        print(f"  > p={n}: The p-Sylow subgroup has order {n}^1 = {n}")

if __name__ == "__main__":
    display_student_identity()
    
    # Testing with order 60 (The order of the alternating group A5)
    get_sylow_orders(60)
    
    print("\n[Status] Code execution successful. Ready for GitHub export.")