import random

print("=" * 60)
print("1. Deterministic System")
print("=" * 60)

a = 10
b = 20
print(f"{a} + {b} = {a + b}")
print(f"{a} + {b} = {a + b}")
print("Same input -> Same output\n")

print("=" * 60)
print("2. Probabilistic System")
print("=" * 60)

classes = ["Cat", "Dog", "Rabbit"]
prediction = random.choice(classes)

print("Input: Image")
print(f"Predicted Class: {prediction}")
print("Different executions may produce different predictions.\n")

print("=" * 60)
print("3. Random Experiment - Coin Toss")
print("=" * 60)

coin = random.choice(["Heads", "Tails"])

print("Experiment : Toss a Coin")
print(f"Outcome     : {coin}\n")

print("=" * 60)
print("4. Random Experiment - Dice Roll")
print("=" * 60)

dice = random.randint(1, 6)

print("Experiment : Roll a Die")
print(f"Outcome     : {dice}\n")

print("=" * 60)
print("5. Possible Outcomes")
print("=" * 60)

sample_space_coin = ["Heads", "Tails"]
sample_space_die = [1, 2, 3, 4, 5, 6]

print("Coin Sample Space :", sample_space_coin)
print("Die Sample Space  :", sample_space_die)

print("\nActual Coin Outcome :", coin)
print("Actual Die Outcome  :", dice)

print("\nDone!")