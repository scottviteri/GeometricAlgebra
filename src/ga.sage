# this needs to be executed with a working ./sage executable

from sage.algebras.clifford_algebra import CliffordAlgebra
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.rational_field import QQ

def Q():
    QF = QuadraticForm(QQ, 3, [1, 0, 0, 1, 0, 1])
    Cl = CliffordAlgebra(QF)
    Cl.inject_variables()
    return Cl

# Test case 1
Q_instance = Q()
e1, e2, e3 = Q_instance.gens()
term = 3 * e2 * e1
assert term == -3 * e1 * e2

# Test case 2
Q_instance = Q()
e1, e2, e3 = Q_instance.gens()
term = 3 * e1 * e2
assert term == 3 * e1 * e2

# Test case 3
Q_instance = Q()
e1, e2, e3 = Q_instance.gens()
term = 3 * e2 * e2
assert term == 3

# Test case 4
Q_instance = Q()
e1, e2, e3 = Q_instance.gens()
term = 3 * e2 * e1 * e2
assert term == -3 * e1

# Test case 5
Q_instance = Q()
e1, e2, e3 = Q_instance.gens()
term = 3 * e2 * e1 * e3
assert term == -3 * e3 * e1 * e2

# Test case 6
Q_instance = Q()
e1, e2, e3 = Q_instance.gens()
term = 2 * e2 * e1 * e3 * e2
assert term == -2 * e3 * e1

# Test case 7
Q_instance = Q()
e1, e2, e3 = Q_instance.gens()
term = 5 * e1 * e2 * e3 * e1 * e2
assert term == -5 * e3

