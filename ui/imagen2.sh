#!/bin/sh
echo "creando imagen"
eval "docker build -t angular-nginx ."
echo "se creo la imagen con nombre angular-nginx"
