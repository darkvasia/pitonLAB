import random

class EnhancedCafe:
    def __init__(self, num_tables, num_waiters):
        self.num_tables = num_tables
        self.num_waiters = num_waiters
        self.tables = [None] * num_tables
        self.waiters = [0] * num_waiters
        self.total_customers = 0
        self.lost_customers = 0
        self.waiting_customers = 0

    def new_customer(self, current_time, peak_hours):
        # Шанс приходу клієнта змінюється в залежності від часу дня
        if random.random() < (0.2 if peak_hours else 0.05):
            # Якщо всі столи зайняті, клієнт чекає
            if None not in self.tables:
                self.waiting_customers += 1
                if self.waiting_customers > 5:  # Максимальна кількість клієнтів, які чекають
                    self.lost_customers += 1
                    self.waiting_customers -= 1
            else:
                table_index = self.tables.index(None)
                self.tables[table_index] = current_time
                self.total_customers += 1
                self.waiting_customers = max(0, self.waiting_customers - 1)

                # Призначення офіціанта
                available_waiter = self.waiters.index(min(self.waiters))
                self.waiters[available_waiter] = current_time + random.randint(5, 15)

    def update_tables(self, current_time):
        # Звільнення столів
        for i in range(len(self.tables)):
            if self.tables[i] is not None:
                if current_time - self.tables[i] > random.randint(30, 60):
                    self.tables[i] = None

def simulate_enhanced_cafe(hours=12, num_tables=10, num_waiters=5):
    cafe = EnhancedCafe(num_tables, num_waiters)
    for hour in range(hours):
        peak_hours = 11 <= hour < 14 or 18 <= hour < 21  # Пікові години
        for minute in range(60):
            current_time = hour * 60 + minute
            cafe.new_customer(current_time, peak_hours)
            cafe.update_tables(current_time)

    return cafe

# Тестування симуляції з різною кількістю столиків та офіціантів
results = []
for tables in range(5, 21, 5):
    for waiters in range(1, 6):
        simulation = simulate_enhanced_cafe(num_tables=tables, num_waiters=waiters)
        results.append((tables, waiters, simulation.total_customers, simulation.lost_customers))

# Вивід результатів
results

