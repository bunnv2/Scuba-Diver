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

    def sort_by_minimal_weights(self):
        """
        Sort the kits by the minimum weight.
        """
        self.kits.sort(key=lambda kit: kit[2])

    def get_needed_kits_to_fit_tank(self):
        """
        Get the list of kits with their parameters needed to fill the tank.
        """
        oxygen_cap, oxygen_sum = self.oxygen_needed, 0
        nitrogen_cap, nitrogen_sum = self.nitrogen_needed, 0
        self.sort_by_minimal_weights()

        needed_kits = []
        # sub_list = []

        # i = 0
        # prev = 0
        # while True:
        #     if oxygen_sum <= oxygen_cap or nitrogen_sum <= nitrogen_cap:
        #         oxygen_sum += self.kits[i][0]
        #         nitrogen_sum += self.kits[i][1]
        #         sub_list.append(self.kits[i])
        #         prev = i
        #     else:
        #         needed_kits.append(sub_list)
        #         sub_list = []
        #         oxygen_sum = 0
        #         nitrogen_sum = 0
        #     i += 1
        #     if i == self.number_of_kits:
        #         i = prev
        #         needed_kits.append(sub_list)
        #         break

        # for idx, kit in enumerate(self.kits):
        # if oxygen_sum <= oxygen_cap or nitrogen_sum <= nitrogen_cap:
        #     oxygen_sum += kit[0]
        #     nitrogen_sum += kit[1]
        #     needed_kits.append(idx)
        # needed_kits = [self.kits[i] for i in needed_kits]

        return needed_kits

    def get_needed_kits_weight(self):
        """
        Get the total weight of the kits needed to fill the tank.
        """
        needed_kits = self.get_needed_kits_to_fit_tank()
        return sum([i[2] for i in needed_kits])

    def get_all_kit_combinations(self):
        """
        Get all possible combinations of kits.
        """
        needed_kits = self.get_needed_kits_to_fit_tank()
        return list(
            itertools.combinations(
                self.kits,
            )
        )


projekt = ScubaDiver("input.txt")
# print(projekt.kits)
# print("oxygen:", projekt.oxygen_needed, "nitrogen:", projekt.nitrogen_needed)
# print(projekt.get_needed_kits_to_fit_tank())
# print("Total weight:", projekt.get_needed_kits_weight())
print(projekt.get_all_kit_combinations())
