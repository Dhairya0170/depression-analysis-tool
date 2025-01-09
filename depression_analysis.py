import numpy as np
import matplotlib.pyplot as plt

def calculate_depression_score():
    print("Alright, let’s see where your head’s at. Answer honestly. Scale: 1 = Nah, not me to 5 = Yep, that’s me.\n")
    
    questions = [
        "Feeling down, depressed, or hopeless lately?",
        "Enjoying activities as much as you used to?",
        "Trouble sleeping (too much or too little)?",
        "Low energy or feeling tired all the time?",
        "Feeling bad about yourself or thinking you’re a failure?",
        "Struggling to concentrate, even on simple stuff?",
        "Feeling restless or like you can’t sit still?",
        "Getting annoyed or irritable more often?",
        "Decisions feel like a giant math problem?",
        "Lost interest in stuff you usually enjoy?",
        "Noticing big changes in appetite or weight?",
        "Ever thought you’d be better off not here?",
    ]

    scores = []
    for question in questions:
        print(question)
        while True:
            try:
                answer = int(input("Your answer (1-5): "))
                if 1 <= answer <= 5:
                    scores.append(answer)
                    break
                else:
                    print("It’s 1 to 5, don’t overthink it.")
            except ValueError:
                print("Numbers only, please. Let’s keep it simple.")

    total_score = np.sum(scores)
    print(f"\nYour total score: {total_score}")

    if total_score <= 15:
        result = "You’re good. No major concerns."
    elif total_score <= 30:
        result = "Mild signs. Maybe talk to someone if you’re feeling off."
    elif total_score <= 45:
        result = "Moderate signs. Getting some professional advice might help."
    elif total_score <= 55:
        result = "Moderately severe. Definitely talk to a professional."
    else:
        result = "Severe. Don’t wait—reach out for help now."

    print(f"Assessment: {result}")
    print("This is just a check-in, not a diagnosis. If anything feels off, seek real advice.\n")
    
    visualize_depression_score(total_score, result)

def visualize_depression_score(score, result):
    categories = ["Minimal", "Mild", "Moderate", "Moderately Severe", "Severe"]
    score_thresholds = [15, 30, 45, 55, 60]

    plt.style.use("dark_background")
    plt.bar(categories, score_thresholds, color="gray", edgecolor="white")
    plt.axhline(y=score, color="red", linestyle="--", label=f"Your Score: {score}")
    plt.title(f"Your Score: {score} ({result})", color="white")
    plt.xlabel("Depression Categories", color="white")
    plt.ylabel("Score", color="white")
    plt.xticks(color="white")
    plt.yticks(color="white")
    plt.legend(facecolor="black", edgecolor="white")
    plt.tight_layout()
    plt.show()

calculate_depression_score()
