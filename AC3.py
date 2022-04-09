# reduces domain by checking arc constistency -
# based on AC-3 pseudocode from AIAMA - Russell, Norvig
#       
#############################################
import queue

def AC3(csp)->bool:
    q = queue.Queue()
    for arc in csp.constraints:
        q.put(arc)

    while not q.empty():
        X,Y = q.get()

        if revise(csp, X,Y):
            # check if domain is empty
            if len(csp.domain[X])==0:
                return False

            for nb in csp.neighbors[X]:
                if nb!=Y:
                    q.put((nb, X))
            
    return True


def revise(csp, var1,var2)->bool:
    boo = False 
    for dom in csp.domain[var1]:
        if not isConsistent(csp, var1, var2, dom):
            csp.domain[var1] = csp.domain[var1].replace(dom,'')
            boo = True 
    return boo


def isConsistent(csp,var1,var2,val)->bool:
    # for all value in var2 domain
    # check that var2 and var1 is connected by arc
    # and that var2 domains are not the same as var1 domains
    for dom in csp.domain[var2]:
        if var2 in csp.neighbors[var1] and dom!=val:
            return True 

    return False 