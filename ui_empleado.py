if categoria == "Por Kilos":
    st.markdown("### Registro de baldes (kilos):")
    cantidad_baldes = st.number_input(
        "¿Cuántos baldes deseas registrar para este producto?", min_value=1, max_value=12, value=1, step=1,
        key=f"num_baldes_{producto_seleccionado}_{fecha_carga}_{usuario}"
    )
    estados_baldes = []
    for n in range(1, cantidad_baldes + 1):
        key_balde = f"{producto_seleccionado}_balde_{n}_{fecha_carga}_{usuario}"
        # Inicializa el valor solo si no existe
        if key_balde not in st.session_state:
            st.session_state[key_balde] = "Vacío"
        opcion = st.selectbox(
            f"Estado del balde {n}",
            list(opciones_valde.keys()),
            index=list(opciones_valde.keys()).index(st.session_state[key_balde]) if st.session_state[key_balde] in opciones_valde else 0,
            key=key_balde
        )
        estados_baldes.append(opcion)

    if st.button(
        f"Actualizar {producto_seleccionado} ({categoria})",
        key=f"btn_{categoria}_{producto_seleccionado}"
    ):
        productos[producto_seleccionado] = estados_baldes.copy()
        guardar_inventario(inventario)
        guardar_historial(
            fecha_carga, usuario, categoria, producto_seleccionado, estados_baldes, modo_actualizacion
        )
        st.success(f"Actualizado. Estado actual: {', '.join(estados_baldes)}")

    st.write("Inventario actual:")
    for p, c in productos.items():
        if isinstance(c, list):
            st.write(f"- {p}: {', '.join(c)}")
        else:
            st.write(f"- {p}: {c}")
