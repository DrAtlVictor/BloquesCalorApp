
# BloquesCalorApp

Simulador interactivo del **método gráfico de bloques de calor** para síntesis de redes de intercambio térmico.  
Permite representar corrientes, aplicar intercambios paso a paso y visualizar bloques con sombreado parcial.

---

## 📁 Archivos

- `simulador.py`: aplicación principal con Streamlit.
- `corrientes_problema_base.csv`: corrientes de entrada.
- `requirements.txt`: dependencias necesarias.
- `README.md`: esta descripción.

---

## ▶️ Cómo ejecutar

1. Instala las dependencias:

```
pip install -r requirements.txt
```

2. Ejecuta con:

```
streamlit run simulador.py
```

3. Sube el archivo `corrientes_problema_base.csv` desde la interfaz.

---

## 📋 Formato del CSV

Encabezados requeridos:

```
Corriente,Tipo,T_entrada,T_salida,WCp
```

Ejemplo:

```
C1,Fría,100,400,21600
C2,Caliente,480,250,31500
...
```

---

## 🧠 Funciones clave

- Validación de ΔTmin por arriba y por abajo
- Sombreado parcial cuando el intercambio es por el lado frío
- Flechas numeradas en bloques satisfechos
