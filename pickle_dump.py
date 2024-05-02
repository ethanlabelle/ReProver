import glob
import pickle

pickle_files = glob.glob('./pickle_jar/*.pickle')

theorems = set()
num_results = 0
num_attempts = {}
num_proves = {}

for file_name in pickle_files:
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
        for elm in data:
            print(elm)
            if elm:
                num_results += 1
                # print(elm.theorem)
                # print(elm.theorem.__dir__())
                # print(elm.theorem.full_name)
                # print(elm.status)
                if "PROVED" in elm.status.__repr__():
                    if elm.theorem.full_name in num_proves:
                        num_proves[elm.theorem.full_name] += 1
                    else:
                        num_proves[elm.theorem.full_name] = 1

                theorems.add(elm.theorem.full_name)
                if elm.theorem.full_name in num_attempts:
                    num_attempts[elm.theorem.full_name] += 1
                else:
                    num_attempts[elm.theorem.full_name] = 1

print(len(theorems))
print(len(num_attempts))
print(len(num_proves))
print(num_results)
print(num_attempts)
print(num_proves)
print(theorems)
