class CoffeeMachine:
    def __init__(self):
        self.resources = {
            'water': 400,
            'milk': 540,
            'coffee_beans': 120,
            'disposable_cups': 9,
            'money': 550
        }
        self.prices = {
            '1': {'name': 'espresso', 'price': 4, 'recipe': {'water': 250, 'milk': 0, 'coffee_beans': 16}},
            '2': {'name': 'latte', 'price': 7, 'recipe': {'water': 350, 'milk': 75, 'coffee_beans': 20}},
            '3': {'name': 'cappuccino', 'price': 6, 'recipe': {'water': 200, 'milk': 100, 'coffee_beans': 12}}
        }

    def process_action(self, action):
        if action == 'buy':
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            if choice == 'back':
                return
            if choice in self.prices:
                if all(self.resources[resource] >= amount for resource, amount in self.prices[choice]['recipe'].items()):
                    print("I have enough resources, making you a coffee!")
                    for resource, amount in self.prices[choice]['recipe'].items():
                        self.resources[resource] -= amount
                    self.resources['money'] += self.prices[choice]['price']
                    self.resources['disposable_cups'] -= 1
                else:
                    print("Sorry, not enough resources!")
            else:
                print("Invalid choice!")
        elif action == 'fill':
            self.resources['water'] += int(input("Write how many ml of water you want to add:\n"))
            self.resources['milk'] += int(input("Write how many ml of milk you want to add:\n"))
            self.resources['coffee_beans'] += int(input("Write how many grams of coffee beans you want to add:\n"))
            self.resources['disposable_cups'] += int(input("Write how many disposable coffee cups you want to add:\n"))
        elif action == 'take':
            print(f"I gave you ${self.resources['money']}")
            self.resources['money'] = 0
        elif action == 'remaining':
            self.display_state()

    def display_state(self):
        print("The coffee machine has:")
        for resource, amount in self.resources.items():
            if resource != 'money':
                print(f"{amount} of {resource}")
            else:
                print(f"${amount} of {resource}")
        print()

# Створення об'єкта кавомашини
coffee_machine = CoffeeMachine()

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'exit':
        break
    elif action in ['buy', 'fill', 'take', 'remaining']:
        coffee_machine.process_action(action)
