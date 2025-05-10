#!/usr/bin/env bash
saludar() {
  local name=$1
  echo "hola, $name!"
}
saludar "equipo"

dividir() {
  local a=$1 b=$2
  (( b==0 )) && return 1
  echo "$((a/b))"
}
if res=$(dividir 10 2); then
  echo "división: $res"
else
  echo "error división"
fi