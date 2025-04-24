import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título neón (opcional - puedes quitarlo si prefieres el original)
st.markdown("""
<h1 style='text-align: center; color: #ff0000; 
            text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000;
            font-weight: bold;'>
    Tablero de Dibujo
</h1>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("🛠️ Personalización")
    
    # Herramientas de dibujo
    drawing_mode = st.selectbox(
        "Selecciona herramienta:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
        index=0  # freedraw como predeterminado
    )
    
    # Selectores de color
    col1, col2 = st.columns(2)
    with col1:
        stroke_color = st.color_picker("Color del pincel", "#FFFFFF")
    with col2:
        bg_color = st.color_picker("Color de fondo", "#000000")
    
    # Grosor de línea
    stroke_width = st.slider("Grosor del trazo", 1, 30, 5)

# Canvas con todas las funciones pero SIN cambiar el tamaño
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno para formas
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,  # ← Mantén estos valores como los tenías
    width=600,   # ← o ajústalos a tu preferencia
    drawing_mode=drawing_mode,
    key="full_featured_canvas"
)
