#!/usr/bin/bash

for i in {1..71}; do
    args+=("arg$i")
done
args+=("jvcioquhcq")

env -i 151=bqckxfhfiw /challenge/run "${args[@]}"

#环境变量用“env -i ····”，参数变量在/run后，level68，70的结合体
