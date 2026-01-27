class Screen:
    def display(self, content):
        print(f"{content} is being displayed")

class Phone:
    def __init__(self):
        self.screen = Screen() # This works in a way such as the phone would have a screen.

    def unlock(self):
        self.screen.display("Home screen")

redminote13 = Phone()
redminote13.unlock()

        