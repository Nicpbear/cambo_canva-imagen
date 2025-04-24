import streamlit as st
from streamlit_drawable_canvas import st_canvas

# 1. Título original (sin cambios)
st.title("Tablero para dibujo")

# 2. Barra lateral CON las nuevas personalizaciones (agregado)
with st.sidebar:
    st.subheader("Propiedades del Tablero")
    
    # Selector de herramientas (nuevo)
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
        index=0  # 'freedraw' como predeterminado
    )
    
    # Selectores de color (nuevos)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")
    
    # Grosor de línea (nuevo)
    stroke_width = st.slider("Ancho de línea", 1, 30, 5)

# 3. Canvas original PERO usando las nuevas personalizaciones (modificado solo en parámetros)
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,        # ← Usa el valor del slider
    stroke_color=stroke_color,        # ← Usa el color seleccionado
    background_color=bg_color,       # ← Usa el color de fondo elegido
    height=300,                       # ← Tamaño original (sin cambios)
    width=500,                        # ← Tamaño original (sin cambios)
    drawing_mode=drawing_mode,        # ← Usa la herramienta seleccionada
    key="canvas"
)

# 4. El resto de tu código (si existiera) permanecería aquí sin cambios
