import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from bubble_sort import Sorter


class BubbleSortTest(unittest.TestCase):

    def setUp(self):
        self.sorter = Sorter()  # Inicializar el SUT

    def test_cp1_lista_de_un_elemento(self):
        # Arrange
        vet = [5]
        # Act
        resultado = self.sorter.bubble_sort(vet)
        # Assert
        self.assertEqual([5], resultado)

    def test_cp2_lista_ya_ordenada(self):
        vet = [1, 2]
        resultado = self.sorter.bubble_sort(vet)
        self.assertEqual([1, 2], resultado)

    def test_cp3_lista_con_un_intercambio(self):
        vet = [2, 1]
        resultado = self.sorter.bubble_sort(vet)
        self.assertEqual([1, 2], resultado)

    def test_cp4_lista_con_varias_iteraciones(self):
        vet = [3, 1, 2]
        resultado = self.sorter.bubble_sort(vet)
        self.assertEqual([1, 2, 3], resultado)


if __name__ == "__main__":
    unittest.main()
