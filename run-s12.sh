#!/usr/bin/bash

export LC_NUMERIC=en_US.UTF-8

fk=(0.9 0.95 1.0 1.05 1.1)
model="sun"
fdata="/tmp/data-${model}.tmp"
E="1.0"
mod="in"
mang="s12"

datf="/tmp/${model}_${mod}_${mang}_E=${E}.dat"
echo -n "" > ${datf}
for ex in ${fk[@]}
do
  ./m4-tol ${model}.lua -c "E=${E};s12=${ex}*s12" survprob.lua > "${fdata}"
  dat=($(grep -v '^#' "${fdata}"))
  ang=$(grep '#*ex.*s12' "${fdata}" | sed -e 's@.*=@@')
  echo "${dat[0]}  ${dat[1]}  ${dat[2]} ${ang} ${ex}" >> "${datf}"
done
