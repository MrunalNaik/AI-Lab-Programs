import os

DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "diseases.txt"
)


def load_diseases(path=DATA_FILE):
    diseases = {}

    if not os.path.exists(path):
        return diseases

    with open(path, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if ":" not in line:
                continue

            name, symptoms = line.split(":", 1)

            symptoms = [s.strip().lower() for s in symptoms.split(",")]

            diseases[name.strip()] = symptoms

    return diseases


def list_diseases(diseases):

    if not diseases:
        print("No diseases in database.")
        return

    print("\nDiseases in Knowledge Base\n")

    for disease, symptoms in diseases.items():

        print(f"{disease} : {', '.join(symptoms)}")


def get_discriminating_symptoms(candidates, diseases):

    if not candidates:
        return []

    scores = {}

    all_symptoms = set()

    for disease in candidates:
        all_symptoms.update(diseases[disease])

    for symptom in all_symptoms:

        have = sum(1 for d in candidates if symptom in diseases[d])

        dont = len(candidates) - have

        if have > 0 and dont > 0:
            score = min(have, dont) / len(candidates)
        else:
            score = 0.01

        scores[symptom] = score

    sorted_scores = sorted(scores.items(),
                           key=lambda x: x[1],
                           reverse=True)

    print("\nDiscriminating symptoms:",
          [f"{s[0]}: {s[1]:.2f}" for s in sorted_scores[:5]])

    return [s[0] for s in sorted_scores]


def diagnose(diseases):

    if not diseases:
        print("No disease data available.")
        return

    positive_symptoms = set()
    asked_symptoms = set()

    candidates = set(diseases.keys())

    question_count = 0

    while candidates:

        symptoms = get_discriminating_symptoms(candidates, diseases)

        symptoms = [s for s in symptoms if s not in asked_symptoms]

        if not symptoms:
            break

        symptom = symptoms[0]

        asked_symptoms.add(symptom)

        question_count += 1

        ans = input(f"\n[Question {question_count}] "
                    f"Do you have '{symptom}'? (y/n): ").lower()

        while ans not in ("y", "n", "yes", "no"):

            ans = input("Enter y or n: ").lower()

        previous = len(candidates)

        if ans.startswith("y"):

            positive_symptoms.add(symptom)

            candidates = {d for d in candidates
                          if symptom in diseases[d]}

        else:

            candidates = {d for d in candidates
                          if symptom not in diseases[d]}

        eliminated = previous - len(candidates)

        print(f"-> Eliminated {eliminated} possibilities")

        print(f"-> Remaining candidates: {len(candidates)}")

        if len(candidates) == 1:

            disease = next(iter(candidates))

            print("\n" + "=" * 60)

            print("DIAGNOSIS:", disease)

            print(f"(Identified after {question_count} questions)")

            print("=" * 60)

            return

        if len(candidates) == 0:

            print("\nNo Matching Disease Found")

            return

    print("\nDiagnosis could not be completed.")


def main():

    diseases = load_diseases()

    while True:

        print("\nExpert System - Simple Disease Diagnoser")

        print("1) Diagnose")

        print("2) List diseases")

        print("3) Quit")

        choice = input("Choose an option: ")

        if choice == "1":

            diagnose(diseases)

        elif choice == "2":

            list_diseases(diseases)

        elif choice == "3":

            print("Exiting...")

            break

        else:

            print("Invalid option.")


if __name__ == "__main__":

    main()