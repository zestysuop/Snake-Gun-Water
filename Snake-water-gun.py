import random

# Choices
choices = ["snake", "water", "gun"]

print("=== Snake Water Gun Game ===")
print("Choose one:")
print("1. Snake")
print("2. Water")
print("3. Gun")

user_choice = input("\nEnter your choice: ").lower()

# Validate input
if user_choice not in choices:
    print("Invalid choice! Please choose snake, water, or gun.")
    exit()

# Computer chooses randomly
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Check result
if user_choice == computer_choice:
    print("\nIt's a Draw!")

elif (
    (user_choice == "snake" and computer_choice == "water") or
    (user_choice == "water" and computer_choice == "gun") or
    (user_choice == "gun" and computer_choice == "snake")
):
    print("\n🎉 Congratulations! You Win!")

else:
    print("\n😔 Computer Wins!")
