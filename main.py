import itertools


class ScubaDiver:
    """ScubaDiver class which represents a scuba diver who needs to find the oxygen and nitrogen kits to fill his tank."""

    def __init__(self, file) -> None:
        """
        Initialize the ScubaDiver object.
        Parameters:
            file: The file to read.
        """

        with open(file) as f:
            line = f.readline()
            self.oxygen_needed = line.split(" ")[0]
            try:
                self.oxygen_needed = int(self.oxygen_needed)
                if self.oxygen_needed < 0:
                    raise ValueError("Oxygen needed must be positive")
                if self.oxygen_needed > 21:
                    raise ValueError("Oxygen needed must be less than 22")

            except ValueError:
                raise ValueError("Oxygen must be an integer.")

            self.nitrogen_needed = line.split(" ")[1]
            try:
                self.nitrogen_needed = int(self.nitrogen_needed)
                if self.nitrogen_needed < 0:
                    raise ValueError("Nitrogen needed must be positive")
                if self.nitrogen_needed > 79:
                    raise ValueError("Nitrogen needed must be less than 80")

            except ValueError:
                raise ValueError("Nitrogen must be an integer.")
            self.number_of_kits = f.readline()
            try:
                self.number_of_kits = int(self.number_of_kits)
                if self.number_of_kits < 0:
                    raise ValueError("Number of kits must be positive.")
                if self.number_of_kits > 1000:
                    raise ValueError("Number of kits must be less than 1000.")
            except ValueError:
                raise ValueError("Number of kits must be an integer.")

            self.kits = [f.readline().split(" ") for i in range(self.number_of_kits)]

            for i in range(self.number_of_kits):
                self.kits[i][-1] = self.kits[i][-1].strip()

            try:
                self.kits = [[int(i) for i in kit] for kit in self.kits]
            except ValueError:
                raise ValueError("Kits must be integers.")

    def get_all_kits_combinations(self):
        """
        Get all the combinations of kits.
        """
        all_kits_combinations = []
        for i in range(len(self.kits)):
            combination_kit = itertools.combinations(self.kits, i)
            combination_list = list(combination_kit)
            all_kits_combinations.append(combination_list)
        return all_kits_combinations

    def get_needed_kits_to_fit_tank(self):
        """
        Get the kits needed to fill the tank.
        """
        needed_kits = []
        all_kits_combinations = self.get_all_kits_combinations()
        for combination in all_kits_combinations:
            for list_of_kits in combination:
                sum_of_oxygen = [sum(i[0] for i in list_of_kits)]
                sum_of_nitrogen = [sum(i[1] for i in list_of_kits)]
                if (
                    sum_of_oxygen[0] >= self.oxygen_needed
                    and sum_of_nitrogen[0] >= self.nitrogen_needed
                ):
                    needed_kits.append(list_of_kits)
        return needed_kits

    def get_minimal_weight_needed_kit(self):
        """
        Get the minimal weight needed kit.
        """
        needed_kits = self.get_needed_kits_to_fit_tank()
        minimal_weight = needed_kits[0][0][2]
        minimal_weight_kit = needed_kits[0]
        for kit in needed_kits:
            if kit[0][2] < minimal_weight:
                minimal_weight = kit[0][2]
                minimal_weight_kit = kit
        minimal_weight = sum(i[2] for i in minimal_weight_kit)
        return minimal_weight


projekt = ScubaDiver("input.txt")
with open("output.txt", "w") as f:
    f.write(str(projekt.get_minimal_weight_needed_kit()))
