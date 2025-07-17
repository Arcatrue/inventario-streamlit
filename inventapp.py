import streamlit as st
import pandas as pd

# Ajustar diseño a pantalla completa
st.set_page_config(layout="wide")

# Título de la app
st.title("📦 Inventario por Sucursal")

# Cargar archivo Excel
@st.cache_data
def cargar_datos():
    df = pd.read_excel("ExportWWBodegaProducto (15).xlsx", sheet_name="Sheet1", skiprows=3)
    df.columns = ["Codigo", "Concepto", "Bodega", "Saldo", "CostoUnitario"]
    df = df.dropna(subset=["Codigo", "Concepto", "Bodega", "Saldo"])
    df["Saldo"] = pd.to_numeric(df["Saldo"], errors="coerce")
    df["CostoUnitario"] = pd.to_numeric(df["CostoUnitario"], errors="coerce")
    return df

df = cargar_datos()
sucursales = df["Bodega"].dropna().unique()

# Mostrar botones por sucursal
sucursal_seleccionada = st.radio("Selecciona una sucursal:", sucursales)

# Mostrar tabla filtrada
df_filtrado = df[df["Bodega"] == sucursal_seleccionada]
st.write(f"Inventario de: **{sucursal_seleccionada}**")
st.dataframe(df_filtrado.reset_index(drop=True), use_container_width=True)

# Mostrar total de saldo
st.markdown(f"### 🔢 Total saldo: {df_filtrado['Saldo'].sum():,.0f}")
