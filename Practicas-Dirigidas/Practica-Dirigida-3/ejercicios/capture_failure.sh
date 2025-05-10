#!/usr/bin/env bash
# ejecuta un comando hasta que falle, captura stdout/stderr y cuenta ejecuciones

count=0
while true; do
  ((count++))
  echo "ejecucion $count"
  n=$(( RANDOM % 100 ))
  if [[ $n -eq 42 ]]; then
    echo "algo paso" > stdout.log
    echo "el error por usar numero magicos" >&2 2> stderr.log
    echo "fallo en la ejecucion $count"
    echo "salida estandar:"
    cat stdout.log
    echo "salida de error:"
    cat stderr.log
    exit 1
  fi
  echo "todo ah salidos de acuerdo al plan" >> stdout.log
done