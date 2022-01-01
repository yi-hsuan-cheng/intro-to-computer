class Judge:
    def __init__(self, answer: str) -> None:

        """
        Set the answer as the attribute of Judge
        answer: (int) the final answer
        """
        # TODO

        self.answer = answer

    def guess(self, num: str) -> bool:
        """
        Method that guess the number, it'll print info that shows:
            Your guess is ...; the result is xAxB
            e.g.: Your guess is 0123; the result is 0A1B
        num: the number that it guessed
        return: whether the player guess the correct answer
        """
        # TODO

        a = 0
        b = 0
        num = str(num)
        for i in range(len(self.answer)):
            if num[i] == self.answer[i]:
                a = a + 1
            elif num[i] != self.answer[i]:
                for j in range(len(self.answer)):
                    if num[i] == self.answer[j]:
                        b = b + 1
        if a == len(self.answer):
            print("Your guess is ", num, "; the result is ", a, "A", b, "B\n", sep='')
            return True
        else:
            print("Your guess is ", num, "; the result is ", a, "A", b, "B\n", sep='')
            return False


def read_input(guess_len: int) -> str:
    """
    Function that read player's guess.
    guess_len: length the the player should guess. it would be same as the length of answer
    return: the valid string guessed by player

    You should show the hint message:
        "Enter your guess:\n"
    If the player's guess is invalid, you should print:
        "Invalid, please enter your guess again:\n"
    Note: a valid guess means contain only guess_len non-repetitive integer range from 0~9
    """
    # TODO

    guess = input("Enter your guess:\n")

    while True:
        invalid = 0

        if len(guess) != guess_len:
            print("Invalid, please enter your guess again:\n")
            invalid = invalid + 1
            guess = input()

        elif guess.isdigit() == 0:
            print("Invalid, please enter your guess again:\n")
            invalid = invalid + 1
            guess = input()

        else:
            repeat = 0
            for i in range(guess_len - 1):
                for j in range(i + 1, guess_len):
                    if guess[i] == guess[j]:
                        repeat = repeat + 1
            if repeat != 0:
                print("Invalid, please enter your guess again:\n")
                invalid = invalid + 1
                guess = input()

        if invalid == 0:
            return guess


def enter_answer() -> str:
    """
    Function that enter the answer, you can assume that the answer must be valid.
    """
    # TODO

    ans = input()
    return ans
