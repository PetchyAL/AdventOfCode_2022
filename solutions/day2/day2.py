import pandas as pd
data = pd.read_csv("input.txt",names=["opp","self"],sep=" ")

def part_one():
    final_score = 0
    scores = { "X": 1, "Y": 2, "Z": 3 }
    loss = { "A": "Z", "B": "X", "C": "Y" }
    win = { "A": "Y", "B": "Z", "C": "X" }

    for _index,round in data.iterrows():
        final_score += scores[round["self"]]
        if (round["self"] == loss[round["opp"]]):
            continue
        elif (round["self"] == win[round["opp"]]):
            final_score += 6
        else:
            final_score += 3
    return final_score

def part_two():
    final_score = 0
    scores = { "A": 1, "B": 2, "C": 3 }
    loss = { "A": "C", "B": "A", "C": "B" }
    wins = { "A": "B", "B": "C", "C": "A" }

    for _index,round in data.iterrows():
        if (round["self"] == "X"):
            final_score += scores[loss[round["opp"]]]
        elif (round["self"] == "Y"):
            final_score += scores[round["opp"]] + 3
        else:
            final_score += scores[wins[round["opp"]]] + 6
    return final_score

print(part_one())
print(part_two())
