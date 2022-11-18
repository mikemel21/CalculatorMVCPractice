# connect Controller to Model and View classes
from model import Model
from view import View

#controller class
class Controller:
    def __init__(self):
        # instance variables
        self.model = Model()
        self.view = View(self)

    def main (self):
        self.view.main()

# main
if __name__ == '__main__':
    calc = Controller()
    calc.main()