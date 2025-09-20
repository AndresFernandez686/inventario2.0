import streamlit as st
from datetime import date

def empleado_inventario_ui(inventario, usuario, opciones_valde, guardar_inventario, guardar_historial):
    st.header("Inventario")
    for categoria, productos in inventario.items():
        st.subheader(categoria)
        productos = productos.copy()
        for producto_seleccionado in productos.keys():
            modo_actualizacion = st.radio(
                f"Modo de actualización para {producto_seleccionado}",
                options=["Añadir", "Reemplazar"],
                key=f"modo_{categoria}_{producto_seleccionado}",
                horizontal=True
            )
            estados_baldes = []
            if categoria == "Helados":
                cantidad = st.number_input(
                    f"Cantidad de baldes para {producto_seleccionado}",
                    min_value=0, step=1, key=f"baldes_{categoria}_{producto_seleccionado}"
                )
                for i in range(int(cantidad)):
                    estado = st.selectbox(
                        f"Estado del balde {i+1} para {producto_seleccionado}",
                        options=list(opciones_valde.values()),
                        key=f"estado_{categoria}_{producto_seleccionado}_{i}"
                    )
                    estados_baldes.append(estado)
                if st.button(
                    f"Actualizar {producto_seleccionado} ({categoria})",
                    key=f"btn_{categoria}_{producto_seleccionado}"
                ):
                    productos[producto_seleccionado] = estados_baldes
                    guardar_inventario(inventario)
                    guardar_historial(
                        date.today(), usuario, categoria, producto_seleccionado, estados_baldes, modo_actualizacion
                    )
                    st.success(f"Actualizado. Estado actual: {', '.join(estados_baldes)}")
                st.write("Inventario actual:")
                for p, c in productos.items():
                    if isinstance(c, list):
                        seleccionados = [x for x in c if x != "Vacío" or c.count("Vacío") > 0]
                        seleccionados = [x for i, x in enumerate(c) if x != "Vacío" or (x == "Vacío" and c[i] == "Vacío")]
                        if seleccionados:
                            st.write(f"- {p}: {', '.join([x for x in c if x != 'Vacío'] + ([x for x in c if x == 'Vacío'] if any(x == 'Vacío' for x in c) else []))}")
                        else:
                            st.write(f"- {p}: ")
                    else:
                        st.write(f"- {p}: {c}")
            else:
                cantidad = st.number_input("Cantidad (unidades)", min_value=0, step=1, key=f"cant_{categoria}_{producto_seleccionado}")
                if st.button(
                    f"Actualizar {producto_seleccionado} ({categoria})",
                    key=f"btn_{categoria}_{producto_seleccionado}"
                ):
                    cantidad = max(0, int(cantidad))
                    if modo_actualizacion == "Añadir":
                        productos[producto_seleccionado] += cantidad
                    else:
                        productos[producto_seleccionado] = cantidad
                    guardar_inventario(inventario)
                    guardar_historial(
                        date.today(), usuario, categoria, producto_seleccionado, cantidad, modo_actualizacion
                    )
                    st.success(f"Actualizado. Nuevo stock: {productos[producto_seleccionado]}")

                st.write("Inventario actual:")
                for p, c in productos.items():
                    st.write(f"- {p}: {c if c > 0 else 'Vacío'}")
