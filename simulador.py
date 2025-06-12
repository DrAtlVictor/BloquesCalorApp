
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(layout="wide")
st.title("Simulador Gráfico — Método de Bloques de Calor con Sombreado")

delta_Tmin = 20
escala = 10000

data = pd.DataFrame({
    "Corriente": ["C1", "C2", "C3", "C4", "C5"],
    "Tipo": ["Fría", "Caliente", "Fría", "Caliente", "Fría"],
    "T_inicial": [100, 480, 150, 400, 200],
    "T_objetivo": [400, 250, 360, 150, 400],
    "WCp": [21600, 31500, 24500, 25200, 24700]
})

satisf = {
    "C1": (100, 400),
    "C2": (274.3, 250),
    "C3": (150, 360),
    "C4": (195.8, 150),
    "C5": (200, 230.99)
}

colores = {"Fría": "blue", "Caliente": "red"}

fig, ax = plt.subplots(figsize=(10, 6))
x = 0
for _, row in data.iterrows():
    nombre = row["Corriente"]
    tipo = row["Tipo"]
    Tin = row["T_inicial"]
    Tout = row["T_objetivo"]
    WCp = row["WCp"]
    color = colores[tipo]
    ancho = WCp / escala
    Tmin, Tmax = sorted([Tin, Tout])
    altura = Tmax - Tmin
    ax.add_patch(patches.Rectangle((x, Tmin), ancho, altura, facecolor=color, edgecolor="black"))
    if nombre in satisf:
        T1, T2 = satisf[nombre]
        T_somb_min, T_somb_max = sorted([T1, T2])
        altura_somb = T_somb_max - T_somb_min
        ax.add_patch(patches.Rectangle((x, T_somb_min), ancho, altura_somb,
                      facecolor="none", hatch="///", edgecolor="black", linewidth=0.8))

    ax.text(x + ancho/2, Tmin + altura/2, f"{nombre}\n{WCp}", ha="center", color='white' if color=="blue" else 'black', fontsize=8)
    ax.text(x + ancho + 0.2, Tmin, f"{Tmin:.1f}°F", fontsize=8)
    ax.text(x + ancho + 0.2, Tmax, f"{Tmax:.1f}°F", fontsize=8)
    x += ancho + 1

ax.set_ylim(0, 550)
ax.set_xlim(0, x)
ax.set_ylabel("Temperatura (°F)")
ax.set_xlabel("Escala horizontal proporcional a WCp")
ax.set_title("Vista de bloques con sombreado parcial")
st.pyplot(fig)
