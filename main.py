import threading

def play_game():
    print("welcome to IQ game")

    score = 0
    num = 2


    while True:
        question = f"{num} + {num} is: "
        answer = input(question)

        try:
            if int(answer) == num * 2:
                score += 1
                print("Correct!\n")
                num *= 2
            else:
                print(f"Incorrect! Game Over. Correct is: {num*2}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Your final score is: {score}")

if __name__ == "__main__":
    play = threading.Thread(target=play_game)
    play.start()
