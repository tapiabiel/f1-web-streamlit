import streamlit as st
import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
from io import BytesIO

# Configuración de gráficos estilo F1
plotting.setup_mpl()

st.title("📊 Análisis de Fórmula 1 con FastF1")

# --- Menús interactivos ---
season_year = st.number_input("Año de la temporada", min_value=2018, max_value=2025, value=2025, step=1)
grand_prix = st.text_input("Gran Premio (ej: Spain, Monaco (en inglés))")
session_type = st.selectbox("Tipo de sesión", ["R", "Q", "FP1", "FP2", "FP3"])

piloto_1 = st.text_input("Código piloto 1 (ej: VER, HAM, NOR, PIA)")
piloto_2 = st.text_input("Código piloto 2")

if st.button("Analizar"):
    # Cargar sesión
    session = fastf1.get_session(season_year, grand_prix, session_type)
    session.load()

    # Obtener vueltas
    laps_1 = session.laps.pick_driver(piloto_1).pick_accurate()
    laps_2 = session.laps.pick_driver(piloto_2).pick_accurate()

    laps_1 = laps_1[laps_1['LapTime'].notna()]
    laps_2 = laps_2[laps_2['LapTime'].notna()]

    if laps_1.empty or laps_2.empty:
        st.error("No se encontraron datos de vueltas para los pilotos seleccionados.")
    else:
        # Calcular tiempos medios y mejores vueltas
        media_1 = laps_1['LapTime'].mean().total_seconds()
        media_2 = laps_2['LapTime'].mean().total_seconds()

        mejor_vuelta_1 = laps_1['LapTime'].min().total_seconds()
        mejor_vuelta_2 = laps_2['LapTime'].min().total_seconds()

        # Mostrar resultados
        st.subheader(f"Resultados: {piloto_1} vs {piloto_2}")
        col1, col2 = st.columns(2)
        col1.metric(f"{piloto_1} Tiempo Medio", f"{media_1:.3f} s")
        col1.metric(f"{piloto_1} Mejor Vuelta", f"{mejor_vuelta_1:.3f} s")

        col2.metric(f"{piloto_2} Tiempo Medio", f"{media_2:.3f} s")
        col2.metric(f"{piloto_2} Mejor Vuelta", f"{mejor_vuelta_2:.3f} s")

        # --- Graficar ---
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(laps_1['LapNumber'], laps_1['LapTime'].dt.total_seconds(),
                marker='o', label=f"{piloto_1} (media: {media_1:.2f}s)")
        ax.plot(laps_2['LapNumber'], laps_2['LapTime'].dt.total_seconds(),
                marker='o', label=f"{piloto_2} (media: {media_2:.2f}s)")

        ax.set_xlabel('Número de vuelta')
        ax.set_ylabel('Tiempo de vuelta (s)')
        ax.set_title(f'Tiempos de vuelta - GP {grand_prix} {season_year}')
        ax.legend()
        ax.grid(True)

        # Mostrar gráfico
        st.pyplot(fig)

        # Guardar en memoria
        buf = BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)

        # Botón de descarga
        st.download_button(
            label="Descargar gráfico como PNG",
            data=buf,
            file_name=f"comparativa_{piloto_1}_{piloto_2}_{grand_prix}_{season_year}.png",
            mime="image/png"
        )
