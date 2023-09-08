### 1 ###
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L)>=2:
        return L[1]
    else:
        return None

q1.check()


### 2 ###
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]
    pass

q2.check()


### 3 ###
def purple_shell(racers):
    a = racers[0]
    b = racers[-1]
    c = a
    a = b
    b = c
    racers[0] = a
    racers[-1] = b
    print(racers)

q3.check()


### 4 ###
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

lengths = [3, 2, 0, 2]

q4.check()


### 5 ###
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    d = (len(arrivals)/2)
    e = arrivals.index(name)
   
    if e < d or e == (len(arrivals)-1):
        return False
    else:
        return True

q5.check()