from dev.Frame import Frame


class Game:

    def __init__(self):
        self.currentFrame = 0
        self.frames = list()
        for i in range(10):
            self.frames.append(Frame())

    def getScore(self) -> int:
        return sum([f.getScore() for f in self.frames])

    def add(self, points: int):
        prev_frame = self.frames[self.currentFrame-1]
        curr_frame = self.frames[self.currentFrame]
        curr_frame.add(points)

        if prev_frame.getResult() == "strike" and curr_frame.getThrows() < 3 \
                or prev_frame.getResult() == "spare" and curr_frame.getThrows() == 1:
            prev_frame.setScore(prev_frame.getScore() + points)

        if self.currentFrame == 9 and curr_frame.getResult() in "spare strike".split():
            curr_frame.setResult(None)

        if not curr_frame.getResult() is None:
            self.currentFrame += 1
