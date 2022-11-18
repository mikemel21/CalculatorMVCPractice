class Model:
    def __init__(self):
        # holds what is displayed in view entry
        self.val = ''
        # previous value
        self.prevVal = ''
        # stores the operator input
        self.operator = ''

    def calc(self, label):
        # if user hits the 'clear' button
        if label == 'C':
            self.operator = ''
            self.prevVal = ''
            self.val = ''
        # user hits the inverse button
        elif label == '+/-':
            if self.val[0] == '-':
                self.val = self.val[1:]
            else:
                self.val = '-' + self.val
        elif label == '%': pass
        elif label == '.':
            # check if there is already a decimal present
            if not label in self.val:
                self.val += label
        elif label == '=':
            self.val = str(self.solve())
        # checks if the button pressed is a number
        elif isinstance(label, int):
            #add number pressed to equation
            self.val += str(label)
        # +, -, *, /
        else:
            # store operator and previous value only if it is nonempty
            if self.val:
                self.operator = label
                self.prevVal = self.val
                self.val = ''

        return self.val;
    
    # evaluates the equation
    def solve(self):
        return eval(self.prevVal + self.operator + self.val)
