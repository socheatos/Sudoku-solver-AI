############################################
# based on backtracking search pseudocode 
# from AIAMA &AIMA GitHub- Russell, Norvig
# inferences inspired by:
#https://steven.codes/blog/constraint-satisfaction-with-sudoku/
#############################################
from copy import deepcopy

def BacktrackingSearch(csp):
    return Backtrack(csp, {})

def Backtrack(csp, assignment):
    if isComplete(assignment):
        return assignment

    variable = minRemainingValue(csp, assignment)

    for value in csp.domain[variable]:
        if isConsistent(csp, assignment,variable, value):
            assignment[variable]=value
            domain = deepcopy(csp.domain)
            inf = inferences(csp, assignment,variable,value)
            if inf != 'FAILURE':
                result = Backtrack(csp, assignment)
                if result != 'FAILURE':
                    return result
                csp.domain.update(domain)
            del assignment[variable]
    return 'FAILURE'

###############################################
def isComplete(assignment):
    return len(set(assignment.keys()))==81

def minRemainingValue(csp,assignment):
    unassigned_var = None 
    Bestval=10
    for var in csp.variables: 
        # checks that var is really unassigned
        if var not in assignment.keys(): 
            if len(csp.domain[var]) < Bestval:
                unassigned_var = var
                Bestval = len(csp.domain[var] )
    return unassigned_var

def isConsistent(csp, assignment, var, val):
    # checks if the assignment's neighboar is already assigned
    # with that same value 
    for nb in csp.neighbors[var]:
        if nb in assignment.keys() and assignment[nb]==val:
            return False
    return True 

def inferences(csp, assignment,var,val):
    inf = {}
    for nb in csp.neighbors[var]:
        if nb not in assignment and val in csp.domain[nb]:
            csp.domain[nb]=csp.domain[nb].replace(val,'')
        if len(csp.domain[nb])==0:
            return 'FAILURE'
    return inf



            