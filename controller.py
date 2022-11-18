# connect Controller to Model and View classes
from model import Model
from view import View

#controller class
class Controller:
    def __init__(self):
        # instance variables
        self.model = Model()
        self.view = View(self)

    # controller for when button is clicked
    def ButtonClicked(self, label):
        calculation = self.model.calc(label)

        # changes the equation displayed in the view
        self.view.valueVar.set(calculation)

    def main (self):
        self.view.main()

# main
if __name__ == '__main__':
    calc = Controller()
    calc.main()