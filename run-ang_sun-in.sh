#!/usr/bin/bash

export LC_NUMERIC=en_US.UTF-8

fk=(0.9 0.95 1.0 1.05 1.1)
model="sun"
fdata="/tmp/data-${model}.tmp"
datadir="$PWD/data"
bindir="$PWD/magexp/bin"
prog=m4-tol
mod="in"
mang="s12"
Ep1=-3
Ep2=7
N=50

if [ ! -d $datadir ];then
  mkdir $datadir
fi

if [ ! -d $bindir ];then
  echo "ошибка: нет каталога '$bindir'"
  exit 1
fi

(( $# !=3 )) && 
{
  echo "сценарий требует 3 аргумента: маркер угла, количество шагов по энергии, количество шагов фактора угла"
  echo "пример: "
  echo "  $0 s12|s13 50 5"
  exit 2
}

case $1 in
  "s12")
    mang="s12"
    ;;
  "s13")
    mang="s13"
    ;;
  *)
    echo "ошибка: нераспознанный маркер: $1"
    exit 3
    ;;
esac

Ne="$2"
Nf="$3"

(( Nf/2 != (Nf-1)/2 )) &&
{
  echo "ошибка: количество шагов для фактора угла должно быть нечетным, Nf=${Nf}"
  exit 4
}

if [ ! -e $bindir/$prog ]; then
  echo "ошибка: нет расчетной программы $prog"
  exit 5
fi

tdir=${datadir}/${model}_${mod}_${mang}/"NexNf=${Ne}x${Nf}"
mkdir -p ${tdir}

for ex in "${fk[@]}"
do
	datf="${model}_${mod}_${mang}_fk=${ex}.dat"
	echo -n "" > "${datf}"
	for i in $(seq 0 1 $((N-1)))
	do
		./m4-tol ${model}.lua -c "Ep1=${Ep1};Ep2=${Ep2};d=(Ep2-Ep1)/(${N}-1);E=math.exp((${Ep1}+${i}*d)*math.log(10));${mang}=${ex}*${mang}" survprob.lua > "${fdata}"
		dat=($(grep -v '^#' "${fdata}"))
		ang=$(grep "#*ex.*${mang}" "${fdata}" | sed -e 's@.*=@@')
		echo "${dat[0]}  ${dat[1]}  ${dat[2]} ${ang} ${ex}" >> "${datf}"
	done
done
