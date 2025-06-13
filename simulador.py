
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Cargar corrientes desde archivo CSV
def cargar_corrientes(file_path):
    return pd.read_csv(file_path)

# Dibujar bloques con sombreado por debajo (lado frío)
def dibujar_bloques(corrientes, intercambios):
    escala = 10000
    fig, ax = plt.subplots(figsize=(12, 6))
    x_offset = 0
    espacio = 0.5

    for _, row in corrientes.iterrows():
        nombre = row['Corriente']
        tipo = row['Tipo']
        Tin = row['T_entrada']
        Tout = row['T_salida']
        WCp = row['WCp']
        ancho = WCp / escala
        Tmin, Tmax = min(Tin, Tout), max(Tin, Tout)
        altura = Tmax - Tmin
        color = 'blue' if tipo.lower() == 'fría' else 'red'
        txt_color = 'white' if color == 'blue' else 'black'

        # bloque base
        ax.add_patch(patches.Rectangle((x_offset, Tmin), ancho, altura,
                                       edgecolor='black', facecolor=color, lw=1.5, alpha=0.6))

        # sombreado parcial
        for i, inter in enumerate(intercambios):
            if inter['corriente'] == nombre:
                Tsat1, Tsat2 = inter['T1'], inter['T2']
                ybot, ytop = min(Tsat1, Tsat2), max(Tsat1, Tsat2)
                ax.add_patch(patches.Rectangle((x_offset, ybot), ancho, ytop - ybot,
                                               hatch='///', facecolor=color, edgecolor='black', lw=0.5))
                xm = x_offset + ancho / 2
                ym = ybot + (ytop - ybot)/2
                ax.annotate(f"{inter['paso']}", (xm, ym), color='black', fontsize=9, ha='center')

        # etiquetas
        ax.text(x_offset + ancho/2, Tmin + altura/2, f"{nombre}\n{int(WCp)}",
                ha='center', va='center', color=txt_color, fontsize=10, weight='bold')
        ax.text(x_offset + ancho + 0.1, Tin, f"{Tin:.1f}°F", fontsize=9)
        ax.text(x_offset + ancho + 0.1, Tout, f"{Tout:.1f}°F", fontsize=9)

        x_offset += ancho + espacio

    ax.set_ylim(0, 500)
    ax.set_xlim(0, x_offset)
    ax.set_xlabel("Escala horizontal proporcional a WCp")
    ax.set_ylabel("Temperatura (°F)")
    ax.set_title("Diagrama con sombreado parcial (lado frío corregido)")
    st.pyplot(fig)

# Streamlit app
st.title("Simulador de bloques de calor — versión corregida")
uploaded_file = st.file_uploader("Carga el archivo de corrientes CSV", type="csv")

if uploaded_file:
    corrientes = cargar_corrientes(uploaded_file)
    st.dataframe(corrientes)

    # Historial de intercambios (solo para visualización)
    intercambios = st.session_state.get("intercambios", [])

    if st.button("Ejemplo: sombreado parcial por debajo"):
        intercambios.append({'corriente': 'C1', 'T1': 100, 'T2': 260.2, 'paso': '1'})
        intercambios.append({'corriente': 'C5', 'T1': 200, 'T2': 230.99, 'paso': '2'})
        st.session_state['intercambios'] = intercambios

    dibujar_bloques(corrientes, intercambios)
