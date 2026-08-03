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


def save_csv(df, name, path):
    print(name)
    df.to_csv(path / f"{name}.csv", index=False)



def check_time(df, column):
	return(df[column].min(),df[column].max())
	
def check_time_difference(df, column):
	# Contamos la cantidad de dias que h
	diferencias = df[column].diff()

	print("Distancias detectadas entre registros (en días):")
	print(diferencias.value_counts())