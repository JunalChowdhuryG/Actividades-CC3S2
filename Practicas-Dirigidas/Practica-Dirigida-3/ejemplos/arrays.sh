#!/usr/bin/env bash
FRUTAS=(manzana banana cereza)
FRUTAS+=("durazno")

echo "Total frutas: ${#FRUTAS[@]}"
for f in "${FRUTAS[@]}"; do
  echo "Fruta: $f"
done

declare -A EDADES=([Alice]=28 [Kapu]=35)
echo "Kapu tiene ${EDADES[Kapu]} años"