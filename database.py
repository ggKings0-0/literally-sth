import pandas as pd
import random
import matplotlib.pyplot as plt

users = pd.DataFrame(columns=['id', 'name', 'age', 'country', 'salary'])
for i in range(1, 21):
    users.loc[i] = [i, f'User {i}', random.randint(18, 40), random.choice(['Russia', 'UK', 'Belarus', 'Kazahstan']), random.randint(1000, 5000)]
print(users)
print(f'Middle age: {users["age"].mean()}')
print(f'Median salary: {users["salary"].median()}')
highest_salary = users.groupby('country')['salary'].mean().idxmax()
print(f'Highest salary: {highest_salary}')
plt.scatter(x='age', y='salary', data=users)
plt.show()
