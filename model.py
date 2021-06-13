import view
import examples
import inspect

class Model:
	"""Model class."""

	def __init__(self):
		"""Init data of a model."""
		self.example_names = dir(examples)

	def start(self, view, controller):
		"""Start of a model."""
		self.view = view
		self.controller = controller
		self.name = self.view.exListbox.get(0)

	def ex_call(self):
		"""Call example's function."""
		self.view.outText.configure(state='normal')

		self.view.outText.delete(1.0, view.tk.END)
		self.view.outText.insert(1.0, "Input: " + self.view.input.get() + "\n")
		self.view.outText.insert(view.tk.END, "Output: ")
		try:
			self.view.outText.insert(view.tk.END, str(eval("examples."
												   + self.name
												   + "("
												   + self.view.input.get()
												   + ")")))
		except Exception as E:
			self.view.outText.insert(view.tk.END, "Incorrect input:\n" + f"{E}")
		
		self.view.outText.configure(state='disabled')

	def show_ex(self):
		"""Show example's code"""
		self.view.codeText.configure(state='normal')
		self.view.outText.configure(state='normal')

		self.view.codeText.delete(1.0, view.tk.END)
		self.view.outText.delete(1.0, view.tk.END)
		self.name = self.view.exListbox.get(self.view.exListbox.curselection()[0])
		self.descr = inspect.getsource(eval("examples." + self.name))
		self.descr = self.descr.replace("\"\"\""
			                            + inspect.getdoc(eval("examples." + self.name))
			                            + "\"\"\"", '')

		self.view.codeText.insert(1.0, self.descr)

		self.view.codeText.configure(state='disabled')
		self.view.outText.configure(state='disabled')

		self.view.example_descr.set(inspect.getdoc(eval("examples." + self.name)))
		self.view.example_hint.set(examples.hints[self.name])

	def enter_select(self):
		"""Enter event handler of select button."""
		self.view.selectButton['background'] = 'green'

	def enter_run(self):
		"""Enter event handler of run button."""
		self.view.runButton['background'] = 'green'

	def enter_quit(self):
		"""Enter event handler of quit button."""
		self.view.quitButton['background'] = 'red'

	def leave_select(self):
		"""Leave event handler of select button."""
		self.view.selectButton['background'] = 'SystemButtonFace'

	def leave_run(self):
		"""Leave event handler of run button."""
		self.view.runButton['background'] = 'SystemButtonFace'

	def leave_quit(self):
		"""Leave event handler of quit button."""
		self.view.quitButton['background'] = 'SystemButtonFace'