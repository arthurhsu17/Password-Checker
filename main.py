import strength_evaluator

def main():
    # input password and it tells you how strong it is
    password = input("Enter a password: ")
    score = strength_evaluator.evaluate_strength(password)
    strength = strength_evaluator.calculate_score(score)
    print(f" Score - {score} & Strength - {strength}")

# this will call the main function upon running the program
if __name__ == "__main__":
    main()