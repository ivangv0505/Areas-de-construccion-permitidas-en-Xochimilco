"""
Iván Garrido Velázquez
Cruzamiento de geometrías con GeoPandas
Analizar manzanas en áreas no permitidas para construcción.
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Ruta base relativa al archivo actual
script_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.abspath(os.path.join(script_dir, '..'))  

# Cargar los datos geoespaciales de las manzanas construidas
print("Cargando datos geoespaciales...")
mzbox2_path = os.path.join(base_path, 'dos1', 'clipmz20once.shp')
print(f"Ruta al archivo de manzanas: {mzbox2_path}")
mzbox2 = gpd.read_file(mzbox2_path)  # Carga el archivo de las manzanas
print("Datos de manzanas cargados:")
print(mzbox2.head())  # Muestra una vista previa de los datos de las manzanas

# Cargar los datos geoespaciales del polígono permitido para construcción
BOX_pol_path = os.path.join(base_path, 'dos1', 'BOX_20.shp')
print(f"Ruta al archivo del polígono: {BOX_pol_path}")
BOX_pol = gpd.read_file(BOX_pol_path)  # Carga el archivo del polígono
print("Datos del polígono cargados:")
print(BOX_pol.head())  # Muestra una vista previa de los datos del polígono

# Verificar y ajustar sistemas de coordenadas (CRS)
if mzbox2.crs != BOX_pol.crs:
    print("Ajustando sistemas de coordenadas (CRS)...")
    BOX_pol = BOX_pol.to_crs(mzbox2.crs)

# Unir todas las geometrías del polígono
poligono_union = BOX_pol.geometry.unary_union

# Identificar manzanas fuera del área permitida
manzanas_afectando = mzbox2[~mzbox2.geometry.intersects(poligono_union)]
print("Manzanas que afectan suelo de conservación:")
print(manzanas_afectando)

# Graficar resultados
print("Generando gráficas...")

# Gráfica 1: Mostrar el polígono permitido
BOX_pol.plot(color='lightgreen', edgecolor='black', alpha=0.7)
plt.title("Zonas Permitidas para Construcción (BOX_20)")
plt.show()

# Gráfica 2: Mostrar las manzanas construidas y las que afectan suelo de conservación
base = BOX_pol.plot(color='lightgreen', edgecolor='black', alpha=0.5, figsize=(10, 8))
mzbox2.plot(ax=base, color='lightgrey', edgecolor='black', label="Manzanas Construidas")
manzanas_afectando.plot(ax=base, color='red', alpha=0.7, label="Afectando Suelo de Conservación")
plt.title("Análisis de Construcción en Suelo de Conservación")
plt.legend(loc="upper right")
plt.show()

# Finalización
print("Proceso completado.")
