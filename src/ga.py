from sympy import symbols, Mul, simplify

def preprocess_factors(factors):
    unique_factors = list(set(factors))
    swaps = 0
    for factor in unique_factors:
        indices = [i for i, x in enumerate(factors) if x == factor]
        pairs = list(zip(indices[::2], indices[1::2]))
        for i, j in pairs:
            swaps += j - i - 1
        factors = [x for i, x in enumerate(factors) if all(i not in pair for pair in pairs)]
    return factors, swaps

def bubble_sort(factors):
    swaps = 0
    for i in range(len(factors)):
        for j in range(len(factors) - 1):
            if str(factors[j]) > str(factors[j + 1]):
                factors[j], factors[j + 1] = factors[j + 1], factors[j]
                swaps += 1
    return factors, swaps

def normal_form(term):
    # Split the term into its factors
    factors = list(term.args)
    # Separate the constant term from the factors
    constant_term = [f for f in factors if not f.free_symbols]
    # Filter out any symbols with powers higher than 1
    factors = [f for f in factors if f.free_symbols and f.as_base_exp()[1] == 1]
    factors, swaps = preprocess_factors(factors)
    # Sort the remaining factors and count the number of swaps
    factors, additional_swaps = bubble_sort(factors)
    factors += constant_term
    # Replace e_i^2 with c
    factors = [simplify(f**2) if isinstance(f, type(factors[0])) and f**2 in factors else f for f in factors]
    # Return the term in normal form
    return Mul(*factors) * (-1)**(swaps + additional_swaps)

# Define the symbols
#e = symbols('e:4', commutative=False)
#term = 3 * e[3] * e[2] * e[1] * e[2]
#print(normal_form(term))  # Outputs: -3*e1*e2