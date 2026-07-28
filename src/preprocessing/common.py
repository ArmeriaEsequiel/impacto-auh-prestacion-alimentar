import pandas as pd

# Format table:
def format_df(sheet_name, general_df, top, bottom, header_position):
	df = general_df[sheet_name]
	# 1. Asignar la fila 1 como encabezado
	df.columns = df.iloc[header_position]
	# 2. Cortar el DataFrame para dejar solo los datos (de la fila 2 en adelante)
	df = df.iloc[top:bottom].reset_index(drop=True)
	df_final = df.loc[:, df.columns.notna()]
	return(df_final)