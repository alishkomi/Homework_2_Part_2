import sys

# get variables and their domains and store them in a dictionary
# returns a dictionary with key as the variable and value as the domain
def Variables(file):
    variables = {} # key: variable(str), value: domain(ints)
    with open(file) as f:
        for line in f:
            objects = line.split() # turn line into a list
            current_var = str(objects[0])[0] # char letter (A, B, C, or D, ...)
            values = objects[1:] # store domain of current variable in a list

            for i in range(0, len(values)): # convert values to int
                values[i] = int(values[i])

            if current_var in variables: # check if current variable in list
                variables[current_var].append(values) # if so, add values to key(current node)
            else:
                variables[current_var] = values # otherwise create a key with values
    return variables


# get conditions from a file
# returns a dictionary with variables as keys and conditions as values stored in a list
def Conditions(file):
    conditions = {} # key: variable(str), value: conditions(str)
    with open(file) as f:
        for line in f: # for each condition in file
            var1 = line[0] # get first variable
            var2 = line[4] # get second variable
            if var1 not in conditions: # if variable not in dictionary
                conditions[var1] = line.rstrip().rsplit("\n") # create variable and store the whole condition
            else:
                conditions[var1].append(line.rstrip().rsplit("\n")[0]) # otherwise append to list
            if var2 not in conditions: # do same to second variable
                conditions[var2] = line.rstrip().rsplit("\n")
            else:
                conditions[var2].append(line.rstrip().rsplit("\n")[0])
    return conditions


def CSP(mode):
    print("CSP Search")



def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    mode = sys.argv[3]

    if mode == 'none':
        mode = sys.argv[3]
    elif mode == 'fc':
        mode = sys.argv[3]
    else:
        raise ValueError("Third argument can only be 'none': backtracking, or 'fc': forward checking.")

    print("Variables: ", Variables(file1))
    print("Conditions: ", Conditions(file2))
    print("Mode: ", mode)

main()
