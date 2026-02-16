import sympy as sp

def verify_complex_integral():
    """
    Verifies the integral of cos(x)*arctan(cos(x)) from 0 to pi/3.
    This script demonstrates the transition from analytical derivation to 
    computational verification, a key skill for quantitative research.
    """
    x = sp.Symbol('x')
    f = sp.cos(x) * sp.atan(sp.cos(x))
    
    print("--- Analytical Integration Tool ---")
    print(f"Integrating: {f}")
    
    # Performing the definite integration
    result = sp.integrate(f, (x, 0, sp.pi/3))
    
    print("\nExact Symbolic Result:")
    sp.pprint(result)
    
    print(f"\nNumerical Value: {result.evalf():.8f}")

if __name__ == "__main__":
    verify_complex_integral()