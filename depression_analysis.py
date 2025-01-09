import numpy as np
import matplotlib.pyplot as plt

def calculate_depression_score():
    print("Let’s see where you’re at. Be real. 1 = Nah, not me to 5 = Yep, that’s me.\n")
    
    questions = [
        "Feeling down or hopeless?",
        "Still enjoying stuff like before?",
        "Trouble sleeping or sleeping too much?",
        "Low energy, tired all the time?",
        "Feeling bad about yourself?",
        "Hard to focus on basic stuff?",
        "Feeling restless or can’t sit still?",
        "Getting annoyed easily?",
        "Even simple decisions feel tough?",
        "Lost interest in stuff you love?",
        "Big appetite or weight changes?",
        "Thoughts about not being here?"
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
                    print("Stick to 1-5, easy.")
            except ValueError:
                print("Numbers only, no fuss.")

    total_score = np.sum(scores)
    print(f"\nYour score: {total_score}")

    if total_score <= 15:
        result = "You’re fine. Chill."
    elif total_score <= 30:
        result = "Mild signs. Talk to someone, maybe?"
    elif total_score <= 45:
        result = "Moderate signs. Think about getting help."
    elif total_score <= 55:
        result = "It’s serious. Call a pro."
    else:
        result = "Not good. Get help ASAP."

    print(f"Result: {result}")
    print("Just a check-in. Not a real diagnosis.\n")
    
    visualize_depression_score(total_score, result)

def visualize_depression_score(score, result):
    categories = ["Minimal", "Mild", "Moderate", "Moderately Severe", "Severe"]
    score_thresholds = [15, 30, 45, 55, 60]

    fig, ax = plt.subplots()
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    
    plt.bar(categories, score_thresholds, color="gray", edgecolor="white")
    plt.axhline(y=score, color="red", linestyle="--", label=f"Your Score: {score}")
    plt.title(f"Score: {score} ({result})", color="white")
    plt.xlabel("Categories", color="white")
    plt.ylabel("Score", color="white")
    plt.xticks(color="white")
    plt.yticks(color="white")
    plt.legend(facecolor="black", edgecolor="white", labelcolor="white")
    plt.tight_layout()
    plt.show()

calculate_depression_score()
