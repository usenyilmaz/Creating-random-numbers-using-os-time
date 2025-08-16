import matplotlib.pyplot as plt
import random
from collections import Counter

# Generate random numbers
random_numbers = []

for i in range(1000000):
    random_numbers.append(random.randint(1, 10))

# Count the frequency of each number
number_counts = Counter(random_numbers)

# Create bar chart
plt.figure(figsize=(10, 6))
numbers = list(range(1, 11))  # All possible numbers (1 to 10)
counts = [number_counts[num] for num in numbers]  # Count for each number

plt.bar(numbers, counts, color='skyblue', edgecolor='navy', alpha=0.7)
plt.title('Frequency of Random Numbers Generated (1-10)')
plt.xlabel('Random Number')
plt.ylabel('Frequency (Count)')
plt.xticks(numbers)  # Show all numbers 1-10 on x-axis
plt.grid(True, alpha=0.3, axis='y')

# Add count labels on top of each bar
for i, count in enumerate(counts):
    plt.text(numbers[i], count + max(counts)*0.01, str(count), 
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('random_numbers_frequency.png', dpi=300, bbox_inches='tight')
plt.show()