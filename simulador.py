
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def cargar_corrientes(path):
    df = pd.read_csv(path)
    return df

def graficar_bloques(df):
    escala = 10000
    fig, ax = plt.subplots(figsize=(12, 6))
    x_cursor = 0
    espacio = 0.5

    for _, row in df.iterrows():
        name = row["Corriente"]
        tipo = row["Tipo"]
        Tin = row["T_entrada"]
        Tout = row["T_salida"]
        WCp = row["WCp"]

        color = "blue" if tipo == "Fría" else "red"
        ancho = WCp / escala
        Ttop = max(Tin, Tout)
        Tbot = min(Tin, Tout)
        altura = Ttop - Tbot

        # Bloque principal sólido
        ax.add_patch(patches.Rectangle((x_cursor, Tbot), ancho, altura,
                                       facecolor=color, edgecolor='black', linewidth=1.5))

        # Etiqueta
        txt_color = "white" if color == "blue" else "black"
        ax.text(x_cursor + ancho/2, Tbot + altura/2, f"{name}\n{int(WCp)}",
                ha='center', va='center', color=txt_color, fontsize=10, weight='bold')

        # Temperaturas
        ax.text(x_cursor + ancho + 0.1, Tin, f"{Tin:.1f}°F", fontsize=9)
        ax.text(x_cursor + ancho + 0.1, Tout, f"{Tout:.1f}°F", fontsize=9)

        x_cursor += ancho + espacio

    ax.set_ylim(0, 500)
    ax.set_xlim(0, x_cursor)
    ax.set_ylabel("Temperatura (°F)")
    ax.set_xlabel("Escala horizontal proporcional a WCp")
    ax.set_title("Diagrama base de bloques térmicos")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    archivo = "corrientes_problema_base.csv"
    df_corrientes = cargar_corrientes(archivo)
    graficar_bloques(df_corrientes)
