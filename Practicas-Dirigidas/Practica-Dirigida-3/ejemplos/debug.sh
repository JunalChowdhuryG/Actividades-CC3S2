#!/usr/bin/env bash
set -xe
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
trap 'echo "error en linea $LINENO"; exit 1' ERR

# ejemplo con error intencional
ls /no_existe