#!/usr/bin/bash

export LC_NUMERIC=en_US.UTF-8

fk=(0.9 0.95 1.0 1.05 1.1)
model="sun"
fdata="/tmp/data-${model}.tmp"
E="1.0"
mod="in"
mang="s12"
Ep1=-3
Ep2=7
N=50

case $1 in
  "s12")
    mang="s12"
    ;;
  "s13")
    mang="s13"
    ;;
  *)
    echo "using default angle ${mang}"
    ;;
esac

datf="/tmp/${model}_${mod}_${mang}_E=${E}.dat"
echo -n "" > ${datf}
i=10
for ex in ${fk[@]}
do
  ./m4-tol ${model}.lua -c "d=(${Ep2}-${Ep1})/(${N}-1);E=math.exp((${Ep1}+${i}*d)*math.log(10));${mang}=${ex}*${mang}" survprob.lua > "${fdata}"
  dat=($(grep -v '^#' "${fdata}"))
  ang=$(grep "#*ex.*${mang}" "${fdata}" | sed -e 's@.*=@@')
  echo "${dat[0]}  ${dat[1]}  ${dat[2]} ${ang} ${ex}" >> "${datf}"
done
