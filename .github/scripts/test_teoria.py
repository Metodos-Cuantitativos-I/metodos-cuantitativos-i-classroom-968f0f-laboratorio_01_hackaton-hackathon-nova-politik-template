#!/usr/bin/env python3
"""
Test Sección 1: Teoría (10 puntos)
Verifica las respuestas de opción múltiple.
"""

import json
import re
import sys
import os

RESPUESTAS_CORRECTAS = {'P1': 'B', 'P2': 'C', 'P3': 'B', 'P4': 'B', 'P5': 'C'}

def encontrar_notebook():
    for file in os.listdir('.'):
        if file.endswith('.ipynb') and not file.startswith('.'):
            return file
    return None

def extraer_respuestas(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    respuestas = {}
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = ''.join(cell.get('source', []))
            for i in range(1, 6):
                patterns = [
                    rf'RESPUESTA\s*P{i}[:\s]*\**\s*([A-Da-d])',
                    rf'\*\*RESPUESTA\s*P{i}:\*\*\s*([A-Da-d])',
                ]
                for pattern in patterns:
                    match = re.search(pattern, source, re.IGNORECASE)
                    if match:
                        respuestas[f'P{i}'] = match.group(1).upper()
                        break
    return respuestas

if __name__ == "__main__":
    notebook = encontrar_notebook()
    if not notebook:
        print("❌ No notebook found")
        sys.exit(1)
    
    respuestas = extraer_respuestas(notebook)
    correctas = sum(1 for p, r in RESPUESTAS_CORRECTAS.items() if respuestas.get(p) == r)
    puntos = correctas * 2
    
    print(f"Teoría: {puntos}/10 ({correctas}/5 correctas)")
    
    # Para GitHub Classroom, exit 0 si pasa umbral
    sys.exit(0 if puntos >= 6 else 1)
