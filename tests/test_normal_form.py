
import pytest
from sympy import symbols
from ..src.ga import *

@pytest.fixture
def e():
    return symbols('e:3', commutative=False)

def test_normal_form_case_1(e):
    term = 3 * e[2] * e[1]
    assert normal_form(term) == -3 * e[1] * e[2]

def test_normal_form_case_2(e):
    term = 3 * e[1] * e[2]
    assert normal_form(term) == 3 * e[1] * e[2]

def test_normal_form_case_3(e):
    term = 3 * e[2] * e[2]
    assert normal_form(term) == 3  # assuming c = 1

def test_normal_form_case_4(e):
    term = 3 * e[2] * e[1] * e[2]
    assert normal_form(term) == -3 * e[1]  # assuming c = 1

def test_normal_form_case_5(e):
    term = 3 * e[2] * e[1] * e[0]
    assert normal_form(term) == -3 * e[0] * e[1] * e[2]

def test_normal_form_case_6(e):
    # term = 2 * e[2] * e[1] * e[0] * e[2]
    # After normal form: -2 * e[0] * e[1] * e[2] * e[2] = -2 * e[0] * e[1] * 1 = -2 * e[0] * e[1]
    term = 2 * e[2] * e[1] * e[0] * e[2]
    assert normal_form(term) == -2 * e[0] * e[1]

def test_normal_form_case_7(e):
    # term = 5 * e[0] * e[1] * e[2] * e[0] * e[1]
    # After normal form: -5 * e[0] * e[0] * e[1] * e[1] * e[2] = -5 * 1 * 1 * e[2] = -5 * e[2]
    term = 5 * e[0] * e[1] * e[2] * e[0] * e[1]
    assert normal_form(term) == -5 * e[2]

@pytest.fixture
def e_long():
    return symbols('e:10', commutative=False)

def test_normal_form_case_8(e_long):
    # term = 7 * e_long[9] * e_long[8] * e_long[7] * e_long[6] * e_long[5]
    # After normal form: -7 * e_long[5] * e_long[6] * e_long[7] * e_long[8] * e_long[9]
    term = 7 * e_long[9] * e_long[8] * e_long[7] * e_long[6] * e_long[5]
    assert normal_form(term) == 7 * e_long[5] * e_long[6] * e_long[7] * e_long[8] * e_long[9]

def test_normal_form_case_9(e_long):
    # term = 6 * e_long[4] * e_long[3] * e_long[2] * e_long[1] * e_long[0]
    # After normal form: 6 * e_long[0] * e_long[1] * e_long[2] * e_long[3] * e_long[4]
    term = 6 * e_long[4] * e_long[3] * e_long[2] * e_long[3] * e_long[0]
    assert normal_form(term) == 6 * e_long[0] * e_long[2] * e_long[4]
