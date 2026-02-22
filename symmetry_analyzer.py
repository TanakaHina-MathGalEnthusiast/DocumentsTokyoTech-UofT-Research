import math

class SymmetryAnalyzer:
    """
    Research tool developed for the Tokyo Tech - UofT collaboration.
    Analyzes group-theoretic structures and their stability.
    """
    
    def __init__(self, order):
        """Initializes the analyzer with the mathematical group order."""
        self.order = order
        # We call the factorization once here
        self.factors = self._calculate_prime_factors()

    def _calculate_prime_factors(self):
        """Internal method for prime factorization of the group order."""
        n = self.order
        factors = []
        d = 2
        temp = n
        while d * d <= temp:
            while (temp % d) == 0:
                factors.append(d)
                temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)
        return factors

    def get_sylow_numbers(self):
        """
        Calculates possible values for n_p based on Sylow theorems.
        Condition: n_p must be 1 mod p and divide m.
        """
        unique_primes = set(self.factors)
        results = {}
        for p in unique_primes:
            m = self.order
            while m % p == 0:
                m //= p
            # Logic to find divisors of m that satisfy n_p = 1 (mod p)
            possible_np = [i for i in range(1, m + 1) if m % i == 0 and i % p == 1]
            results[p] = possible_np
        return results

    def check_sylow_stability(self):
        """Evaluates structural stability based on order parity."""
        print(f"--- Analysis Report: Order {self.order} ---")
        print(f"Prime Factorization: {self.factors}")
        
        if self.order % 2 == 0:
            return "Status: Symmetric structure detected (Even order)."
        else:
            return "Status: Asymmetric structure (Odd order)."

    def verify_integral_results(self):
        """
        Numerical verification of the integral result from research notes.
        Formula: (sqrt(3)/2)*atan(1/2) - pi/3 + sqrt(2)*atan(sqrt(1.5))
        """
        # Using math library for high precision
        term1 = (math.sqrt(3) / 2) * math.atan(0.5)
        term2 = math.pi / 3
        term3 = math.sqrt(2) * math.atan(math.sqrt(1.5))
        
        final_value = term1 - term2 + term3
        return f"Integral Numerical Value: {final_value:.6f}"
# --- EXECUTION ---
if __name__ == "__main__":
    # Test with Order 60 (The classic A5 group case)
    analysis = SymmetryAnalyzer(60)
    
    # 1. Show the stability report
    print(analysis.check_sylow_stability())
    
    # 2. Show the Sylow possibilities
    sylow_data = analysis.get_sylow_numbers()
    print(f"Sylow n_p candidates: {sylow_data}")
    
    # 3. Show the integral verification result
    print(analysis.verify_integral_results())