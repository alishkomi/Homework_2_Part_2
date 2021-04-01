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
                values[i] = int(values[i].strip())

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


# function that selects the most constrained variable
# this can be implemented easier but to understand the output, additional parameters are added
def chooseVariable(variables, conditions):
    order = []
    variable = {'Variable': ['NA', 999, [], 999, []]}  # [variable name, possible values, constraints]
    for key in variables:
        if len(variables[key]) < variable['Variable'][1]:  # find variable with fewest legal values
            variable['Variable'] = [key, len(variables[key]), variables[key], len(conditions[key]), conditions[key]]


        elif len(variables[key]) == variable['Variable'][1]:  # if there is a tie

            if len(conditions[key]) > len(variable['Variable'][2]):  # find variable with most constraints
                variable['Variable'] = [key, len(variables[key]), variables[key], len(conditions[key]), conditions[key]]

            elif len(conditions[key]) == variable['Variable'][3]:  # break tie alphabetically

                if key < variable['Variable'][0]:
                    variable['Variable'] == [key, len(variables[key]), variables[key], len(conditions[key]),
                                             conditions[key]]
                else:
                    variable['Variable'] == variable['Variable']
    order.append(variable['Variable'][0])
    return variable['Variable'][
        0]  # returns a dictionary: {'Variable': ['Variable Name'(str), Num. of legal values(int), [Legal Values](list), Num. of Conditions(int), ]Conditions](list)}
    # return listofVar = [F,E,A,B,C,D]


1
pick
a
variable
2
pick
a
value
3
update
domains
list[F, E, A, B, C, D]

4
next
variable(updated(variables(domains)), conditions())
5
pick
a
variable
...


# example: choose least constraining value for F. chooseValue(F, variables, conditions)
def chooseValue(varName, variables, conditions):
    legalValue = {}

    for condition in conditions[varName]:  # ['B > F', 'F > D', 'F = A'] 'var1 operation var2'
        var1 = condition[0]  # conditions['D'] = ['A > D', 'D < E'] A = 1,2,3 D = 1,2,3,4,5 E = 1,2,3,4,5
        var2 = condition[4]  # B: 1,2,3,4,5 F:1,2 D: 1,2,3,4,5
        operation = condition[2]
        var1domain = variables[var1]
        var2domain = variables[var2]

        if operation == '>':  # if condition is var 1 > var 2
            if var1 == varName:  # if var1 is the variable we are finding the number for
                var2domainSize = 0
                for value in var1domain:
                    var2domainSizeCurrent = len([x for x in var2domain if x < value])
                    if var2domainSizeCurrent > var2domainSize:
                        var2domainSize = var2domainSizeCurrent
                        legalValue[value] = var2domainSize
            elif var2 == varName:  # B > F;  B: 1 2 3 4 5   F: 1 2
                var1domainSize = 0
                for value in var2domain:
                    var1domainSizeCurrent = len([x for x in var1domain if x < value])
                    if var1domainSizeCurrent > var1domainSize:
                        var1domainSize = var1domainSizeCurrent
                        legalValue[value] = var1domainSize
            else:
                print("Error")
            print("> operation", legalValue)

        elif operation == '=':
            if var1 == varName:
                var2domainSize = 0
                for value in var1domain:
                    var2domainSizeCurrent = len([x for x in var2domain if x == value])
                    if var2domainSizeCurrent > var2domainSize:
                        var2domainSize = var2domainSizeCurrent
                        legalValue[value] = var2domainSize

            elif var2 == varName:  # B > F;  B: 1 2 3 4 5   F: 1 2
                var1domainSize = 0
            for value in var2domain:
                var1domainSizeCurrent = len([x for x in var1domain if x == value])
                if var1domainSizeCurrent > var1domainSize:
                    var1domainSize = var1domainSizeCurrent
                    legalValue[value] = var1domainSize
            else:
                print("Error")
            print("= operation", legalValue)

        elif condition[2] == '<':
            if var1 == varName:
                var2domainSize = 0
                for value in var1domain:
                    var2domainSizeCurrent = len([x for x in var2domain if x > value])
                    if var2domainSizeCurrent > var2domainSize:
                        var2domainSize = var2domainSizeCurrent
                        legalValue[value] = var2domainSize

            elif var2 == varName:  # B > F;  B: 1 2 3 4 5   F: 1 2
                var1domainSize = 0
                for value in var2domain:
                    var1domainSizeCurrent = len([x for x in var1domain if x < value])
                    if var1domainSizeCurrent > var1domainSize:
                        var1domainSize = var1domainSizeCurrent
                        legalValue[value] = var1domainSize
            else:
                print("Error")
            print("< operation", legalValue)
        else:
            print("Error")


def CSP(variables, conditions, mode):
    print("Variables: ", variables)  # for debug purposes
    print("Conditions: ", conditions)  # for debug purposes
    print("Mode: ", mode)  # for debug purposes
    # sorted_variables = sorted(conditions)


def fc(order, variables, conditions):
    for var in order:


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
    most_constrained_variable = chooseVariable(Variables(file1), Conditions(file2))
    print("Most constrained variable: ", most_constrained_variable['Variable'][0])


main()
