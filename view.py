import tkinter as tk
import Pmw

class View(tk.Frame):
    """View class."""

    def __init__(self, master=None, model=None, controller=None):
        """Create root window."""
        tk.Frame.__init__(self, master)
        self.model = model
        self.controller = controller
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def createWidgets(self):
        """Widgets."""
        #Create quit button
        self.quitButton = tk.Button(self, text='Exit', command=self.quit)

        #Create select button to select code example
        self.selectButton = tk.Button(self, text='Select', command=self.controller.select)

        #Create run button to run example with custom input
        self.runButton = tk.Button(self, text='RUN', command=self.controller.run)

        #Create Text window for code example with scrollbar
        self.codeText = tk.Text(self, state='disabled')
        self.codeScrollbar = tk.Scrollbar(self, command=self.codeText.yview)
        self.codeText['yscrollcommand'] = self.codeScrollbar.set

        #Create Text window for input result with scrollbar
        self.outText = tk.Text(self, state='disabled')
        self.outScrollbar = tk.Scrollbar(self, command=self.outText.yview)
        self.outText['yscrollcommand'] = self.outScrollbar.set

        #Create and initialize Listbox window for selecting examples with scrollbar
        self.boxScrollbar = tk.Scrollbar(self)
        self.exListbox = tk.Listbox(self, yscrollcommand=self.boxScrollbar.set)
        for c in self.model.example_names:
            if (c[0] != '_') and (c != 'np') and (c!='hints'):
                self.exListbox.insert(tk.END, c)
        self.boxScrollbar.config(command=self.exListbox.yview)
        
        #Set default selection for listbox
        self.exListbox.select_set(0)

        #Create Label for example's description
        self.example_descr = tk.StringVar()
        self.nameLabel = tk.Label(self, textvariable=self.example_descr, bg="#333", fg="#eee", font="Arial 20", bd="3")

        #Create Label for input's hint
        self.example_hint = tk.StringVar()
        self.hintLabel = tk.Label(self, textvariable=self.example_hint)

        #Create Entry window for custom input
        self.input = tk.StringVar(self, value="Type here...")
        self.inputEntry = tk.Entry(self, textvariable=self.input)

        #Place widgets on a grid
        self.exListbox.grid(row=0, column=0, rowspan=3, sticky="NEWS")
        self.boxScrollbar.grid(row=0, column=1, rowspan=3, sticky="NES")
        self.nameLabel.grid(row=0, column=2, columnspan=4, sticky="NEWS")
        self.codeText.grid(row=1, column=2, sticky="NEWS")
        self.codeScrollbar.grid(row=1, column=3, sticky="NES")
        self.outText.grid(row=1, column=4, sticky="NEWS")
        self.outScrollbar.grid(row=1, column=5, sticky="NES")
        self.inputEntry.grid(row=2, column=2, columnspan=3, sticky="NEWS")
        self.runButton.grid(row=2, column=5, sticky="NEWS")
        self.selectButton.grid(row=3, column=0, columnspan=2, sticky="NEWS")
        self.hintLabel.grid(row=3, column=2, columnspan=3, sticky="NEWS")
        self.quitButton.grid(row=3, column=5, sticky="NEWS")
        
