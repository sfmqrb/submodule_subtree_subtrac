

import random


def generate_tasks_edf(n: int,
                   MAX_BEGIN=2,
                   MAX_INTERVAL=10,
                   MAX_PRIORITY=10,):
    import numpy as np
    id = [i for i in range(1, n+1)]

    begins = list(np.random.randint(1, MAX_BEGIN, size=n+1))
    for idx, _ in enumerate(begins):
        if idx == 0:
            continue
        begins[idx] += begins[idx-1]
    intervals = list(np.random.randint(1, MAX_INTERVAL, size=n))
    deadlines = [0] * len(begins)
    for idx, _ in enumerate(intervals):
        deadlines[idx] = begins[idx] + \
            int(3*random.random() + 2) * intervals[idx]
    priorities = list(np.random.randint(1, MAX_PRIORITY, size=n))

    return {
        id[i]: {
            'id': id[i],
            'begin': begins[i],
            'deadline': deadlines[i],
            'interval': intervals[i]
        }
        for i in range(len(id))
    }


def generate_tasks_rms(n: int,
                   MAX_PERIOD=12):
    
    import numpy as np
    id = [i for i in range(1, n+1)]

    Periods = []
    for _ in range(n):
        while True:
            x = random.randint(MAX_PERIOD // 3, MAX_PERIOD)
            if x not in Periods:
                Periods.append(x)
                break
    Intervals = [0] * len(Periods)
    
    for idx, _ in enumerate(Periods):
        Intervals[idx] = int((Periods[idx] // 3)*random.random()) + 1 
    
    return {
        id[i]: {
            'id': id[i],
            'period': Periods[i],
            'interval': Intervals[i],
            'time_need': 0
        }
        for i in range(len(id))
    }


if __name__ == '__main__':
    print(generate_tasks_edf(3))
    print(generate_tasks_rms(3))
