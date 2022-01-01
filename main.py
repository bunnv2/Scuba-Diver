import glob
from ScubaDiver import ScubaDiver

from timeit import default_timer as timer

inputs = glob.glob("inputs/*.txt")
for i, file in enumerate(inputs):
    with open(f"outputs/output{i+1}.txt", "w") as f:
        if f.tell() == 0:
            f.write("")
    with open(f"clocks/time{i+1}.txt", "w") as f:
        if f.tell() == 0:
            f.write("")

for i, file in enumerate(inputs):
    print(file)
    projekt = ScubaDiver(file)
    start = timer()
    weight = projekt.get_minimal_weight_needed_kit()
    execution_time = timer() - start
    print(f"Execution time: {execution_time}")
    with open(f"outputs/output{i+1}.txt", "a") as f:
        f.write(str(weight) + "\n")
    with open(f"clocks/time{i+1}.txt", "a") as f:
        f.write(str(execution_time) + "\n")
