import hunter

class HuntLocals:
    def __init__(self):
        self.last_locals = {}

    def __call__(self, event):
        if self.last_locals != event.locals:
            self.last_locals = dict(event.locals)
            print self.last_locals

# docs http://python-hunter.readthedocs.io/en/latest/reference.html
# how hunter.When works: When Query hunter.Q then Actions.
hunter.trace(hunter.When(
    hunter.Q(module="test.test", function="foo"), HuntLocals()))