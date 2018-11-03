#!/bin/bash

printf "Please enter the number of tests repetitions you want to do:\n> "
read REP

# DEFAULTS:
# -a 50
# -e 0.1
# -i 50
# -k 1
# python3 longest_path.py -a 50 -e 0.1 -i 50 -k 1 input/datasets/graph1.txt

I=1
while [ $I -le $REP ]
do
    printf "Executing iteration %d...\n" "$I"

    # Ant population changes
    printf "Executing ant population changes for iteration %d...\n" "$I"

    printf "Graph1\n"
    mkdir -p output/$I/graph1/ant
    python3 longest_path.py -a 10 input/datasets/graph1.txt > output/$I/graph1/ant/output1.txt &
    python3 longest_path.py -a 20 input/datasets/graph1.txt > output/$I/graph1/ant/output2.txt &
    python3 longest_path.py -a 50 input/datasets/graph1.txt > output/$I/graph1/ant/output3.txt &
    python3 longest_path.py -a 75 input/datasets/graph1.txt > output/$I/graph1/ant/output4.txt &
    python3 longest_path.py -a 100 input/datasets/graph1.txt > output/$I/graph1/ant/output5.txt

    printf "Graph2\n"
    mkdir -p output/$I/graph2/ant
    python3 longest_path.py -a 10 input/datasets/graph2.txt > output/$I/graph2/ant/output1.txt &
    python3 longest_path.py -a 20 input/datasets/graph2.txt > output/$I/graph2/ant/output2.txt &
    python3 longest_path.py -a 50 input/datasets/graph2.txt > output/$I/graph2/ant/output3.txt &
    python3 longest_path.py -a 75 input/datasets/graph2.txt > output/$I/graph2/ant/output4.txt &
    python3 longest_path.py -a 100 input/datasets/graph2.txt > output/$I/graph2/ant/output5.txt

    printf "Graph3\n"
    mkdir -p output/$I/graph3/ant
    python3 longest_path.py -a 10 input/datasets/graph3.txt > output/$I/graph3/ant/output1.txt &
    python3 longest_path.py -a 20 input/datasets/graph3.txt > output/$I/graph3/ant/output2.txt &
    python3 longest_path.py -a 50 input/datasets/graph3.txt > output/$I/graph3/ant/output3.txt &
    python3 longest_path.py -a 75 input/datasets/graph3.txt > output/$I/graph3/ant/output4.txt &
    python3 longest_path.py -a 100 input/datasets/graph3.txt > output/$I/graph3/ant/output5.txt

    # Evaporation rate changes
    printf "Executing evaporation rate changes for iteration %d...\n" "$I"

    printf "Graph1\n"
    mkdir -p output/$I/graph1/evaporation
    python3 longest_path.py -e 0.01 input/datasets/graph1.txt > output/$I/graph1/evaporation/output1.txt &
    python3 longest_path.py -e 0.05 input/datasets/graph1.txt > output/$I/graph1/evaporation/output2.txt &
    python3 longest_path.py -e 0.1 input/datasets/graph1.txt > output/$I/graph1/evaporation/output3.txt &
    python3 longest_path.py -e 0.5 input/datasets/graph1.txt > output/$I/graph1/evaporation/output4.txt &
    python3 longest_path.py -e 0.8 input/datasets/graph1.txt > output/$I/graph1/evaporation/output5.txt

    printf "Graph2\n"
    mkdir -p output/$I/graph2/evaporation
    python3 longest_path.py -e 0.01 input/datasets/graph2.txt > output/$I/graph2/evaporation/output1.txt &
    python3 longest_path.py -e 0.05 input/datasets/graph2.txt > output/$I/graph2/evaporation/output2.txt &
    python3 longest_path.py -e 0.1 input/datasets/graph2.txt > output/$I/graph2/evaporation/output3.txt &
    python3 longest_path.py -e 0.5 input/datasets/graph2.txt > output/$I/graph2/evaporation/output4.txt &
    python3 longest_path.py -e 0.8 input/datasets/graph2.txt > output/$I/graph2/evaporation/output5.txt

    printf "Graph3\n"
    mkdir -p output/$I/graph3/evaporation
    python3 longest_path.py -a 10 -e 0.01 input/datasets/graph3.txt > output/$I/graph3/evaporation/output1.txt &
    python3 longest_path.py -a 20 -e 0.05 input/datasets/graph3.txt > output/$I/graph3/evaporation/output2.txt &
    python3 longest_path.py -a 50 -e 0.1 input/datasets/graph3.txt > output/$I/graph3/evaporation/output3.txt &
    python3 longest_path.py -e 0.5 input/datasets/graph3.txt > output/$I/graph3/evaporation/output4.txt &
    python3 longest_path.py -e 0.8 input/datasets/graph3.txt > output/$I/graph3/evaporation/output5.txt

    # k changes
    printf "Executing k changes for iteration %d...\n" "$I"

    printf "Graph1\n"
    mkdir -p output/$I/graph1/k
    python3 longest_path.py -k 1 input/datasets/graph1.txt > output/$I/graph1/k/output1.txt &
    python3 longest_path.py -k 10 input/datasets/graph1.txt > output/$I/graph1/k/output2.txt &
    python3 longest_path.py -k 20 input/datasets/graph1.txt > output/$I/graph1/k/output3.txt &
    python3 longest_path.py -k 40 input/datasets/graph1.txt > output/$I/graph1/k/output4.txt

    printf "Graph2\n"
    mkdir -p output/$I/graph2/k
    python3 longest_path.py -k 1 input/datasets/graph2.txt > output/$I/graph2/k/output1.txt &
    python3 longest_path.py -k 10 input/datasets/graph2.txt > output/$I/graph2/k/output2.txt &
    python3 longest_path.py -k 20 input/datasets/graph2.txt > output/$I/graph2/k/output3.txt &
    python3 longest_path.py -k 40 input/datasets/graph2.txt > output/$I/graph2/k/output4.txt

    printf "Graph3\n"
    mkdir -p output/$I/graph3/k
    python3 longest_path.py -k 1 input/datasets/graph3.txt > output/$I/graph3/k/output1.txt &
    python3 longest_path.py -k 10 input/datasets/graph3.txt > output/$I/graph3/k/output2.txt &
    python3 longest_path.py -k 20 input/datasets/graph3.txt > output/$I/graph3/k/output3.txt &
    python3 longest_path.py -k 40 input/datasets/graph3.txt > output/$I/graph3/k/output4.txt 

    # Iteration changes
    printf "Executing iteration changes for iteration %d...\n" "$I"

    printf "Graph1\n"
    mkdir -p output/$I/graph1/iteration
    python3 longest_path.py -i 10 input/datasets/graph1.txt > output/$I/graph1/iteration/output1.txt &
    python3 longest_path.py -i 20 input/datasets/graph1.txt > output/$I/graph1/iteration/output2.txt &
    python3 longest_path.py -i 50 input/datasets/graph1.txt > output/$I/graph1/iteration/output3.txt &
    python3 longest_path.py -i 75 input/datasets/graph1.txt > output/$I/graph1/iteration/output4.txt &
    python3 longest_path.py -i 100 input/datasets/graph1.txt > output/$I/graph1/iteration/output5.txt

    printf "Graph2\n"
    mkdir -p output/$I/graph2/iteration
    python3 longest_path.py -i 10 input/datasets/graph2.txt > output/$I/graph2/iteration/output1.txt &
    python3 longest_path.py -i 20 input/datasets/graph2.txt > output/$I/graph2/iteration/output2.txt &
    python3 longest_path.py -i 50 input/datasets/graph2.txt > output/$I/graph2/iteration/output3.txt &
    python3 longest_path.py -i 75 input/datasets/graph2.txt > output/$I/graph2/iteration/output4.txt &
    python3 longest_path.py -i 100 input/datasets/graph2.txt > output/$I/graph2/iteration/output5.txt

    printf "Graph3\n"
    mkdir -p output/$I/graph3/iteration
    python3 longest_path.py -i 10 input/datasets/graph3.txt > output/$I/graph3/iteration/output1.txt &
    python3 longest_path.py -i 20 input/datasets/graph3.txt > output/$I/graph3/iteration/output2.txt &
    python3 longest_path.py -i 50 input/datasets/graph3.txt > output/$I/graph3/iteration/output3.txt &
    python3 longest_path.py -i 75 input/datasets/graph3.txt > output/$I/graph3/iteration/output4.txt &
    python3 longest_path.py -i 100 input/datasets/graph3.txt > output/$I/graph3/iteration/output5.txt

    (( I++ ))
done

printf "Done executing %d tests repetitions\n" "$REP"
