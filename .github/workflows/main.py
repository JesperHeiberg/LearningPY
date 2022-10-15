class players:
    ambo=[0,0,0,0,0,0]
    kalaha=0
    hand=0
    def __init__(self):
        self.ambo = [6, 6, 6, 6, 6, 6]

    def addToAmbo(self, position):
        self.ambo[position]=self.ambo[position]+1

    def moveFromAmbo(self, position):
        self.ambo[position]=self.ambo[position]-1

    def addToKalaha(self):
        self.kalaha=self.kalaha+1

    def addToHand(self, numberOfBalls):
        self.hand=numberOfBalls

    def moveFromHand(self, position):
        self.hand=self.hand-1




