
from random import choice 
import matplotlib.pyplot as plt
from collections import Counter 
 
class Die: 
 
    def __init__(self, sides=6): 
        self.sides = range(1, sides + 1) # offset 
 
    def roll(self): 
        return choice(self.sides) 
    
def simulate_dice_rolls(trials): 
    dice = Die(), Die() 
    results = [] 
    for _ in range(trials): 
        result = sum([d.roll() for d in dice])
        results.append(result) 
        probabilities=Counter(results)
    return  probabilities 
 



def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Кількість вдалих спроб випадіння кубиків')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob/sum(probs)*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 500, 1000, 10000, 20000]:
        # Симуляція кидків і обчислення ймовірностей
         probabilities = simulate_dice_rolls(accuracy)

        # Відображення ймовірностей на графіку
         plot_probabilities(probabilities)





