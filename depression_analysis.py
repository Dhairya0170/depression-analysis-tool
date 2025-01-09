import numpy as np
import matplotlib.pyplot as plt

def calculate_depression_score():
    questions = [
        "Do you feel down, depressed, or hopeless?",
        "Do you enjoy activities as much as before?",
        "Do you have trouble falling asleep, staying asleep, or sleeping too much?",
        "Do you feel tired or have little energy?",
        "Do you feel bad about yourself, or that you're a failure or let yourself or your family down?",
        "Do you have trouble concentrating on things like reading or watching TV?",
        "Do you feel restless or find it hard to sit still?",
        "Do you feel more irritable or easily annoyed than usual?",
        "Do you find it hard to make decisions, even simple ones?",
        "Have you lost interest or pleasure in doing things you usually enjoy?",
        "Have you experienced a significant change in appetite or weight?",
        "Do you have thoughts of hurting yourself or that you'd be better off not alive?",
    ]

    options = {
        5: "Very True",
        4: "True",
        3: "Somewhat True",
        2: "False",
        1: "Very False"
    }

    scores = []
    print("Please answer the following questions honestly by entering a number from 1 to 5:")
    print("1 = Very False, 2 = False, 3 = Somewhat True, 4 = True, 5 = Very True\n")

    for question in questions:
        print(question)
        while True:
            try:
                answer = int(input("Your answer (1-5): ").strip())
                if answer in options:
                    scores.append(answer)
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 5.")

    total_score = np.sum(scores)
    print("\nYour Depression Score:", total_score)

    if total_score <= 15:
        result = "Minimal or no depression"
        advice = "Keep maintaining a positive mental health routine!"
    elif total_score <= 30:
        result = "Mild depression"
        advice = "It might help to talk to someone you trust or a mental health professional."
    elif total_score <= 45:
        result = "Moderate depression"
        advice = "Consider seeking support from a counselor or therapist."
    elif total_score <= 55:
        result = "Moderately severe depression"
        advice = "It's important to reach out to a healthcare provider for help."
    else:
        result = "Severe depression"
        advice = "Please seek immediate assistance from a mental health professional."

    print(f"Result: {result}")
    print(f"Advice: {advice}\n")
    print("Remember, this tool is for informational purposes only and not a substitute for professional diagnosis.")

    visualize_depression_score(total_score, result)

def visualize_depression_score(score, result):
    categories = [
        "Minimal or No Depression",
        "Mild Depression",
        "Moderate Depression",
        "Moderately Severe Depression",
        "Severe Depression",
    ]
    score_thresholds = [15, 30, 45, 55, 60]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, score_thresholds, color="lightblue", label="Score Thresholds")
    plt.axhline(y=score, color="red", linestyle="--", label=f"Your Score: {score}")

    plt.xlabel("Depression Categories")
    plt.ylabel("Score")
    plt.title(f"Your Depression Score: {score} ({result})")
    plt.xticks(rotation=15)
    plt.legend()
    plt.tight_layout()
    plt.show()

calculate_depression_score()
