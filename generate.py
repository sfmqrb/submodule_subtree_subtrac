

import random


def generate_tasks(n: int,
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
            'priority': priorities[i],
            'interval': intervals[i]
        }
        for i in range(len(id))
    }


if __name__ == '__main__':
    print(generate_tasks(10))
