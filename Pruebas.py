import numpy as np
import pandas as pd

ventas = pd.Series([1200, 950, 1430, 1100],
                   index=["ene", "feb", "mar", "abr"])
#print(ventas)

# un diccionario de columnas -> una tabla
pedidos = pd.DataFrame({
    "cliente": ["Ana", "Luis", "Marta", "Pedro"],
    "ciudad": ["Madrid", "Bilbao", "Madrid", "Valencia"],
    "importe": [120.5, 89.0, 200.0, 45.0],
    "unidades": [3, 1, 5, 2],
},index=['i0','i1','i2','i3'])
#print(pedidos)
'''
perdidos_nueva = pedidos.set_index('cliente')
print(perdidos_nueva)
vuelta = pedidos.reset_index()
print(vuelta)
'''
loc_aux = pedidos.loc['i1']
#print(loc_aux['ciudad'])

# ventas por tienda, con un dato que falta
ventas = pd.DataFrame({
    "tienda": ["norte", "norte", "sur", "sur", "sur"],
    "producto": ["teclado", "raton", "teclado", "teclado", "raton"],
    "unidades": [10, 5, 8, 12, 3],
    "importe": [250.0, 60.0, 200.0, np.nan, 36.0],
})

# una clave, una columna, una funcion
por_tienda = ventas.groupby("tienda")["importe"].sum()
#print(por_tienda)
#print(por_tienda["norte"])

# varias columnas agregadas a la vez
#print(ventas.groupby("tienda")[["importe", "unidades"]].sum())

# una funcion distinta por columna, con nombres propios
'''print(
    ventas.groupby("tienda").agg(
        importe_total=("importe", "sum"),
        unidades_media=("unidades", "mean"),
    )
)'''
'''
# agrupar por dos claves
por_tp = ventas.groupby(["tienda", "producto"])["importe"].sum()
#print(por_tp)
#print(por_tp.index.nlevels)

# una fila del MultiIndex: hace falta una tupla
print(por_tp.loc[("norte", "teclado")])

# agrupar por dos claves
por_tp = ventas.groupby(["tienda", "producto"])["importe"].sum()
print(por_tp)
print(por_tp.index.nlevels)

# una fila del MultiIndex: hace falta una tupla
print(por_tp.loc[("norte", "teclado")])

# aplanar: los niveles vuelven a ser columnas
plano = por_tp.reset_index()
print(plano)
print(plano.columns.tolist())
'''

# seis alumnos, con huecos repartidos
alumnos = pd.DataFrame({
    "alumno": ["Ana", "Luis", "Marta", "Pedro", "Nuria", "Ivan"],
    "edad": [25, np.nan, 40, 33, np.nan, np.nan],
    "nota": [7.5, 8.0, np.nan, 6.0, 9.0, np.nan],
    "ciudad": ["Madrid", "Bilbao", "Madrid", None, "Valencia", "Sevilla"],
})

# el total, y el porcentaje sobre todas las celdas
total = alumnos.isna().sum().sum()
#print(total)

# 1. guarda en sin_huecos solo las filas sin ningun hueco
sin_huecos = alumnos.dropna()
#print(sin_huecos)

# apilar por filas, renumerando el indice
enero = pd.DataFrame({"producto": ["teclado", "raton"], "unidades": [10, 20]})
febrero = pd.DataFrame({"producto": ["teclado", "monitor"], "unidades": [15, 8]})
trimestre = pd.concat([enero, febrero], ignore_index=True)
#print(trimestre)

# columnas que no coinciden: se rellenan con NaN
marzo = pd.DataFrame({"producto": ["webcam"], "devoluciones": [2]})
#print(pd.concat([enero, marzo], ignore_index=True))

import pandas as pd

clientes = pd.DataFrame({
    "cliente_id": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Marta", "Pedro"],
})
pedidos = pd.DataFrame({
    "cliente_id": [3, 3, 4, 5],
    "importe": [100.0, 50.0, 200.0, 80.0],
})

# 1. guarda en inner el merge por 'cliente_id' que deja solo las coincidencias
inner = pd.merge(clientes,pedidos, on='cliente_id')

# 2. guarda en izq el merge que conserva TODOS los clientes
izq = pd.merge(clientes, pedidos, on = 'cliente_id', how = 'left')

# 3. guarda en n_inner y n_izq el numero de filas de cada uno
n_inner = inner.shape[1]
n_izq = izq.shape[1]

# 4. guarda en sin_pedido cuantas filas de izq tienen el importe vacio
sin_pedido = izq.isna().sum().sum()

print(inner)
print(izq)
print(n_inner, n_izq, sin_pedido)
