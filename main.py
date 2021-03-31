import sys


# get variables and their domains and store them in a dictionary
# returns a dictionary with key as the variable and value as the domain
def Variables(file):
    variables = {}  # key: variable(str), value: domain(ints)
    with open(file) as f:
        for line in f:
            objects = line.split()  # turn line into a list
            current_var = str(objects[0])[0]  # char letter (A, B, C, or D, ...)
            values = objects[1:]  # store domain of current variable in a list

            for i in range(0, len(values)):  # convert values to int
                values[i] = int(values[i])

            if current_var in variables:  # check if current variable in list
                variables[current_var].append(values)  # if so, add values to key(current node)
            else:
                variables[current_var] = values  # otherwise create a key with values
    return variables


# get conditions from a file
# returns a dictionary with variables as keys and conditions as values stored in a list
def Conditions(file):
    conditions = {}  # key: variable(str), value: conditions(str)
    with open(file) as f:
        for line in f:  # for each condition in file
            var1 = line[0]  # get first variable
            var2 = line[4]  # get second variable
            if var1 not in conditions:  # if variable not in dictionary
                conditions[var1] = line.rstrip().rsplit("\n")  # create variable and store the whole condition
            else:
                conditions[var1].append(line.rstrip().rsplit("\n")[0])  # otherwise append to list
            if var2 not in conditions:  # do same to second variable
                conditions[var2] = line.rstrip().rsplit("\n")
            else:
                conditions[var2].append(line.rstrip().rsplit("\n")[0])
    return conditions


def CSP(variables, conditions, mode):
    print("Variables: ", variables)  # for debug purposes
    print("Conditions: ", conditions)  # for debug purposes
    print("Mode: ", mode)  # for debug purposes
    sorted_variables = sorted(conditions)
    for variable in sorted_variables:
        for value in range(len(variables[variable])):
            print(variable, "=", variables[variable][value])


def main():
    file1 = sys.argv[1]  # holds file that contains variables(Instructions Page 3 (1))
    file2 = sys.argv[2]  # holds file that contains conditions(Instructions Page 3 (2))
    mode = sys.argv[3]  # holds method: 'none' - backtracking, 'fc' - forward checking(Instructions Page 3 (3))

    # checks for valid mode input
    if mode == 'none' or mode == 'fc':
        mode = mode
    # if third argument is anything other than 'none' or 'fc' throw ValueError
    else:
        raise ValueError("Third argument can only be 'none': backtracking, or 'fc': forward checking.")

    CSP(Variables(file1), Conditions(file2), mode)


main()
