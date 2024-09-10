def req_5(catalog, durac_inf, durac_sup, fecha_inf, fecha_sup):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    try:
        num_peliculas = 0
        duraciones = al.new_list()
        peliculas_rango = al.new_list()

        fecha_inf = dt.date.isoformat(fecha_inf)
        fecha_sup = dt.date.isoformat(fecha_sup)
        durac_inf = int(durac_inf)
        durac_sup = int(durac_sup
                    )

        for pelicula in catalog["peliculas"]["elements"]:
            if pelicula['release_date'] >= fecha_inf and pelicula['release_date'] <= fecha_sup:
                if pelicula['runtime'] >= durac_inf and pelicula['runtime'] <= durac_sup:
                    al.add_last(duraciones, pelicula['runtime'])
                    
    except Exception as exc:
        raise ' ERROR at req_5 ->:' + exc
