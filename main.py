from model import Model
from view import View
from controller import Controller

AppModel = Model()
AppController = Controller()
AppView = View(model=AppModel, controller=AppController)
AppModel.start(AppView, AppController)
AppController.start(AppView, AppModel)
AppView.mainloop()