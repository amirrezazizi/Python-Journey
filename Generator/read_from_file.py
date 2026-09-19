def read_lines(filename):
    with open(filename) as file:
        for line in file:
            yield line

for line in read_lines("pythonJourney_linux/Python-Journey/Generator/sample.txt"):
    print(line)