#!/usr/bin/env bash
# archivos reciente
latest=$(find . -type f -printf "%T@ %p\n" | sort -nr | head -n1 | cut -d' ' -f2-)
if [[ -n "$latest" ]]; then
  echo "archivo reciente: $latest"
else
  echo "no hay   archivos"
fi

# impprime lista de archivo ordenadoss
echo -e "\narchivos ordenados por fecha"
find . -type f -printf "%T@ %TY-%Tm-%Td %TH:%TM %p\n" | sort -nr | cut -d' ' -f2-