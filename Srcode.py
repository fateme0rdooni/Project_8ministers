class NQueenGA:
    def __init__(self, n, population_size=100, mutation_rate=0.05, generations=1000):
        self.n = n  # تعداد ملکه‌ها
        self.population_size = population_size  # اندازه جمعیت
        self.mutation_rate = mutation_rate  # نرخ جهش
        self.generations = generations  # تعداد نسل‌ها
        self.population = self.create_initial_population() 

    def create_initial_population(self):
        return [self.random_chromosome() for _ in range(self.population_size)]
        # تابع برای محاسبه برازندگی (fitness) کروموزوم
    def fitness(self, chromosome):
        clashes = 0  
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                    clashes += 1
        return self.n * (self.n - 1) // 2 - clashes
    def next_generation(self):
        selected = self.selection()
        next_pop = list(selected)
        while len(next_pop) < self.population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            next_pop.append(child)
        self.population = next_pop[:self.population_size]