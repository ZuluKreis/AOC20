def partOne():
    with open("input1.txt", "r") as file:
        lines = file.read().split("\n")
        liste = [int(number) for number in lines]
        for i in range(len(liste)):
            for j in range(i + 1, len(liste)):
                if liste[i] + liste[j] == 2020:
                    return liste[i] * liste[j]


def partTwo():
    with open("input1.txt", "r") as file:
        lines = file.read().split("\n")
        liste = [int(number) for number in lines]
        for i in range(len(liste)):
            for j in range(i + 1, len(liste)):
                for k in range(j + 1, len(liste)):
                    if liste[i] + liste[j] + liste[k] == 2020:
                        return liste[i] * liste[j] * liste[k]

print(partTwo())