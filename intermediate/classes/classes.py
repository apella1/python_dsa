class Cookie:
    def __init__(self, color: str) -> None:
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color
