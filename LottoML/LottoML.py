import csv
from collections import Counter
import math

def analyze_lottery_data(file_path):
    number_frequency = Counter()
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for i in range(1, 7):
                number = int(row[f'Num{i}'])
                number_frequency[number] += 1
    
    total_draws = sum(number_frequency.values()) // 6
    
    probabilities = {num: freq / total_draws for num, freq in number_frequency.items()}
    
    sorted_numbers = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
    
    most_probable_numbers = [num for num, _ in sorted_numbers[:6]]
    
    return most_probable_numbers, probabilities

def calculate_winning_probability(probabilities, most_probable_numbers):
    adjusted_prob = math.prod(probabilities[num] for num in most_probable_numbers)
    theoretical_prob = 1 / math.comb(49, 6)
    return adjusted_prob, theoretical_prob

# File 
file_path = './Data/Results.csv'

# Analyze the data
most_probable, probabilities = analyze_lottery_data(file_path)

# Calculate winning probabilities
adjusted_prob, theoretical_prob = calculate_winning_probability(probabilities, most_probable)

# Print results
print(f"6 most probable numbers for the next lottery: {most_probable}")
print(f"\nAdjusted probability of winning with these numbers: {adjusted_prob:.2e}")
print(f"Theoretical probability of winning: {theoretical_prob:.2e}")
print(f"Ratio (Adjusted / Theoretical): {adjusted_prob / theoretical_prob:.2f}")
