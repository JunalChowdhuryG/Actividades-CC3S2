#!/usr/bin/env bash
# encuentra  HTMLs recursivamente y  comprime en  ZIP

find . -type f -name "*.html" -print0 | xargs -0 zip html_files.zip