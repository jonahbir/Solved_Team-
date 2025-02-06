At first i tried so solve the problem using class. and it generated a runtime error due to the memory limit. the code was little bit lengthy and complicated. i will put it here:
class team:
    def __init__(self, questions: int, listed_sure: list):
        self.questions = questions
        self.listed_sure = listed_sure
        self.solved = 0  

        assert 1 <= self.questions <= 100, "Invalid input"
        for i in self.listed_sure:
            for j in i:  # i is a sublist, j is an element in the sublist
                assert j == 1 or j == 0, "Invalid input"

    def no_implemented(self):
        for value in self.listed_sure:
            sure = sum(value)  
            if sure >= 2:
                self.solved += 1  
        return self.solved


# Now let's take the input 
n = int(input())

def take_input():
    listed_sure = []
    for i in range(n):
        sures = list(map(int, input().split()))
        listed_sure.append(sures)
    return listed_sure

questions = n
listed_sure = take_input()

the_three_teams = team(questions, listed_sure)
print(the_three_teams.no_implemented())
