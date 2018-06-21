class ball:
    def __init__(self, size = 80):
        self.bgcolor = '0'
#    def draw():
    def setActive(self, active=True):
        if active:
            self.bgcolor = '1'
        else:
            self.bgcolor = '0'