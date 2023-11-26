# Pas besoin d'importer pytest pour ces tests simples
# import pytest - Pas nécessaire si vous n'utilisez pas les fonctionnalités spécifiques de pytest

def test_calc_addition():
    # Test de la fonction pour le résultat de 2 + 4
    output = 2 + 4
    assert output == 6


def test_calc_substraction():
    # Test de la fonction pour le résultat de 2 - 4
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    # Test de la fonction pour le résultat de 2 * 4
    output = 2 * 4
    assert output == 8


def test_coucou():
    # Test de la fonction pour vérifier si le résultat est 'hello'
    output = 'hello'
    assert output == 'hello'
