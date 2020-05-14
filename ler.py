#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, subprocess

path="/home/edson/"
file="codigo"
ref_arquivo = open(path + file, "r")

etapa = 0

for linha in ref_arquivo:

        if etapa == 0:
                if "printf" in linha:
                        etapa = 1

        if etapa == 1:
                if "(" in linha:
                        etapa = 2

        if etapa == 2:
                if ")" in linha:
                        etapa = 3

        if etapa == 3:
                if ";" in linha:
                    if etapa == 3:
                        print('Você utilizou PONTO E VIRGULA somente em uma linha')

                else:
                    print('Infelismente não localizamos o PONTO E VIRGULA')
ref_arquivo.close()

