class Model:
    def __init__(self):
        # holds what is displayed in view entry
        self.equation = ''

    def calc(self, label):
        # if user hits the 'clear' button
        if label == 'C':
            self.value = 0
        
        return self.value;
