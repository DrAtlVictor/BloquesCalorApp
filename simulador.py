
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(layout="wide")
st.title("Simulador Interactivo - Método Gráfico de Bloques de Calor")

delta_Tmin = 20
escala = 10000

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
    colores = {"Fría": "blue", "Caliente": "red"}

    # Selección de corrientes
    cols = st.columns(2)
    calientes = [k for k, v in estado.items() if v["tipo"] == "Caliente" and not v["satisfecho"]]
    frias = [k for k, v in estado.items() if v["tipo"] == "Fría" and not v["satisfecho"]]

    caliente = cols[0].selectbox("Corriente Caliente", [""] + calientes)
    fria = cols[1].selectbox("Corriente Fría", [""] + frias)

    def aplicar_intercambio(c, f):
        C = estado[c]
        F = estado[f]
        Tcc = C["T_in"]
        Tff = F["T_out"]

        if Tcc <= Tff + delta_Tmin:
            st.warning("No se cumple ∆Tmin para contracorriente.")
            return

        delta_Tf = F["T_out"] - F["T_in"]
        Qf = F["WCp"] * delta_Tf

        delta_Tc = C["T_in"] - C["T_out"]
        Qc = C["WCp"] * delta_Tc

        Q_real = min(Qf, Qc)
        deltaT_C = Q_real / C["WCp"]
        deltaT_F = Q_real / F["WCp"]

        C["T_in"] -= deltaT_C
        F["T_in"] += deltaT_F

        if abs(C["T_in"] - C["T_out"]) < 1:
            C["satisfecho"] = True
        if abs(F["T_in"] - F["T_out"]) < 1:
            F["satisfecho"] = True

        st.session_state.historial.append((st.session_state.paso, c, f, Q_real))
        st.session_state.paso += 1

    if st.button("Aplicar intercambio"):
        if caliente and fria:
            aplicar_intercambio(c=caliente, f=fria)

    # Mostrar gráfica
    fig, ax = plt.subplots(figsize=(10, 6))
    x = 0
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

    # Mostrar historial
    if st.session_state.historial:
        st.subheader("Historial de intercambios")
        df_hist = pd.DataFrame(st.session_state.historial, columns=["Paso", "Caliente", "Fría", "Q (Btu/h)"])
        st.dataframe(df_hist)
