
# BloquesCalorApp

Simulador interactivo del método gráfico de bloques de calor. Desarrollado en Python con Streamlit.

## Archivos incluidos

- `simulador.py`: archivo principal del simulador
- `corrientes_problema_base.csv`: datos de entrada del problema 5SPI
- `requirements.txt`: dependencias necesarias para ejecutar el simulador

## Cómo ejecutar en Streamlit Cloud

1. Sube esta carpeta a un repositorio de GitHub llamado `BloquesCalorApp`.
2. Ve a https://streamlit.io/cloud y crea una cuenta.
3. Haz clic en **New App**, selecciona tu repositorio y el archivo `simulador.py`.
4. Ejecuta la app.

## Cómo ejecutar localmente

1. Instala las dependencias:
```
pip install streamlit matplotlib pandas numpy
```

2. Ejecuta:
```
streamlit run simulador.py
```
