#!/bin/bash


cd ..
for subject in "field_theory"
do
  echo "Evaluating: $subject" 
  python prover/evaluate.py --data-path data/leandojo_benchmark/random/  --ckpt_path ../leandojo-pl-ckpts/generator_random.ckpt --split test_"$subject" --with-gpus --num-cpus 1
done
