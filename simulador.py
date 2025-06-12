
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(layout="wide")
st.title("Simulador Interactivo - Método Gráfico de Bloques de Calor")

# Parámetros
delta_Tmin = 20
escala = 10000

# Cargar archivo
archivo = st.file_uploader("Sube el archivo CSV con los datos de las corrientes", type="csv")
if archivo is not None:
    data = pd.read_csv(archivo)
    st.dataframe(data)

    if "estado" not in st.session_state:
        st.session_state.estado = {
            row["Corriente"]: {
                "tipo": row["Tipo"],
                "T_in": row["T_entrada (°F)"],
                "T_out": row["T_salida (°F)"],
                "WCp": row["WCp (Btu/h°F)"],
                "satisfecho": False
            } for _, row in data.iterrows()
        }
        st.session_state.historial = []
        st.session_state.paso = 1

    estado = st.session_state.estado

    # Mostrar gráfica
    fig, ax = plt.subplots(figsize=(10, 6))
    x = 0
    colores = {"Fría": "blue", "Caliente": "red"}

    for nombre, valores in estado.items():
        ancho = valores["WCp"] / escala
        T1 = min(valores["T_in"], valores["T_out"])
        T2 = max(valores["T_in"], valores["T_out"])
        altura = T2 - T1
        color = colores[valores["tipo"]]
        ax.add_patch(patches.Rectangle((x, T1), ancho, altura,
                                       facecolor=color, edgecolor='black'))
        ax.text(x + ancho/2, T1 + altura/2, f"{nombre}\n{valores['WCp']}",
                ha='center', color='white' if color == 'blue' else 'black')
        ax.text(x + ancho + 0.2, T1, f"{T1:.1f}°F", fontsize=8)
        ax.text(x + ancho + 0.2, T2, f"{T2:.1f}°F", fontsize=8)
        x += ancho + 1

    ax.set_ylim(0, 550)
    ax.set_xlim(0, x)
    ax.set_ylabel("Temperatura (°F)")
    ax.set_xlabel("Escala horizontal ~ WCp")
    ax.set_title("Bloques de Calor")
    st.pyplot(fig)
