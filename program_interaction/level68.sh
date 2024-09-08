#!/bin/bash

# 构建一个参数列表，确保第 153 个参数为 epegyanlhb
args=()
for i in {1..152}; do
    args+=("arg$i")  # 填充前 152 个参数
done
args+=("epegyanlhb")  # 第 153 个参数

# 运行挑战程序，传递所有参数
/challenge/run "${args[@]}"
