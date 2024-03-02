#!/bin/bash

if [ -z "$1" ]
    then
        echo "specify ../experiment subdir"
	exit -1
fi

cd ..
DIR="$1"
mkdir experiments/"$DIR"

for subject in "algebraic_geometry" "field_theory" "order" "algebraic_topology" "geometry" "probability" "algebra" "group_theory" "representation_theory" "analysis" "information_theory" "ring_theory" "category_theory" "set_theory" "combinatorics" "library" "tactic" "computability" "linear_algebra" "topology" "control" "logic" "data" "measure_theory" "deprecated" "model_theory"
do
  echo "Evaluating: $subject" 
  python prover/evaluate.py --data-path data/leandojo_benchmark/random/  --ckpt_path ../leandojo-pl-ckpts/generator_random.ckpt --split test_"$subject" --num-cpus 24 2>&1 | tee experiments/"$DIR"/"$subject"_random_premises_without_retrieval_evalution_"$(date +"%m%d%Y_%H%M")".txt
done
