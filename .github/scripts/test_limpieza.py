#!/usr/bin/env python3
"""
Test Sección 2: Limpieza de Datos (30 puntos)
Verifica que el código de limpieza esté presente.
"""

import json
import sys
import os

def encontrar_notebook():
    for file in os.listdir('.'):
        if file.endswith('.ipynb') and not file.startswith('.'):
            return file
    return None

def verificar_limpieza(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    codigo = ""
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            codigo += ''.join(cell.get('source', []))
    
    puntos = 0
    
    # Identificar nulos (5 pts)
    if 'isnull()' in codigo or 'isna()' in codigo:
        puntos += 2.5
    if '.dtypes' in codigo or '.info()' in codigo:
        puntos += 2.5
    
    # Rellenar nulos (10 pts)
    if '.fillna(' in codigo:
        puntos += 5
        if '.median()' in codigo:
            puntos += 5
        elif '.mean()' in codigo:
            puntos += 3
    
    # Convertir tipos (10 pts)
    if 'to_numeric' in codigo or 'astype' in codigo:
        puntos += 7
        if "errors='coerce'" in codigo or 'errors="coerce"' in codigo:
            puntos += 3
    
    # Verificación (5 pts)
    if 'df_limpio' in codigo:
        puntos += 5
    
    return min(int(puntos), 30)

if __name__ == "__main__":
    notebook = encontrar_notebook()
    if not notebook:
        print("❌ No notebook found")
        sys.exit(1)
    
    puntos = verificar_limpieza(notebook)
    print(f"Limpieza: {puntos}/30")
    
    sys.exit(0 if puntos >= 15 else 1)
