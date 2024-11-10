class GV:
    counter = 1
    def __init__(self, name, score):
        self.id = f"GV{GV.counter:02d}"
        GV.counter += 1
        self.name = name
        self.score = score
    def __str__(self):
        return 