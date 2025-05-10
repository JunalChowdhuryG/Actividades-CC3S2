#!/usr/bin/env bash
set -u  # error si variable no definida
NOMBRE="Cesar"
readonly PI=3.14159
export ENV="producción"

echo "Usuario: $NOMBRE"
echo "PI vale: $PI"
echo "Entorno: $ENV"