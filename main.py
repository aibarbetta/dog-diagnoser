# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import regex
import csv
from pprint import pprint
from operator import itemgetter

from PyInquirer import style_from_dict, Token, prompt

from examples import custom_style_3

print('Diagnosticador de perros')

questions = [
    {
        'type': 'list',
        'name': 'picazon',
        'message': 'Presenta picazón?',
        'choices': ['No', 'Normal', 'Intensa'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'comportamiento',
        'message': 'Cuál es su comportamiento?',
        'choices': ['Normal', 'Inquieto', 'Nervioso', 'Hiperactivo', 'Decaído', 'Apático'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'heridas',
        'message': 'Presenta heridas?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'pelaje',
        'message': 'Cuál es el estado del pelaje?',
        'choices': ['Normal', 'Con insectos', 'Con caídas leves', 'Con caídas severas'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'heces',
        'message': 'Cuál es el estado de las heces?',
        'choices': ['Normal', 'Con parásitos'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'sangrado',
        'message': 'Presenta sangrado?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'paralisis',
        'message': 'Presenta parálisis?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'ardor',
        'message': 'Presenta ardor?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'apetito',
        'message': 'Cuál es su apetito?',
        'choices': ['Normal', 'Leve', 'Moderado', 'Severo'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'fiebre',
        'message': 'Presenta fiebre?',
        'choices': ['No', 'Baja', 'Alta'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'convulsiones',
        'message': 'Presenta convulsiones?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'ojos',
        'message': 'Cuál es el estado de sus ojos?',
        'choices': ['Normal', 'Con lágrimas', 'Con pus'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'tos',
        'message': 'Presenta tos?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'estornudos',
        'message': 'Presenta estornudos?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'vomito',
        'message': 'Presenta vómitos?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'oidos',
        'message': 'Cuál es el estado de sus oídos?',
        'choices': ['Normal', 'Con temperatura', 'Con olor'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'debilidad',
        'message': 'Se encuentra débil?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'cojera',
        'message': 'Presenta cojera?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'dolor',
        'message': 'Presenta dolor?',
        'choices': ['No', 'Abdominal', 'En las extremidades'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'jadeo',
        'message': 'Jadea?',
        'choices': ['No', 'Si'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'ladridos',
        'message': 'Ladra?',
        'choices': ['Normal', 'Más de lo normal'],
        'filter': lambda val: val.lower()
    }
]

answers = prompt(questions, style=custom_style_3)
#print('Los síntomas son:')
#pprint(answers)

results = {}
with open("symptom_data.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    header = []
    for i, line in enumerate(reader):
        if (i == 0):
            # Save header
            header = line
        else:
            # Compute
            disease = line[0]
            line = line[1:]
            achievedScore = 0
            bestScore = len(line)

            #print('Computing for disease: ' + disease)
            for index, column in enumerate(header[1:]):
                #print('Parsing {}: {} == {}'.format(column, line[index], answers[column]))
                if answers[column] == line[index]:
                    achievedScore += 1
            results[disease] = round(100*float(achievedScore)/bestScore, 2)

results = sorted(results.items(), key=itemgetter(1), reverse=True)
for i in results:
    print('Chances de que tenga {}: {}%'.format(i[0], i[1]))
