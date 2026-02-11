#!/usr/bin/env python3
"""
Test Sección 3: Cálculo de Índices (30 puntos)
Verifica que los índices estén calculados.
"""

import json
import sys
import os

def encontrar_notebook():
    for file in os.listdir('.'):
        if file.endswith('.ipynb') and not file.startswith('.'):
            return file
    return None

def verificar_indices(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    codigo = ""
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            codigo += ''.join(cell.get('source', []))
    
    puntos = 0
    
    # Tasa de protestas (15 pts)
    if 'tasa_protestas' in codigo:
        puntos += 5
        if '/ poblacion' in codigo.replace(' ', '') or '/poblacion' in codigo.replace(' ', '') or "['poblacion']" in codigo:
            puntos += 5
            if '* 10000' in codigo or '*10000' in codigo:
                puntos += 5
    
    # Índice de inestabilidad (10 pts)
    if 'indice_inestabilidad' in codigo:
        puntos += 7
        if 'tasa_heridos' in codigo:
            puntos += 3
    
    # Merge (5 pts)
    if '.merge(' in codigo:
        puntos += 3
        if 'gdf_final' in codigo:
            puntos += 2
    
    return min(int(puntos), 30)

if __name__ == "__main__":
    notebook = encontrar_notebook()
    if not notebook:
        print("❌ No notebook found")
        sys.exit(1)
    
    puntos = verificar_indices(notebook)
    print(f"Índices: {puntos}/30")
    
    sys.exit(0 if puntos >= 15 else 1)
