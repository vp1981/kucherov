#!/usr/bin/bash

export LC_NUMERIC=en_US.UTF-8

a=-3
b=7
N=50
step=$(echo 1/${N}| bc -l)

fdata="data-full.dat"

for ex in $(seq ${a} ${step} ${b})
do
  ./m4-tol sun.lua -c "E=math.exp(${ex}*math.log(10))" survprob.lua >> "${fdata}"
done

sed '/^#/d' "${fdata}" > "${fdata/-full/}"

