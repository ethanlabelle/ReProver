import sys
from glob import glob


for filename in glob(sys.argv[1]):
    print(filename.split("/")[3].split("_random_premises")[0])
    num_total = num_correct = 0
    for line in open(filename):
        if "SearchResult" in line:
            num_total += 1
            if "Proved" in line:
                num_correct += 1

    if num_total == 0:
        print("N/A")
    else:
        print(f"{num_correct} / {num_total} = {num_correct / num_total}")
