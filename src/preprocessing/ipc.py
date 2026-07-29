def format_df_IPC(df, top, bottom, header_position, time_df, need_time):
    """
    Formatea una hoja del Excel del IPC.

    La función:
    - asigna los encabezados utilizando una fila específica,
    - elimina las filas iniciales y finales que no contienen datos,
    - elimina columnas con encabezados vacíos,
    - opcionalmente agrega la columna 'Periodo' tomada de otro DataFrame.

    Args:
        df (pd.DataFrame):
            Hoja del Excel que se desea formatear.

        top (int):
            Índice de la primera fila que contiene datos.

        bottom (int):
            Índice de la última fila que contiene datos. Puede ser negativo.

        header_position (int):
            Índice de la fila que contiene los nombres de las columnas.

        time_df (pd.DataFrame, optional):
            DataFrame del cual se copiará la primera columna para utilizarla
            como columna "Periodo".

        need_time (bool, optional):
            Indica si debe agregarse la columna "Periodo".
            Por defecto es False.

    Returns:
        pd.DataFrame:
            DataFrame limpio y listo para su análisis.
    """

    df_clean = df.copy()
    # 1. Asignar la fila header_position como encabezado
    df.iloc[5, 0] = df.iloc[4, 0]
    df.columns = df.iloc[header_position]
    # 2. Cortar el DataFrame para dejar solo los datos
    df = df.iloc[top:bottom].reset_index(drop=True)
    if need_time:
        df.insert(0, "Periodo", time_df.iloc[:, 0].values)
        df = df.loc[:, df.columns.notna()]
    return(df)