import model

class Controller:
	"""Controller class."""

	def start(self, view, model):
		"""Start of the controller."""
		self.model = model
		self.view = view
		self.view.quitButton.bind("<Enter>", self.model.enter_quit())
		self.view.quitButton.bind("<Leave>", self.model.leave_quit())
		self.view.selectButton.bind("<Enter>", self.model.enter_select())
		self.view.selectButton.bind("<Leave>", self.model.leave_select())
		self.view.runButton.bind("<Enter>", self.model.enter_run())
		self.view.runButton.bind("<Leave>", self.model.leave_run())
		self.view.inputEntry.bind("<Return>", self.enter_press)

	def enter_press(self, event):
		self.run()

	def select(self):
		"""Select button handler."""
		self.model.show_ex()

	def run(self):
		"""Run button handler."""
		self.model.ex_call()