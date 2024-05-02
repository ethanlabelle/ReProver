with open('result_dicts.txt', 'r') as f:
    lines = f.readlines()
    dicts = []
    for i in range(len(lines)):
        try:
            # print(eval(lines[i]))
            dicts.append(eval(lines[i]))
        except:
            pass
# print(dicts)
print(dicts[0]) # num theorems searched
print(dicts[1]) # num theorems searched
print(dicts[2]) # num theorems proved
print(dicts[3]) # num search attempts
# print(dicts[4]) # num trials
# print(dicts[5]) # num solves
# print(dicts[6]) # test set
# dicts
n_theorems = dicts[0] # num theorems searched
# dicts[1] # num theorems searched ^^ same as above
n_solved = dicts[2] # num theorems proved
n_attempts = dicts[3] # num search attempts
trials_dict = dicts[4] # num trials
solves_dict = dicts[5] # num solves
problem_set = dicts[6] # test set
problem_set = sorted(list(problem_set))
# print(sorted(list(problem_set)))
solve_rates = {}
for problem in problem_set:
    # print(f'{problem}: {trials_dict[problem]}')
    solves = 0
    if problem in solves_dict:
        solves = solves_dict[problem]
    solve_rates[problem] = solves/trials_dict[problem]
    # print(f'{problem in solves_dict}')

problem_set = sorted(list(problem_set), key=lambda x: solve_rates[x])
for problem in problem_set:
    attempts = trials_dict[problem]
    if problem not in solves_dict:
        solves = 0
    else:
        solves = solves_dict[problem]
    print(f'{problem}: {solve_rates[problem]} ({solves}/{attempts})')

print(f'Overall solve rate: {len(solves_dict)/len(problem_set)}')
