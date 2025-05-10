#!/usr/bin/env bash
# funciones marco y polo para guardar y restaurar el directorio de trabajo
marco() {
  export MARCO_DIR="$PWD"
  echo "Directorio guardado: $MARCO_DIR"
}

polo() {
  if [[ -z "$MARCO_DIR" ]]; then
    echo "error: no se  ejecuto marco previamente"
    return 1
  fi
  cd "$MARCO_DIR" || {
    echo "error: no se pudo cambiar al directorio $MARCO_DIR"
    return 1
  }
  echo "regresaste a: $PWD"
}