#FATIMA FAHEEM RAADIA 

import math
from functools import reduce
from typing import List, Tuple

class Task:
    def __init__(self, C: int, D: int, T: int):
        self.C = C  # Worst-case execution time
        self.D = D  # Relative deadline
        self.T = T  # Period (minimum inter-arrival time)

def dbf(t: int, task: Task) -> int:
    if t < task.D:
        return 0
    else:
        return (math.floor((t - task.D) / task.T) + 1) * task.C

def edf_schedulability(tasks: List[Task]) -> bool:
    """
    Check EDF schedulability for a set of sporadic tasks.
    
    :param tasks: List of Task objects representing the task set.
    :return: True if the task set is schedulable under EDF, False otherwise.
    """
    if not tasks:
        return True

    # Calculate the least common multiple (LCM) of the periods
    periods = [task.T for task in tasks]
    lcm_period = lcm_multiple(periods)
    
    # Check the DBF sum for each time interval t from 0 to lcm_period
    for t in range(1, lcm_period + 1):
        dbf_sum = sum(dbf(t, task) for task in tasks)
        if dbf_sum > t:
            return False
    return True

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def lcm_multiple(numbers: List[int]) -> int:
    return reduce(lcm, numbers)

# Example usage:
tasks = [
    Task(2, 5, 10),  # Task 1 (Ci, Di, Ti)
    Task(1, 3, 5),   # Task 2
    Task(2, 7, 14)   # Task 3
]

schedulable = edf_schedulability(tasks)
print("Schedulable under EDF:", schedulable)
