import sys


def Variables(file):
    variables = {}
    with open(file) as f:
        for line in f:
            objects = line.split()
            current_node = str(objects[0])[0]
            values = objects[1:]

            for i in range(0, len(values)):
                values[i] = int(values[i])

            if current_node in variables:
                variables[current_node].append(values)
            else:
                variables[current_node] = values
    return variables


def Conditions(file):
    conditions = {}
    with open(file) as f:
        for line in f:
            var1 = line[0]
            var2 = line[4]
            if var1 not in conditions:
                conditions[var1] = line.rstrip().rsplit("\n")
            else:
                conditions[var1].append(line.rstrip().rsplit("\n")[0])
            if var2 not in conditions:
                conditions[var2] = line.rstrip().rsplit("\n")
            else:
                conditions[var2].append(line.rstrip().rsplit("\n")[0])
    return conditions


def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    print("Variables: ", Variables(file1))
    print("Conditions: ", Conditions(file2))


main()
