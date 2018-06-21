class ball:
    def __init__(self, size = 80):
        self.bgcolor = 'red'
#    def draw():
    def setActive(self, active=True):
        if active:
            self.bgcolor = 'blue'
        else:
            self.bgcolor = 'red'