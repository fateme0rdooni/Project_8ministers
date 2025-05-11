class NQueenGA:
    def __init__(self, n, population_size=100, mutation_rate=0.05, generations=1000):
        self.n = n  # تعداد ملکه‌ها
        self.population_size = population_size  # اندازه جمعیت
        self.mutation_rate = mutation_rate  # نرخ جهش
        self.generations = generations  # تعداد نسل‌ها
        self.population = self.create_initial_population()  # جمعیت اولیه
        
    # تابع برای ایجاد جمعیت اولیه
    def create_initial_population(self):
        return [self.random_chromosome() for _ in range(self.population_size)]