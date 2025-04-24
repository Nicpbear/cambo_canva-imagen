import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de página
st.set_page_config(layout="wide")

# --- TÍTULO CON EFECTO NEÓN ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bungee&display=swap');
.neon-title {
    font-family: 'Bungee', cursive;
    text-align: center;
    color: #FF2A6D;
    text-shadow: 0 0 10px #FF2A6D, 0 0 20px #D1F7FF, 0 0 30px #05E0FF;
    margin-bottom: 20px;
}
</style>
<h1 class="neon-title">TABLERO INCREÍBLE</h1>
""", unsafe_allow_html=True)

# --- CONTROLES DE PREDICCIÓN EN PÁGINA PRINCIPAL ---
col1, col2 = st.columns([1, 3])
with col1:
    api_key = st.text_input("API Key", type="password")
with col2:
    predict_btn = st.button("✨ Predecir", use_container_width=True)

# --- BARRA LATERAL SOLO CON HERRAMIENTAS DE DIBUJO ---
with st.sidebar:
    st.header("🎨 Herramientas de Dibujo")
    drawing_mode = st.selectbox(
        "Modo de dibujo:",
        ["freedraw", "line", "rect", "circle", "transform", "polygon", "point"],
        index=0
    )
    col1, col2 = st.columns(2)
    with col1:
        stroke_color = st.color_picker("Color", "#FFFFFF")
    with col2:
        bg_color = st.color_picker("Fondo", "#000000")
    stroke_width = st.slider("Grosor", 1, 30, 5)

# --- ÁREA DE DIBUJO ---
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=600,
    width=800,
    drawing_mode=drawing_mode,
    key="ultimate_canvas"
)

# --- LÓGICA DE PREDICCIÓN ---
if predict_btn and api_key:
    with st.spinner("Analizando tu dibujo..."):
        try:
            # Simulación de respuesta (reemplaza con tu API real)
            mock_response = {
                "predictions": [
                    {"label": "Figura reconocida", "confidence": 0.92},
                    {"label": "Elemento secundario", "confidence": 0.87}
                ],
                "analysis": "Se ha identificado el dibujo correctamente."
            }
            
            st.success("Predicción completada!")
            st.json(mock_response)
            
        except Exception as e:
            st.error(f"Error en la predicción: {str(e)}")
elif predict_btn:
    st.warning("⚠️ Por favor ingresa tu API Key")

# Estilo mínimo para el botón
st.markdown("""
<style>
.stButton>button {
    border: 2px solid #4CAF50 !important;
    transition: all 0.3s;
}
.stButton>button:hover {
    background-color: #4CAF50 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)
