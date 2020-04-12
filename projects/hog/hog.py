from dice import six_sided, four_sided, make_test_dice
from operator import add, sub
from doctest import testmod

GOAL_SCORE = 100

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'

    def iter(i, sum):
        if i == num_rolls:
            return sum
        outcome = dice()
        if outcome == 1:
            return 1
        else:
            return iter(i + 1, sum + outcome)
    
    return iter(0, 0)

def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.

    >>> print(free_bacon(4))
    3
    >>> print(free_bacon(1))
    2
    >>> print(free_bacon(20))
    9
    >>> print(free_bacon(45))
    13
    """
    assert score < 100

    def extract_last(num):
        if num < 10: 
            return num
        return num % 10

    def remove_last(num):
        return num // 10

    def iter(n, sum, operator):
        if n < 10:
            return 1 + abs(operator(sum, n))
        if operator == add:
            return iter(remove_last(n), operator(sum, extract_last(n)), sub)
        else:
            return iter(remove_last(n), operator(sum, extract_last(n)), add)

    score_cubed = score * score * score
    
    return iter(score_cubed, 0, sub)

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'

    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)

def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped

    >>> print(is_swap(2, 4))
    False
    >>> print(is_swap(11, 1))
    False
    >>> print(is_swap(1, 0))
    True
    >>> print(is_swap(23, 4))
    True
    """
    def extract_last(num):
        if num < 10: 
            return num
        return num % 10

    def remove_last(num):
        if num < 10:
            return num
        return num // 10

    def extract_first(num):
        if num < 10:
            return num
        return extract_first(remove_last(num))

    excitement = pow(3, player_score + opponent_score)
    
    if extract_first(excitement) == extract_last(excitement):
        return True
    else:
        return False

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)


    while score0 < goal and score1 < goal:
        if who == 0:
            score0 += take_turn(strategy0(score0, score1), score1)
            who = 1
        else:
            score1 += take_turn(strategy1(score1, score0), score0)
            who = 0
        if is_swap(score0, score1):
            score0, score1 = score1, score0
    
    return score0, score1

def sayScore(score0, score1):
    print("Score0:", score0, " Score1:", score1)

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    if free_bacon(opponent_score) >= 8:
        return 0
    else:
        return num_rolls

def swap_strategy(score, opponent_score, margin=8, num_rolls=6):
    def beneficial_swap(score, opponent_score):
        if score < opponent_score:
            return True
        return False

    if beneficial_swap(score, opponent_score):
        return 0

    if free_bacon(opponent_score) >= margin and not beneficial_swap(opponent_score, free_bacon(opponent_score) + score):
        return 0
    
    return num_rolls
    
def get_winner(strategy0, strategy1):
    score0, score1 = play(strategy0, strategy1)
    if score0 < score1:
        return 1
    else:
        return 0

def run_experiments(strategy0, strategy1, num_iter=10000):
    i = 1
    wins0 = 0
    wins1 = 0

    while i < num_iter:
        winner = get_winner(strategy0, strategy1)
        if winner == 0:
            wins0 += 1
        elif winner == 1:
            wins1 += 1
        i = i + 1

    wr0 = wins0 * 100.0 / num_iter
    wr1 = wins1 * 100.0 / num_iter

    print("strategy0 winrate: " , wr0, "% strategy1 winrate: ", wr1, "%")


run_experiments(swap_strategy, always_roll(6))