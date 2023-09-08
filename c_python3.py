### 1 ###
def sign(n):
    if n < 0:
        return -1
    if n > 0:
        return 1
    if n == 0:
        return 0
sign(4)
q1.check()


### 2 ###
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)


to_smash(1)


def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)
q2.check()


q2.solution()


### 3 ###
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

have_umbrella = False
rain_level = 6.0
have_hood = True
is_workday = False

actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

q3.check()


### 4 ###
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number < 0 else False 
pass 

q4.check()


### 5a ###
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
   
    return not onion


def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion
    pass

q5.a.check()


### 5b ###
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return (not(ketchup)) and (not(mustard)) and (not(onion))
    pass

q5.b.check()


### 5c ###
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (((ketchup and not mustard) and onion) or ((not ketchup and mustard) and onion)) or ((ketchup and not mustard) or (not ketchup and mustard) )
    pass

q5.c.check()


### 6 ###
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    if (int(ketchup) + int(mustard) + int(onion)) == 1:
        return True
    else:
        return False
    pass

q6.check()


### 7 ###
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    
    return False


q7.simulate_one_game()


q7.simulate(n_games=50000)


def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False

q7.simulate(n_games=50000)