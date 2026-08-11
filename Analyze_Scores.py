scores = [78,92,65,88,100,54,81]

def analyze_scores(scores):
    highest = scores[0]
    lowest = scores [0]
    total = 0

    for score in scores:
        total += score

        if score > highest:
            highest = score
        elif score < lowest:
            lowest = score
    average = total / len(scores)

    return highest, lowest, average


highest, lowest, average = analyze_scores(scores)
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Average score: {average:.2f}")