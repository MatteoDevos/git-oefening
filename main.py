students = {
    "Emma": 14,
    "Lucas": 17,
    "Noah": 12
}

total = 0

for name, score in students.items():
    print(f"{name}: {score}/20")
    total += score

average = total / len(students)

print(f"\nGemiddelde score: {average:.2f}/20")