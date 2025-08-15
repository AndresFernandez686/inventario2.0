# UI y lógica de empleados (Inventario, delivery)
import streamlit as st
from datetime import date
from utils import df_to_csv_bytes

def empleado_inventario_ui(inventario, usuario, opciones_valde, guardar_inventario, guardar_historial):
    st.header("Inventario")
    fecha_carga = st.date_input("Selecciona la fecha de carga", value=date.today(), key="fecha_inv")

    tabs = st.tabs(list(inventario.keys()))
    for i, categoria in enumerate(inventario.keys()):
        with tabs[i]:
            productos = inventario[categoria]
            producto_seleccionado = st.selectbox(
                f"Producto de {categoria}",
                list(productos.keys()),
                key=f"sel_{categoria}"
            )

            modo_actualizacion = st.radio(
                "¿Deseas añadir a la cantidad existente o reemplazarla?",
                ("Añadir", "Reemplazar"),
                key=f"modo_{categoria}_{producto_seleccionado}"
            )

            if categoria == "Por Kilos":
                st.markdown("### Estado de hasta 6 baldes:")
                estados_baldes = []
                for n in range(1, 7):
                    key_balde = f"{producto_seleccionado}_balde_{n}_{fecha_carga}_{usuario}"
                    # Inicializa el valor solo si no existe
                    if key_balde not in st.session_state:
                        valor_guardado = None
                        if isinstance(productos[producto_seleccionado], list) and len(productos[producto_seleccionado]) >= n:
                            valor_guardado = productos[producto_seleccionado][n-1]
                        st.session_state[key_balde] = valor_guardado if valor_guardado is not None else "Vacío"
                    opcion = st.selectbox(
                        f"Balde {n}",
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
                        # Solo muestra "Vacío" si fue seleccionado explícitamente
                        seleccionados = [x for x in c if x != "Vacío" or c.count("Vacío") > 0]
                        # Pero solo mostramos "Vacío" si el usuario explícitamente lo eligió en algún balde
                        # (en la práctica, esto ya pasa con el filtro anterior, pero lo dejamos claro)
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
                        fecha_carga, usuario, categoria, producto_seleccionado, cantidad, modo_actualizacion
                    )
                    st.success(f"Actualizado. Nuevo stock: {productos[producto_seleccionado]}")

                st.write("Inventario actual:")
                for p, c in productos.items():
                    st.write(f"- {p}: {c if c > 0 else 'Vacío'}")

def empleado_delivery_ui(usuario, cargar_catalogo_delivery, guardar_venta_delivery, cargar_ventas_delivery):
    st.header("Delivery")
    catalogo = cargar_catalogo_delivery()
    activos = [item for item in catalogo if item.get("activo", True)]

    if not activos:
        st.info("No hay productos de delivery activos. Pide al administrador que agregue opciones.")
        return

    fecha_venta = st.date_input("Fecha de la venta", value=date.today(), key="fecha_deliv")
    opciones = [f"{it['nombre']} {'(PROMO)' if it.get('es_promocion', False) else ''}" for it in activos]
    seleccion = st.selectbox("Producto de delivery", opciones)
    idx = opciones.index(seleccion)
    item_sel = activos[idx]
    cantidad = st.number_input("Cantidad vendida", min_value=1, step=1)

    if st.button("Registrar venta de delivery"):
        guardar_venta_delivery(
            fecha_venta,
            usuario,
            item_sel["nombre"],
            cantidad,
            item_sel.get("es_promocion", False)
        )
        st.success("Venta registrada con éxito ✅")

    ventas = cargar_ventas_delivery()
    if not ventas.empty:
        ventas_hoy = ventas[(ventas["Usuario"] == usuario) & (ventas["Fecha"].dt.date == date.today())]
        if not ventas_hoy.empty:
            st.subheader("Tus ventas de delivery hoy")
            st.dataframe(ventas_hoy)
