"""یک بردار از اعداد تصادفی با سید مساوی شماره دانشجویی خود تولید کنید بردار شما 10000 درایه صحیح بین صفر تا بیست(خود بیست هم باشه) داشته باشد سپس تعداد تکرار هر عدد بین صفر تا بیست را در لیست تولیدی محاسبه و چاپ کنید"""

import numpy as np
from collections import Counter

student_id = 99121047 
np.random.seed(student_id)

random_numbers = np.random.randint(0, 21, size=10000)

number_counts = Counter(random_numbers)

for number in range(21):
    count = number_counts[number]
    print(f'عدد {number} تکرار شده است {count} بار')
