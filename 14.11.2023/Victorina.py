class Questions:
    def __init__(self, question, ans1, ans2, ans3, ans4, right):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.right = right

    def __str__(self):
        return f'0'


class Victorina:

    COUNT = 0

    def __init__(self, player1=0, player2=0):
        self.player1 = player1
        self.player2 = player2

    def ask_quest(self, qw):
        print(qw)
        answer = int(input('Answer: '))
        if answer == qw.right:
            

