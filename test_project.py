import unittest
from unittest.mock import MagicMock
from model import Model
import tkinter as tk

class TestMo(unittest.TestCase):

	def setUp(self):
		self.model = Model()
		self.view = MagicMock()
		self.controller = MagicMock()
		self.view.outText = tk.Text()
		self.model.start(self.view, self.controller)

	#ARANGE TESTS

	def test_arange_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="0, 3, 1")
		self.model.name = "np_arange"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 0, 3, 1\nOutput: [0 1 2]\n")

	def test_arange_incorrect1(self):
		"""Test for incorrect input with only 1 of 3 operands."""
		self.view.input.get = MagicMock(return_value="1")
		self.model.name = "np_arange"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 1\nOutput: Incorrect input:\nnp_arange() missing 2 required positional arguments: 'stop' and 'step'\n")

	def test_arange_incorrect2(self):
		"""Test for incorrect input with only 2 of 3 operands."""
		self.view.input.get = MagicMock(return_value="1, 2")
		self.model.name = "np_arange"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 1, 2\nOutput: Incorrect input:\nnp_arange() missing 1 required positional argument: 'step'\n")

	def test_arange_incorrect3(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_arange"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_arange_incorrect4(self):
		"""Test for incorrect input with step=0."""
		self.view.input.get = MagicMock(return_value="0, 1, 0")
		self.model.name = "np_arange"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 0, 1, 0\nOutput: Incorrect input:\ndivision by zero\n")

	#RESHAPE TESTS

	def test_reshape_correct1(self):
		"""Test for correct input for reshaping 1D array."""
		self.view.input.get = MagicMock(return_value="(1, 2, 3, 4), (2, 2)")
		self.model.name = "np_reshape"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2, 3, 4), (2, 2)\nOutput: [[1 2]\n [3 4]]\n")

	def test_reshape_correct2(self):
		"""Test for correct input for reshaping 2D array."""
		self.view.input.get = MagicMock(return_value="((2, 2), (2, 2)), (1, 4)")
		self.model.name = "np_reshape"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((2, 2), (2, 2)), (1, 4)\nOutput: [[2 2 2 2]]\n")

	def test_reshape_incorrect1(self):
		"""Test for incorrect input with wrong result shape."""
		self.view.input.get = MagicMock(return_value="(1, 2, 3), (2, 2)")
		self.model.name = "np_reshape"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2, 3), (2, 2)\nOutput: Incorrect input:\ncannot reshape array of size 3 into shape (2,2)\n")

	def test_reshape_incorrect2(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_reshape"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_reshape_incorrect3(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 1)")
		self.model.name = "np_reshape"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 1)\nOutput: Incorrect input:\nnp_reshape() missing 1 required positional argument: 'newshape'\n")

	#ZEROS TESTS

	def test_zeros_correct1(self):
		"""Test for correct input for shaping 2D array."""
		self.view.input.get = MagicMock(return_value="(2, 2)")
		self.model.name = "np_zeros"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (2, 2)\nOutput: [[0. 0.]\n [0. 0.]]\n")

	def test_zeros_correct2(self):
		"""Test for correct input for shaping 1D array."""
		self.view.input.get = MagicMock(return_value="3")
		self.model.name = "np_zeros"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 3\nOutput: [0. 0. 0.]\n")

	def test_zeros_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_zeros"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_zeros_incorrect2(self):
		"""Test for incorrect input with negative shape dimension."""
		self.view.input.get = MagicMock(return_value="-1")
		self.model.name = "np_zeros"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: -1\nOutput: Incorrect input:\nnegative dimensions are not allowed\n")

	#ONES TESTS

	def test_ones_correct1(self):
		"""Test for correct input for shaping 2D array."""
		self.view.input.get = MagicMock(return_value="(2, 2)")
		self.model.name = "np_ones"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (2, 2)\nOutput: [[1. 1.]\n [1. 1.]]\n")

	def test_ones_correct2(self):
		"""Test for correct input for shaping 1D array."""
		self.view.input.get = MagicMock(return_value="3")
		self.model.name = "np_ones"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 3\nOutput: [1. 1. 1.]\n")

	def test_ones_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_ones"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_ones_incorrect2(self):
		"""Test for incorrect input with negative shape dimension."""
		self.view.input.get = MagicMock(return_value="-1")
		self.model.name = "np_ones"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: -1\nOutput: Incorrect input:\nnegative dimensions are not allowed\n")

	#MATRIX_MULTIPLICATION

	def test_matrix_multiplication_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="((1, 2), (3, 4)), ((5, 6), (7, 8))")
		self.model.name = "np_matrix_multiplication"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2), (3, 4)), ((5, 6), (7, 8))\nOutput: [[19 22]\n [43 50]]\n")

	def test_matrix_multiplication_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_matrix_multiplication"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_matrix_multiplication_incorrect2(self):
		"""Test for incorrect input with two different shaped arrays."""
		self.view.input.get = MagicMock(return_value="(1, 2), (1, 2, 3)")
		self.model.name = "np_matrix_multiplication"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (1, 2, 3)\nOutput: Incorrect input:\nmatmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 3 is different from 2)\n")

	def test_matrix_multiplication_incorrect3(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_matrix_multiplication"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_matrix_multiplication() missing 1 required positional argument: 'b'\n")

	#POWER TESTS

	def test_power_correct1(self):
		"""Test for correct input with 2 arrays."""
		self.view.input.get = MagicMock(return_value="(2, 3), (2, 5)")
		self.model.name = "np_power"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (2, 3), (2, 5)\nOutput: [  4 243]\n")

	def test_power_correct2(self):
		"""Test for correct input with array and number."""
		self.view.input.get = MagicMock(return_value="(2, 3), 2")
		self.model.name = "np_power"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (2, 3), 2\nOutput: [4 9]\n")

	def test_power_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_power"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_power_incorrect2(self):
		"""Test for incorrect input with only 1 od 2 operands."""
		self.view.input.get = MagicMock(return_value="(2, 3)")
		self.model.name = "np_power"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (2, 3)\nOutput: Incorrect input:\nnp_power() missing 1 required positional argument: 'b'\n")

	def test_power_incorrect3(self):
		"""Test for incorrect input with arrays of different shapes."""
		self.view.input.get = MagicMock(return_value="(2, 3, 1), (2, 3)")
		self.model.name = "np_power"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (2, 3, 1), (2, 3)\nOutput: Incorrect input:\noperands could not be broadcast together with shapes (3,) (2,) \n")

	#LINSPACE TESTS

	def test_linspace_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="1, 4, 25")
		self.model.name = "np_linspace"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 1, 4, 25\nOutput: [1.    1.125 1.25  1.375 1.5   1.625 1.75  1.875 2.    2.125 2.25  2.375\n 2.5   2.625 2.75  2.875 3.    3.125 3.25  3.375 3.5   3.625 3.75  3.875\n 4.   ]\n")

	def test_linspace_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_linspace"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_linspace_incorrect2(self):
		"""Test for incorrect input with only 1 of 3 operands."""
		self.view.input.get = MagicMock(return_value="1")
		self.model.name = "np_linspace"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 1\nOutput: Incorrect input:\nnp_linspace() missing 2 required positional arguments: 'stop' and 'num'\n")

	def test_linspace_incorrect3(self):
		"""Test for incorrect input with only 2 of 3 operands."""
		self.view.input.get = MagicMock(return_value="1, 4")
		self.model.name = "np_linspace"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 1, 4\nOutput: Incorrect input:\nnp_linspace() missing 1 required positional argument: 'num'\n")

	def test_linspace_incorrect4(self):
		"""Test for incorrect input with negative number of samples."""
		self.view.input.get = MagicMock(return_value="1, 4, -2")
		self.model.name = "np_linspace"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 1, 4, -2\nOutput: Incorrect input:\nNumber of samples, -2, must be non-negative.\n")

	#EXP TESTS

	def test_exp_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 2, 3, 4)")
		self.model.name = "np_exp"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2, 3, 4)\nOutput: [ 2.71828183  7.3890561  20.08553692 54.59815003]\n")

	def test_exp_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_exp"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#SQRT TESTS

	def test_sqrt_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 4, 9, 16)")
		self.model.name = "np_sqrt"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 4, 9, 16)\nOutput: [1. 2. 3. 4.]\n")

	def test_sqrt_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_sqrt"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#TRANSPOSE TESTS

	def test_transpose_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="((1, 2), (3, 4))")
		self.model.name = "np_transpose"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2), (3, 4))\nOutput: [[1 3]\n [2 4]]\n")

	def test_transpose_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_transpose"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#VSTACK TESTS

	def test_vstack_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 2), (3, 4)")
		self.model.name = "np_vstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (3, 4)\nOutput: [[1 2]\n [3 4]]\n")

	def test_vstack_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_vstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_vstack_incorrect2(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_vstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_vstack() missing 1 required positional argument: 'b'\n")

	def test_vstack_incorrect3(self):
		"""Test for incorrect input with arrays of different shapes."""
		self.view.input.get = MagicMock(return_value="(1, 2), (3, 4, 5)")
		self.model.name = "np_vstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (3, 4, 5)\nOutput: Incorrect input:\nall the input array dimensions for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 2 and the array at index 1 has size 3\n")

	#HSTACK TESTS

	def test_hstack_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 2), (3, 4)")
		self.model.name = "np_hstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (3, 4)\nOutput: [1 2 3 4]\n")

	def test_hstack_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_hstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_hstack_incorrect2(self):
		"""Test for incorrect input with arrays of different shapes."""
		self.view.input.get = MagicMock(return_value="(1, 2), ((1, 2), (1, 2))")
		self.model.name = "np_hstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), ((1, 2), (1, 2))\nOutput: Incorrect input:\nall the input arrays must have same number of dimensions, but the array at index 0 has 1 dimension(s) and the array at index 1 has 2 dimension(s)\n")

	def test_hstack_incorrect3(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_hstack"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_hstack() missing 1 required positional argument: 'b'\n")

	#SORT TESTS

	def test_sort_correct1(self):
		"""Test for correct input for 1D array."""
		self.view.input.get = MagicMock(return_value="(41, 3, 23, 1)")
		self.model.name = "np_sort"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (41, 3, 23, 1)\nOutput: [ 1  3 23 41]\n")

	def test_sort_correct2(self):
		"""Test for correct input for 2D array."""
		self.view.input.get = MagicMock(return_value="((41, 3), (23, 1))")
		self.model.name = "np_sort"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((41, 3), (23, 1))\nOutput: [[ 3 41]\n [ 1 23]]\n")

	def test_sort_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_sort"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#SUM TESTS

	def test_sum_correct1(self):
		"""Test for correct input for 2D array."""
		self.view.input.get = MagicMock(return_value="((1, 3), (4, 7))")
		self.model.name = "np_sum"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 3), (4, 7))\nOutput: 15\n")

	def test_sum_correct2(self):
		"""Test for correct input for 1D array."""
		self.view.input.get = MagicMock(return_value="(1, 3, 4, 7)")
		self.model.name = "np_sum"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 3, 4, 7)\nOutput: 15\n")

	def test_sum_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_sum"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#UNIQUE TESTS

	def test_unique_correct1(self):
		"""Test for correct input for 1D array."""
		self.view.input.get = MagicMock(return_value="(1, 3, 4, 1, 4, 3, 5)")
		self.model.name = "np_unique"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 3, 4, 1, 4, 3, 5)\nOutput: [1 3 4 5]\n")

	def test_unique_correct2(self):
		"""Test for correct input for 2D array."""
		self.view.input.get = MagicMock(return_value="((1, 3, 4), (1, 4, 3))")
		self.model.name = "np_unique"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 3, 4), (1, 4, 3))\nOutput: [1 3 4]\n")

	def test_unique_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_unique"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#FLIP TESTS

	def test_flip_correct1(self):
		"""Test for correct input for 1D array."""
		self.view.input.get = MagicMock(return_value="(5, 6, 3, 2)")
		self.model.name = "np_flip"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (5, 6, 3, 2)\nOutput: [2 3 6 5]\n")

	def test_flip_correct2(self):
		"""Test for correct input for 2D array."""
		self.view.input.get = MagicMock(return_value="((5, 6), (3, 2))")
		self.model.name = "np_flip"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((5, 6), (3, 2))\nOutput: [[2 3]\n [6 5]]\n")

	def test_flip_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_flip"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#FLATTEN TESTS

	def test_flatten_correct1(self):
		"""Test for correct input for 2D array."""
		self.view.input.get = MagicMock(return_value="((3, 5), (6, 8))")
		self.model.name = "np_flatten"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((3, 5), (6, 8))\nOutput: [3 5 6 8]\n")

	def test_flatten_correct2(self):
		"""Test for correct input for 1D array."""
		self.view.input.get = MagicMock(return_value="(3, 5, 6, 8)")
		self.model.name = "np_flatten"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (3, 5, 6, 8)\nOutput: [3 5 6 8]\n")

	def test_flatten_incorrect(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_flatten"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	#PLUS TESTS

	def test_plus_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 2), (3, 4)")
		self.model.name = "np_plus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (3, 4)\nOutput: [4 6]\n")

	def test_plus_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_plus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_plus_incorrect2(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_plus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_plus() missing 1 required positional argument: 'b'\n")

	def test_plus_incorrect3(self):
		"""Test for incorrect input with arrays of different shapes."""
		self.view.input.get = MagicMock(return_value="(1, 2), (1, 2, 3)")
		self.model.name = "np_plus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (1, 2, 3)\nOutput: Incorrect input:\noperands could not be broadcast together with shapes (2,) (3,) \n")

	#MINUS TESTS

	def test_minus_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 2), (3, 4)")
		self.model.name = "np_minus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (3, 4)\nOutput: [-2 -2]\n")

	def test_minus_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_minus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_minus_incorrect2(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_minus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_minus() missing 1 required positional argument: 'b'\n")

	def test_minus_incorrect3(self):
		"""Test for incorrect input with arrays of different shapes."""
		self.view.input.get = MagicMock(return_value="(1, 2), (1, 2, 3)")
		self.model.name = "np_minus"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (1, 2, 3)\nOutput: Incorrect input:\noperands could not be broadcast together with shapes (2,) (3,) \n")

	#MULTIPLICATION TESTS

	def test_mul_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 2), (3, 4)")
		self.model.name = "np_mul"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (3, 4)\nOutput: [3 8]\n")

	def test_mul_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_mul"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_mul_incorrect2(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_mul"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_mul() missing 1 required positional argument: 'b'\n")

	def test_mul_incorrect3(self):
		"""Test for incorrect input with arrays of different shapes."""
		self.view.input.get = MagicMock(return_value="(1, 2), (1, 2, 3)")
		self.model.name = "np_mul"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (1, 2, 3)\nOutput: Incorrect input:\noperands could not be broadcast together with shapes (2,) (3,) \n")

	#DIVISION TESTS

	def test_div_correct(self):
		"""Test for correct input."""
		self.view.input.get = MagicMock(return_value="(1, 2), (3, 4)")
		self.model.name = "np_div"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (3, 4)\nOutput: [0.33333333 0.5       ]\n")

	def test_div_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_div"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_div_incorrect2(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_div"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_div() missing 1 required positional argument: 'b'\n")

	def test_div_incorrect3(self):
		"""Test for incorrect input with arrays of different shapes."""
		self.view.input.get = MagicMock(return_value="(1, 2), (1, 2, 3)")
		self.model.name = "np_div"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (1, 2, 3)\nOutput: Incorrect input:\noperands could not be broadcast together with shapes (2,) (3,) \n")

	#VSPLIT TESTS

	def test_vsplit_correct1(self):
		"""Test for correct input with equally splitting."""
		self.view.input.get = MagicMock(return_value="((1, 2), (3, 4)), 2")
		self.model.name = "np_vsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2), (3, 4)), 2\nOutput: [array([[1, 2]]), array([[3, 4]])]\n")

	def test_vsplit_correct2(self):
		"""Test for correct input with splitting by input rows."""
		self.view.input.get = MagicMock(return_value="((1, 2, 3), (4, 5, 6), (7, 8, 9)), (1, 2)")
		self.model.name = "np_vsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2, 3), (4, 5, 6), (7, 8, 9)), (1, 2)\nOutput: [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]\n")

	def test_vsplit_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_vsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_vsplit_incorrect2(self):
		"""Test for incorrect input with no possible equal splitting."""
		self.view.input.get = MagicMock(return_value="((1, 2, 3), (4, 5, 6), (7, 8, 9)), 2")
		self.model.name = "np_vsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 2\nOutput: Incorrect input:\narray split does not result in an equal division\n")

	def test_vsplit_incorrect3(self):
		"""Test for incorrect input with splitting by 0."""
		self.view.input.get = MagicMock(return_value="((1, 2, 3), (4, 5, 6), (7, 8, 9)), 0")
		self.model.name = "np_vsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 0\nOutput: Incorrect input:\ninteger division or modulo by zero\n")

	def test_vsplit_incorrect4(self):
		"""Test for incorrect input with splitting a 1D array."""
		self.view.input.get = MagicMock(return_value="(1, 2), (1, 2)")
		self.model.name = "np_vsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2), (1, 2)\nOutput: Incorrect input:\nvsplit only works on arrays of 2 or more dimensions\n")

	def test_vsplit_incorrect5(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_vsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_vsplit() missing 1 required positional argument: 'shape'\n")

	#HSPLIT TESTS

	def test_hsplit_correct1(self):
		"""Test for correct input with equally splitting."""
		self.view.input.get = MagicMock(return_value="((1, 2), (3, 4)), 2")
		self.model.name = "np_hsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2), (3, 4)), 2\nOutput: [array([[1],\n       [3]]), array([[2],\n       [4]])]\n")

	def test_hsplit_correct2(self):
		"""Test for correct input with splitting by input columns."""
		self.view.input.get = MagicMock(return_value="((1, 2, 3), (4, 5, 6), (7, 8, 9)), (1, 2)")
		self.model.name = "np_hsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2, 3), (4, 5, 6), (7, 8, 9)), (1, 2)\nOutput: [array([[1],\n       [4],\n       [7]]), array([[2],\n       [5],\n       [8]]), array([[3],\n       [6],\n       [9]])]\n")
		
	def test_hsplit_incorrect1(self):
		"""Test for incorrect input."""
		self.view.input.get = MagicMock(return_value="abc")
		self.model.name = "np_hsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: abc\nOutput: Incorrect input:\nname 'abc' is not defined\n")

	def test_hsplit_incorrect2(self):
		"""Test for incorrect input with no possible equal splitting."""
		self.view.input.get = MagicMock(return_value="((1, 2, 3), (4, 5, 6), (7, 8, 9)), 2")
		self.model.name = "np_hsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 2\nOutput: Incorrect input:\narray split does not result in an equal division\n")

	def test_hsplit_incorrect3(self):
		"""Test for incorrect input with splitting by 0."""
		self.view.input.get = MagicMock(return_value="((1, 2, 3), (4, 5, 6), (7, 8, 9)), 0")
		self.model.name = "np_hsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: ((1, 2, 3), (4, 5, 6), (7, 8, 9)), 0\nOutput: Incorrect input:\ninteger division or modulo by zero\n")

	def test_hsplit_incorrect4(self):
		"""Test for incorrect input with splitting a number."""
		self.view.input.get = MagicMock(return_value="1, (1, 2)")
		self.model.name = "np_hsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: 1, (1, 2)\nOutput: Incorrect input:\nhsplit only works on arrays of 1 or more dimensions\n")

	def test_hsplit_incorrect5(self):
		"""Test for incorrect input with only 1 of 2 operands."""
		self.view.input.get = MagicMock(return_value="(1, 2)")
		self.model.name = "np_hsplit"
		self.model.ex_call()
		self.assertEqual(self.view.outText.get(1.0, tk.END), "Input: (1, 2)\nOutput: Incorrect input:\nnp_hsplit() missing 1 required positional argument: 'shape'\n")


