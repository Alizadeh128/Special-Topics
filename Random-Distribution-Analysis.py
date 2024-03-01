import numpy as np
from collections import Counter

student_id = 99121047 
np.random.seed(student_id)

random_numbers = np.random.randint(0, 21, size=10000)

number_counts = Counter(random_numbers)

for number in range(21):
    count = number_counts[number]
    print(f'عدد {number} تکرار شده است {count} بار')
