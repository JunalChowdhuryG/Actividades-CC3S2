#!/usr/bin/env bash
email="$1"
re='^[[:alnum:]_.+-]+@[[:alnum:]-]+\.[[:alnum:].-]+$'
if [[ $email =~ $re ]]; then
  echo "email valido"
  echo "Usuario: ${BASH_REMATCH[1]}"  # primer grupo
else
  echo "email invalido"
fi