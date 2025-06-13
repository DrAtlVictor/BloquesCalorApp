
# BloquesCalorApp

Simulador interactivo del **método gráfico de bloques de calor** para síntesis de redes de intercambio térmico (HEN).  
Permite representar corrientes calientes y frías, aplicar intercambios paso a paso validando ΔTmin, y visualizar los bloques con sombreado parcial según los pasos aplicados.

---

## 📦 Archivos principales

- `simulador_bloques_lado_frio_corregido.py`: Aplicación principal desarrollada con Streamlit.
- `corrientes_problema_base.csv`: Archivo con las corrientes de entrada (nombre, tipo, temperatura, WCp).
- `requirements.txt`: Lista de dependencias necesarias.

---

## ▶️ Cómo ejecutar

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta la aplicación en Streamlit:

```bash
streamlit run simulador_bloques_lado_frio_corregido.py
```

3. Sube el archivo `corrientes_problema_base.csv` desde la interfaz de la app.

---

## 📋 Formato del archivo CSV

Debe contener los siguientes encabezados:

```
Corriente,Tipo,T_entrada,T_salida,WCp
```

Ejemplo de contenido:

```
C1,Fría,100,400,21600
C2,Caliente,480,250,31500
C3,Fría,150,360,24500
C4,Caliente,400,150,25200
C5,Fría,200,400,24700
```

---

## 🧠 Funcionalidades

- Lectura dinámica de datos desde archivo `.csv`
- Representación gráfica con bloques térmicos proporcionales a WCp y ΔT
- Aplicación de intercambios paso a paso con:
  - Validación de factibilidad por el lado caliente y el lado frío
  - Sombreado parcial (///) de bloques ya satisfechos
  - Flechas numeradas indicando el orden de intercambios

---

## ✍️ Autor

DrAtlVictor — basado en el método gráfico de contenido de calor (Smith, 2005).

