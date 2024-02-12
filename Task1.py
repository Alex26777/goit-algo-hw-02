from queue import Queue

# Створення екземпляру черги
q = Queue()

# Додавання елементів до черги
for i in range(5):  # Генеруємо 5 запитів
    q.put(f"Запит {i+1}")

# Тепер ми вилучаємо елементи з черги
while not q.empty():
    # Вилучення елементів з черги
    request = q.get()
    print(f"Обробляємо {request}")
