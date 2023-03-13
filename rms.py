from generate import generate_tasks_rms
import sys

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm



n = int(input('input n: '))

tasks = generate_tasks_rms(n)
print(tasks)
time = 0

upper_bound = n * (2**(1/n) - 1)

utility = 0
for id in tasks:
    utility += tasks[id]['interval'] / tasks[id]['period'] 

print('utility:', utility)
print('upper_bound:', upper_bound)

if utility > upper_bound:
    print("no valid rms implementation")
    sys.exit(1)

max_time = 1
for id in tasks:
    max_time = lcm(max_time, tasks[id]['period'])

end_time = max_time
print('max_time', max_time)

while True:
    if time > end_time:
        break
    
    period_candid = -1
    id_candid = -1
    for id in tasks:
        need = tasks[id]['time_need']   
        if need > 0:
            if period_candid == -1:
                period_candid = tasks[id]['period']   
                id_candid = id
            if period_candid > tasks[id]['period']:
                period_candid = tasks[id]['period']   
                id_candid = id
                
    if period_candid == -1:
        id_candid = "NAN"
    else:
        tasks[id_candid]['time_need'] -= 1
        
    print('task number -> ', id_candid)
    print('-----', time, '-----\n')
    # print(time, tasks)
    
    for id in tasks:
        period = tasks[id]['period']
        if time % period == 0:
            tasks[id]['time_need'] += tasks[id]['interval']

    time += 1
    
    
