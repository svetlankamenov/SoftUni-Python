from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name:str, budget:int, animal_capacity:int, workers_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal:Animal, price:int):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker:Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name:str):
        for hired_worker in self.workers:
            if hired_worker.name == worker_name:
                self.workers.remove(hired_worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary_cost = 0
        for hired_worker in self.workers:
            total_salary_cost += hired_worker.salary

        if self.__budget < total_salary_cost:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salary_cost
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_budget_for_care = 0
        for animal in self.animals:
            total_budget_for_care += animal.money_for_care

        if self.__budget < total_budget_for_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_budget_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount:int):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        output = ""

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        output += f"You have {len(self.animals)} animals\n"
        if lions:
            output += f"----- {len(lions)} Lions:\n"
            for lion in lions:
                output += f"{lion}\n"
        if tigers:
            output += f"----- {len(tigers)} Tigers:\n"
            for tiger in tigers:
                output += f"{tiger}\n"
        if cheetahs:
            output += f"----- {len(cheetahs)} Cheetahs:\n"
            for cheetah in cheetahs:
                output += f"{cheetah}\n"

        return output.rstrip()

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        output = ""

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)

        output += f"You have {len(self.workers)} workers\n"
        if keepers:
            output += f"----- {len(keepers)} Keepers:\n"
            for keeper in keepers:
                output += f"{keeper}\n"
        if caretakers:
            output += f"----- {len(caretakers)} Caretakers:\n"
            for caretaker in caretakers:
                output += f"{caretaker}\n"
        if vets:
            output += f"----- {len(vets)} Vets:\n"
            for vet in vets:
                output += f"{vet}\n"

        return output.rstrip()