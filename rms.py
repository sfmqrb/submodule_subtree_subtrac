from generate import generate_tasks

n = int(input('input n: '))

tasks = generate_tasks(n)
time = 0

end_condition = False

print(tasks)
while True:
    if end_condition:
        break
    valid_ls = [tasks[i+1] for i in range(len(tasks)) if tasks[i+1]['begin'] < time and tasks[i+1]['interval'] > 0]
    deadline_passed_ls = [x for x in valid_ls if x['interval'] > 0 and x['deadline'] <= time] 
    if len(deadline_passed_ls) > 0:
        print('not valid sequence')
        import sys
        sys.exit(1)
        
    print('---', time, '---')
    if valid_ls:
        x = valid_ls[0]
        for valid in valid_ls:
            if valid['deadline'] < x['deadline']:
                x = valid
        earliest_deadline_task = x
        
        id = x['id']
        tasks[id]['interval'] -= 1
        print('task -> ', id)
    else:
        print('task -> ', 'NAN')
        
    end_condition = [tasks[i+1] for i in range(len(tasks)) if tasks[i+1]['interval'] != 0]
    end_condition = True if len(end_condition) == 0 else False

    # print(time, tasks)
    time += 1
    
    
