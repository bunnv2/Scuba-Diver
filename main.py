import glob
from ScubaDiver import ScubaDiver

inputs = glob.glob("inputs/*.txt")
with open("output.txt", "w") as f:
    if f.tell() == 0:
        f.write("")

for file in inputs:
    print(file)
    projekt = ScubaDiver(file)
    with open("output.txt", "a") as f:
        f.write(str(projekt.get_minimal_weight_needed_kit()) + "\n")
