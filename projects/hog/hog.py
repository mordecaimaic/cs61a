"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    total = 0
    sow_bad = False;
    while num_rolls > 0:
        score = dice()
        if score == 1:
            sow_bad = True
        else:
            total += score
        num_rolls -= 1
    if sow_bad == True:
        return 1
    else:
        return total
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    tens_digit_oppoent = opponent_score // 10 % 10
    ones_digit_player = player_score % 10
    score = 3 * abs(tens_digit_oppoent - ones_digit_player)
    if score < 1:
        return 1
    else:
        return score
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls > 0:
        return roll_dice(num_rolls, dice=dice)
    else:
        return boar_brawl(player_score, opponent_score)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    num, count = 1, 1
    while num < n:
        if n % num == 0:
            count += 1
        num += 1
    return count
    # END PROBLEM 4

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # Sus Fuss 是一个游戏规则，当当前选手的分数是有3个或者4个因数(包括1和该数字本身)的时候，就会跳转到下一个prime(质数)
    # sus_points()可以根据sus fuss规则返回一个正确的分数
    if num_factors(score) == 3 or num_factors(score) == 4:
        new_score = score + 1
        while is_prime(new_score) == False:
            new_score += 1
        return new_score
    else:
        return score

    # END PROBLEM 4

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # sus_update()是一个分数更新函数，分别结合了boar_brawl规则以及sus_points的规则
    # 当投掷次数大于0的时候，更新2次分数。分别根据普通掷骰子更新roll_dice()再根据sus_points规则进行更新
    # 当投掷次数等于0的时候，更新2次分数。分别根据boar_brawl()规则更新，然后再更具sus_points规则进行更新
    if num_rolls > 0:
        player_score += roll_dice(num_rolls, dice=dice)
        player_score = sus_points(player_score)
        return player_score
    else:
        player_score += boar_brawl(player_score, opponent_score)
        player_score = sus_points(player_score)
        return player_score
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            score0 = update(num_rolls, score0, score1, dice)
        elif who == 1:
            num_rolls = strategy1(score1,score0)
            score1 = update(num_rolls, score1, score0, dice)
        who = 1 - who
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def strategy(score, oppoenet_score):
        return n
    return strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    # 判断这个输入输入的策略是否为always策略（也就是通过遍历骰子🎲的所有组合，判断输入的策略是否会根据用户的不同比分而有所不同）
    score, opponent_score = 0, 0
    roll_nums = strategy(score, opponent_score)
    while score < goal:
        opponent_score = 0
        while opponent_score < goal:
            new_roll_nums = strategy(score, opponent_score)
            if not new_roll_nums == roll_nums:
                return False
            else:
                roll_nums = new_roll_nums
            opponent_score += 1
        score += 1
    return True


    # END PROBLEM 7


def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    #笔记
    """ averaged_dice = make_averaged(roll_dice, 40)。表示制造一个函数averaged_dice()，调用make_average可以控制函数的调用次数，用来统计这40次的roll_dice()的平均返回值
    假设调用函数averaged_dice(3),将会调用roll_dice 40次，每一次都是都是投掷3个骰子，并且返回这40次的平均值。
    函数的输入只和roll_dice本身有关,和averaged没有任何关系。
    所以make_averaged在定义平均函数的时候,应该是采取*agrs,表示任意数量的参数。因为即使在更换了输入函数之后,（详细可查看cs61a 2023 fall里面的课程解释）
    我们需要调查的函数的输入参数,和我们本身制造调查平均数函数之间并没有关系.
    因此需要采用agrs来表示
    -- 另外需要注意的点,思考一下：如果在上面的例程中,使用averaged_dice(2,dice)的话,也就是代表每一轮扔2个
    -- 第一轮扔的是6分,但是第二轮扔的只有1分,因为有Sow Sad规则,如果在一轮中扔了n次骰子,如果其中有一次是点数为1的骰子🎲的话,那么roll_dice()函数返回为1
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def average(*args):
        total , count = 0, samples_count
        while count > 0:
            total += original_function(*args)
            count -= 1
        return total / samples_count
    return average 
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, samples_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of SAMPLES_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    #笔记
    """ max_scoring_num_rolls(),这个函数是用来求出一个最佳的骰子(用最少的投掷次数，达到分数最大化）
        这个函数用来返回玩家每回合应该**最少**掷多少次骰子(可以从1-10次)）？以此来达到骰子点数的最大化。
        假设骰子是由于make_test_dice(1, 6)构造的。那么假设掷骰子计数1000轮,每轮扔多少个骰子会达到总平均数的最大值呢？
        -- 答案很明显是1个,因为如果每轮超过一个的话,平局下来的话每一轮都只有1分了(由于sow bad规则),这显然不符合我们最开始的原则:扔1000轮,每一轮平均点数最大化的原则,且每一轮扔的次数尽量少
        -- 如果每轮扔一个骰子的话,我们至少还可以有(1+6) / 2 = 3.5分
        -- 思考一个新的问题：如果假设 dice = make_test(3)的话, 那么每一轮多少个掷骰子,可以保证利益最大化呢
        -- 答案很很明显是:是每轮掷10次,因为这样子我们可以每轮获得30分(因为这个骰子🎲里面只有3,没有1,不需要担心收到sow bad的限制)
        -- 根据以上的思路,我们就可以实现max_scoring_num_rolls()函数了
        -- 要利用到我们上面所实现的make_averaged()以及roll_dice()这两个函数
    """
    max_score, best_nums, roll_nums = 0, 0, 1
    # 遍历所有可能取得分数最大化的骰子次数，roll_nums从1-10次
    while roll_nums <= 10:
        average_score = make_averaged(roll_dice, samples_count)
        current_averge_score = average_score(roll_nums, dice)
        if current_averge_score > max_score:
           max_score = current_averge_score
           best_nums = roll_nums
        roll_nums += 1
    return best_nums

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    # 这个函数是针对Boar Brawl规则最优化的策略，num_rolls指的是原来打算投掷的次数。
    # 就是当投掷🎲0次的时候，若当返回的分数大于threshold(阈值)的话，就返回0次（也就是更改原来打算投掷的次数）
    # 若当返回的分数小于阈值的时候，也就是是Boar Brawl没有达到预期的时候，我们就直接返回num_rolls(按照原来打算投的次数)
    # 这个是目前胜利最高的策略可以达到66%-67%，和其他单一always的策略相比较
    # 这个策略可以感觉用在股票市场里面，同时也可以被理解为见好就收策略，threshold(阈值)的设置要恰当合理，不然胜率会下降（默认是11）
    if boar_brawl(score, opponent_score) >= threshold:
        return 0
    else:
        return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    # sus_strategy()考虑到2个规则，并且根据阈值将分数评估为最大化
    # boar规则和sus规则
    # 
    increase_score = sus_update(0, score, opponent_score) - score
    if increase_score >= threshold:
        return 0
    else:
        return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    最终函数(风险最小化):1. 当分数快要赢的时候(例如90多分的时候，100分胜利)，不要投掷太多次数的点数(检测投掷0，1，2是否能够获胜)
                      2. 当投掷0个大于投掷6个的平均分数的时候，始终投掷出0个

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    roll_nums = 1
    # make_average()，里面必须手动修改测试平均数的值(默认是1000次)，不然运行的时间过久，会导致ok函数超时
    average = make_averaged(roll_dice, 100)
    if sus_update(0, score, opponent_score) > GOAL:
        return 0
    else:
        while roll_nums <= 2:
            if score + average(roll_nums) > GOAL:
                return roll_nums
            else:
                roll_nums +=1
        
    if boar_brawl(score, opponent_score) > average(6):
        return 0
    else:
        return 6  
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()