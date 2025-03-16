# Areas-de-construccion-permitidas-en-Xochimilco

## Descripción
Este proyecto utiliza Python, GeoPandas y Matplotlib para analizar datos geoespaciales y detectar construcciones en áreas destinadas a la conservación. El script carga datos desde shapefiles que representan manzanas construidas y un polígono con la zona permitida para construcción. Posteriormente, se ajustan los sistemas de coordenadas para garantizar la coherencia y se realiza un cruce de geometrías para identificar aquellas manzanas que se encuentran fuera del área autorizada, facilitando la toma de decisiones informadas en la gestión del territorio y la preservación de suelo de conservación.

## Requisitos

Para ejecutar este proyecto, necesitas lo siguiente:

### Bibliotecas de Python
- **GeoPandas**: Para el manejo y análisis de datos geoespaciales.
- **Matplotlib**: Para la generación de gráficas.
- **OS**: Para la manipulación de rutas de archivos.

Puedes instalarlas usando pip:
```bash
pip install geopandas matplotlib
```


### Archivos de datos
- **`clipmz20once.shp`**: Shapefile que contiene las geometrías de las manzanas construidas.
- **`BOX_20.shp`**: Shapefile que define el polígono de las áreas permitidas para construcción.

Estos archivos deben estar ubicados en el subdirectorio `dos1` relativo a la carpeta raíz del proyecto.

## Uso
Ejecuta el script "lectura_de_shape_intersection.py"
```bash
python lectura_de_shape_intersection.py
```
## Resultados

Al ejecutar el script, se obtienen los siguientes resultados:

- **Datos procesados**:  
  - Se muestra en la consola una vista previa de los datos geoespaciales cargados, incluyendo las manzanas construidas y el polígono de áreas permitidas.  
  - Se imprime una lista de las manzanas que se encuentran fuera del área autorizada para construcción, es decir, aquellas que afectan el suelo de conservación.  

- **Visualizaciones**:  
  - **Gráfica 1**: Representa el polígono de las áreas permitidas para construcción, destacado en verde claro. Esta gráfica permite visualizar el límite de la zona autorizada.  
  - **Gráfica 2**: Muestra una combinación del polígono permitido, las manzanas construidas (en gris) y las manzanas que afectan el suelo de conservación (en rojo). Esta visualización facilita la identificación de las áreas en conflicto y es clave para la toma de decisiones en la gestión del territorio.