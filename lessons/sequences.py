"""Examples of tuple and range sequences"""

# Tuple with no type sequencing?
goat: tuple[str, int] = ("MJ", 23)
SuperGoatAttributes = tuple[str, tuple[str, int]]

for i in goat:
    print(i, end="")
    if i == goat[0]:
        print(" ", end="")

dabber: SuperGoatAttributes = ("dabbit", ["in the sand", 5])
dabber[1][0] = "dutder"
print(dabber)
my_dict = {("superdictlist", "!"):"Son Goku"}


my_range: range = range(0, 10, 2)
print(my_range[2])
for i in my_range:
    print(i)

class my_ranger():


    def __init__(start: int, stop: int, step: int):
        self.start = start
        self.stop = stop
        self.step = step
    
