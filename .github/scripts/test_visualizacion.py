#!/usr/bin/env python3
"""
Test Sección 4: Visualización (30 puntos)
Verifica que los mapas estén generados y la conclusión escrita.
"""

import json
import sys
import os

def encontrar_notebook():
    for file in os.listdir('.'):
        if file.endswith('.ipynb') and not file.startswith('.'):
            return file
    return None

def verificar_visualizacion(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    codigo = ""
    markdown = ""
    
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            codigo += ''.join(cell.get('source', []))
        elif cell.get('cell_type') == 'markdown':
            markdown += ''.join(cell.get('source', [])).lower()
    
    puntos = 0
    
    # Mapa 1 (10 pts)
    if '.plot(' in codigo:
        puntos += 3
        if 'equal_interval' in codigo:
            puntos += 3
        if "'Reds'" in codigo or '"Reds"' in codigo:
            puntos += 2
        if 'set_title' in codigo or 'title=' in codigo:
            puntos += 2
    
    # Mapa 2 (10 pts)
    if 'quantiles' in codigo:
        puntos += 4
    if "'YlOrRd'" in codigo or '"YlOrRd"' in codigo:
        puntos += 3
    if 'legend=True' in codigo:
        puntos += 3
    
    # Conclusión (10 pts)
    if 'conclusión' in markdown or 'mi conclusión' in markdown:
        if 'engañoso' in markdown or 'engañosa' in markdown:
            puntos += 3
        if 'normaliz' in markdown or 'tasa' in markdown:
            puntos += 2
        if 'provincia' in markdown:
            puntos += 3
        if 'limitación' in markdown or 'limitacion' in markdown:
            puntos += 2
    
    return min(int(puntos), 30)

if __name__ == "__main__":
    notebook = encontrar_notebook()
    if not notebook:
        print("❌ No notebook found")
        sys.exit(1)
    
    puntos = verificar_visualizacion(notebook)
    print(f"Visualización: {puntos}/30")
    
    sys.exit(0 if puntos >= 15 else 1)
