import streamlit as st
import pandas as pd
import numpy as np

# Para que la pág quede grande
st.set_page_config(
    layout="wide"
)

# Título
st.markdown("<center><h1>◇◇◇◇◇◇◇◇ Solución - Evaluación de desempeño. ◇◇◇◇◇◇◇◇</h1></center>", unsafe_allow_html=True)


# Dataframe
st.subheader("Dataframe en pantalla: ")
archivo_csv = 'static/datasets/sales_data.csv'
dataframe_csv = pd.read_csv(archivo_csv)
st.dataframe(dataframe_csv)


# FILTROS

st.markdown("<center><h1>------- Filtros. ------- </h1></center>", unsafe_allow_html=True)


# Selector
st.subheader("Filtro de selector : ")
categoria = dataframe_csv['Category'].unique()
filtro_selector = st.selectbox("Filtrar por Electronics o Accessories: ", categoria)
df_filtro_selector = dataframe_csv[dataframe_csv['Category'] == filtro_selector]
st.write("Dataframe filtrado por selector:")
st.dataframe(df_filtro_selector)

# Control deslizante
st.subheader("Filtro de control deslizante: ")
minimo = dataframe_csv['Price'].min()
maximo = dataframe_csv['Price'].max()
rango = st.slider("Selecciona un rango de precios: ", min_value=minimo, max_value=maximo, value=(minimo, maximo))

df_dataframe_csv = dataframe_csv[
    (dataframe_csv["Category"] == filtro_selector) &
    (dataframe_csv["Price"] >= rango[0]) &
    (dataframe_csv["Price"] <= rango[1])
]


st.write("Dataframe filtrado por precio- slider:")
st.dataframe(df_dataframe_csv)

# ESTADÍSTICAS
st.markdown("<center><h1>°°°°°°° Estadísticas. °°°°°°° </h1></center>", unsafe_allow_html=True)


# Total de ventas
st.subheader("Total Estadísticas: ")
if not df_dataframe_csv.empty:
    categoria_total_sales = df_dataframe_csv["Total_Sales"].sum()
    categoria_price = df_dataframe_csv["Price"].mean()

    columna1, columna2 = st.columns(2)
    columna1.metric("Total de ventas: ",f"${categoria_total_sales:,.2f}")
    columna2.metric("Total de precios: ",f"${categoria_price:,.2f}")
else:
    st.write("No hay datos para mostrar.")

# Este es el excel con la data, está comentado para que no se genere siempre que se habra el archivo.
# np.random.seed(42)
# dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
# products = ["Laptop", "Phone", "Tablet", "Headphones"]
# categories = ["Electronics", "Accessories"]
# data = {
#     "Date": np.random.choice(dates, 50),
#     "Product": np.random.choice(products, 50),
#     "Category": np.random.choice(categories, 50),
#     "Price": np.random.uniform(50, 500, 50).round(2),
#     "Quantity": np.random.randint(1, 5, 50)
# }
# df = pd.DataFrame(data)
# df["Total_Sales"] = df["Price"] * df["Quantity"]
# df.to_csv("sales_data.csv", index=False)




#Código para cambiar el color de fondo de la página
color_inicio = "#4A148C"
color_fin = "#A9A9A9"
direccion = "to bottom"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient({direccion}, {color_inicio}, {color_fin});
    }}
    </style>
    """,
    unsafe_allow_html=True
)

