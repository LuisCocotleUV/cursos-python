### 1 ###   
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    
    x = round(num, 2)
    return(x)
    pass
round_to_two_places(3.14159)

q1.check()


### 2 ###
round(52.23456,-1)


q2.solution()


### 3 ###     
def to_smash(total_candies, n = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n

q3.check()


### 4 (Opcional) ###
round_to_two_places(9.9999)


x = -10
y = 5
smallest_abs = min(abs(x),abs(y))
print(smallest_abs)


def f(x):
    y = abs(x)
    return y

print(f(5))