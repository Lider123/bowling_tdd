class Frame:

    def __init__(self):
        self.score = 0
        self.result = None
        self.throws = 0

    def getScore(self) -> int:
        return self.score

    def setScore(self, score):
        self.score = score

    def getThrows(self) -> int:
        return self.throws

    def getResult(self) -> str:
        return self.result

    def setResult(self, result: str):
        self.result = result

    def add(self, points: int):
        self.score += points
        self.throws += 1

        if self.throws == 2 and self.score < 10:
            self.result = "open"
        elif self.throws == 2 and self.score == 10:
            self.result = "spare"
        elif self.throws == 1 and self.score == 10:
            self.result = "strike"
