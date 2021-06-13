import numpy as np

global hints

hints = {'np_arange': "Enter 'start, stop, step'\nstart: Start of interval\nstop: End of interval\nstep: Spacing between values\nExample: 2, 3, 4",
		 'np_reshape': "Enter 'array, newshape'\narray: Array to be reshaped\n newshape: The new shape (should be compatible with the original shape)\nExample: (1, 2, 3, 4), (2, 2)",
		 'np_zeros': "Enter 'shape'\nshape: Shape of new array\nExample: 2 or (2, 3)",
		 'np_ones': "Enter 'shape'\nshape: Shape of new array\nExample: 2 or (2, 3)",
		 'np_matrix_multiplication': "Enter 'array1, array2'\narray1: First argument\narray2: Second argument\nExample: ((1, 2), (3, 4)), ((5, 6), (7, 8))",
		 'np_power': "Enter 'array1, array2'\narray1: The bases array\narray2: The exponents array\nExample: (2, 3), (2, 5)",
		 'np_linspace': "Enter 'start, stop, num'\nstart: The starting value of the sequence\nstop: The end value of the sequence\nnum: Number of samples to generate\nExample: 1, 4, 25",
		 'np_exp': "Enter 'array'\narray: Input values\nExamples: (1, 2, 3, 4)",
		 'np_sqrt': "Enter 'array'\narray: The values whose square-roots are required\nExample: (1, 4, 9, 16)",
		 'np_transpose': "Enter 'array'\narray: Input array to be transposed\nExample: ((1, 2), (3, 4))",
		 'np_vstack': "Enter 'array1, array2'\narray1,2: Arrays to be stacked\n Example: (1, 2), (3, 4)",
		 'np_hstack': "Enter 'array1, array2'\narray1,2: Arrays to be stacked\n Example: (1, 2), (3, 4)",
		 'np_sort': "Enter 'array'\narray: Array to be sorted\nExample: ((41, 3), (23, 1))",
		 'np_sum': "Enter 'array'\narray: Elements to sum\nExample: ((1, 3), (4, 7))",
		 'np_unique': "Enter 'array'\narray: Input array\nExample:(1, 3, 4, 1, 4, 3, 5)",
		 'np_flip': "Enter 'array'\narray: Input array to be reversed\nExample: (5, 6, 3, 2)",
		 'np_flatten': "Enter 'array'\narray: Input array to be collapsed into 1D\nExample: ((3, 5), (6, 8))",
		 'np_plus': "Enter 'array1, array2'\narray1: First array\narray2: Second array\nExample: (1, 2), (3, 4)",
		 'np_minus': "Enter 'array1, array2'\narray1: First array\narray2: Second array\nExample: (1, 2), (3, 4)",
		 'np_mul': "Enter 'array1, array2'\narray1: First array\narray2: Second array\nExample: (1, 2), (3, 4)",
		 'np_div': "Enter 'array1, array2'\narray1: First array\narray2: Second array\nExample: (1, 2), (3, 4)",
		 'np_vsplit': "Enter 'array, shape'\narray: Input array\nshape: if shape is 1 number - split into shape equal sized arrays\nshape: if shape is a tuple - split array by this column numbers\nExample: ((1, 2), (3, 4)), 2 or ((1, 2, 3), (4, 5, 6), (7, 8, 9)), (1, 2)",
		 'np_hsplit': "Enter 'array, shape'\narray: Input array\nshape: if shape is 1 number - split into shape equal sized arrays\nshape: if shape is a tuple - split array by this row numbers\nExample: ((1, 2), (3, 4)), 2 or ((1, 2, 3), (4, 5, 6), (7, 8, 9)), (1, 2)"}

def np_arange(start, stop, step):
	"""Return evenly spaced values within a given interval."""
	return np.arange(start, stop, step)

def np_reshape(a, newshape):
	"""Gives a new shape to an array without changing its data."""
	return np.array(a).reshape(newshape)

def np_zeros(shape):
	"""Return a new array of given shape and type, filled with zeros."""
	return np.zeros(shape)

def np_ones(shape):
	"""Return a new array of given shape and type, filled with ones."""
	return np.ones(shape)

def np_matrix_multiplication(a, b):
	"""Matrix multiplication product of two arrays."""
	return np.array(a) @ np.array(b)

def np_power(a, b):
	"""First array elements raised to powers from second array, element-wise."""
	return np.power(np.array(a), np.array(b))

def np_linspace(start, stop, num):
	"""Returns num evenly spaced samples, calculated over the interval [start, stop]."""
	return np.linspace(start, stop, num)

def np_exp(a):
	"""Calculate the exponential of all elements in the input array."""
	return np.exp(a)

def np_sqrt(a):
	"""Return the non-negative square-root of an array, element-wise."""
	return np.sqrt(a)

def np_transpose(a):
	"""Reverse or permute the axes of an array; returns the modified array."""
	return np.array(a).T

def np_vstack(a, b):
	"""Stack arrays in sequence vertically (row wise)."""
	return np.vstack((np.array(a), np.array(b)))

def np_hstack(a, b):
	"""Stack arrays in sequence horizontally (column wise)."""
	return np.hstack((np.array(a), np.array(b)))

def np_sort(a):
	"""Return a sorted copy of an array."""
	return np.sort(np.array(a))

def np_sum(a):
	"""Sum of array elements."""
	return np.array(a).sum()

def np_unique(a):
	"""Find the unique elements of an array."""
	return np.unique(np.array(a))

def np_flip(a):
	"""Reverse the order of elements in an array."""
	return np.flip(np.array(a))

def np_flatten(a):
	"""Return a copy of the array collapsed into one dimension."""
	return np.array(a).flatten()

def np_plus(a, b):
	"""Return the sum product of two given arrays."""
	return np.array(a) + np.array(b)

def np_minus(a, b):
	"""Return the difference product of two given arrays."""
	return np.array(a) - np.array(b)

def np_mul(a, b):
	"""Return the multiplication product of two given arrays."""
	return np.array(a) * np.array(b)

def np_div(a, b):
	"""Return the division product of two given arrays."""
	return np.array(a) / np.array(b)

def np_vsplit(a, shape):
	"""Split an array into multiple sub-arrays vertically (row-wise)."""
	return np.vsplit(np.array(a), shape)

def np_hsplit(a, shape):
	"""Split an array into multiple sub-arrays horizontally (column-wise)."""
	return np.hsplit(np.array(a), shape)

