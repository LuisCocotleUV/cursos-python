### 1 ###
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
        

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    bool_values = []
    if len(nums) > 0:
        for num in nums:
            if num % 7 == 0:
                bool_values.append(1)
            else:
                bool_values.append(0)
            print(bool_values)
    else:
        return False
    
    if sum(bool_values) > 0:
                return True
    else: 
        return False

q1.check()


### 2 ###
[1, 2, 3, 4] > 2


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    bool_list = []
    for i in range(len(L)):
        if L[i] > thresh:
            bool_list.append(True)
        else:
            bool_list.append(False)  
    
    return(bool_list)
    
    pass

q2.check()


### 3 ###
def menu_is_boring(meals):
    
    return any([meals[i] == meals[i+1] for i in range(0, len(meals)-1)])
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """

q3.check()


### 4 ###
play_slot_machine()


def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5k
    """
    n_runs_sum =[]
    for i in range(n_runs):
        n_runs_sum.append(play_slot_machine()-1) 
    return sum(n_runs_sum)/len(n_runs_sum) 


q4.solution()