#todas las funciones de carga y guardado de datos (JSON y CSV)
import json
import os
import pandas as pd
from datetime import date

INVENTARIO_FILE = "inventario_categorias.json"
HISTORIAL_FILE = "historial_inventario.csv"
DELIVERY_CATALOG_FILE = "delivery_catalog.json"
DELIVERY_VENTAS_FILE = "delivery_ventas.csv"

def cargar_inventario(productos_por_categoria):
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return json.loads(json.dumps(productos_por_categoria))

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False)

def guardar_historial(fecha, usuario, categoria, producto, cantidad, modo):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Categoría": categoria,
        "Producto": producto,
        "Cantidad": cantidad,
        "Acción": modo
    }])
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(HISTORIAL_FILE, index=False)

def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Categoría", "Producto", "Cantidad", "Acción"])

def cargar_catalogo_delivery():
    if os.path.exists(DELIVERY_CATALOG_FILE):
        with open(DELIVERY_CATALOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_catalogo_delivery(catalogo):
    with open(DELIVERY_CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False)

def guardar_venta_delivery(fecha, usuario, producto, cantidad, es_promocion):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Producto": producto,
        "Cantidad": int(cantidad),
        "Promoción": bool(es_promocion)
    }])
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(DELIVERY_VENTAS_FILE, index=False)

def cargar_ventas_delivery():
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Producto", "Cantidad", "Promoción"])
import json
import os
import pandas as pd
from datetime import date

INVENTARIO_FILE = "inventario_categorias.json"
HISTORIAL_FILE = "historial_inventario.csv"
DELIVERY_CATALOG_FILE = "delivery_catalog.json"
DELIVERY_VENTAS_FILE = "delivery_ventas.csv"

def cargar_inventario(productos_por_categoria):
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return json.loads(json.dumps(productos_por_categoria))

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False)

def guardar_historial(fecha, usuario, categoria, producto, cantidad, modo):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Categoría": categoria,
        "Producto": producto,
        "Cantidad": cantidad,
        "Acción": modo
    }])
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(HISTORIAL_FILE, index=False)

def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Categoría", "Producto", "Cantidad", "Acción"])

def cargar_catalogo_delivery():
    if os.path.exists(DELIVERY_CATALOG_FILE):
        with open(DELIVERY_CATALOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_catalogo_delivery(catalogo):
    with open(DELIVERY_CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False)

def guardar_venta_delivery(fecha, usuario, producto, cantidad, es_promocion):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Producto": producto,
        "Cantidad": int(cantidad),
        "Promoción": bool(es_promocion)
    }])
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(DELIVERY_VENTAS_FILE, index=False)

def cargar_ventas_delivery():
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Producto", "Cantidad", "Promoción"])
import json
import os
import pandas as pd
from datetime import date

INVENTARIO_FILE = "inventario_categorias.json"
HISTORIAL_FILE = "historial_inventario.csv"
DELIVERY_CATALOG_FILE = "delivery_catalog.json"
DELIVERY_VENTAS_FILE = "delivery_ventas.csv"

def cargar_inventario(productos_por_categoria):
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return json.loads(json.dumps(productos_por_categoria))

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False)

def guardar_historial(fecha, usuario, categoria, producto, cantidad, modo):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Categoría": categoria,
        "Producto": producto,
        "Cantidad": cantidad,
        "Acción": modo
    }])
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(HISTORIAL_FILE, index=False)

def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Categoría", "Producto", "Cantidad", "Acción"])

def cargar_catalogo_delivery():
    if os.path.exists(DELIVERY_CATALOG_FILE):
        with open(DELIVERY_CATALOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_catalogo_delivery(catalogo):
    with open(DELIVERY_CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False)

def guardar_venta_delivery(fecha, usuario, producto, cantidad, es_promocion):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Producto": producto,
        "Cantidad": int(cantidad),
        "Promoción": bool(es_promocion)
    }])
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(DELIVERY_VENTAS_FILE, index=False)

def cargar_ventas_delivery():
    if os.path.exists(DELIVERY_VENTAS_FILE):import json
import os
import pandas as pd
from datetime import date

INVENTARIO_FILE = "inventario_categorias.json"
HISTORIAL_FILE = "historial_inventario.csv"
DELIVERY_CATALOG_FILE = "delivery_catalog.json"
DELIVERY_VENTAS_FILE = "delivery_ventas.csv"

def cargar_inventario(productos_por_categoria):
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return json.loads(json.dumps(productos_por_categoria))

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False)

def guardar_historial(fecha, usuario, categoria, producto, cantidad, modo):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Categoría": categoria,
        "Producto": producto,
        "Cantidad": cantidad,
        "Acción": modo
    }])
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(HISTORIAL_FILE, index=False)

def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Categoría", "Producto", "Cantidad", "Acción"])

def cargar_catalogo_delivery():
    if os.path.exists(DELIVERY_CATALOG_FILE):
        with open(DELIVERY_CATALOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_catalogo_delivery(catalogo):
    with open(DELIVERY_CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False)

def guardar_venta_delivery(fecha, usuario, producto, cantidad, es_promocion):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Producto": producto,
        "Cantidad": int(cantidad),
        "Promoción": bool(es_promocion)
    }])
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(DELIVERY_VENTAS_FILE, index=False)

def cargar_ventas_delivery():
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Producto", "Cantidad", "Promoción"])import json
import os
import pandas as pd
from datetime import date

INVENTARIO_FILE = "inventario_categorias.json"
HISTORIAL_FILE = "historial_inventario.csv"
DELIVERY_CATALOG_FILE = "delivery_catalog.json"
DELIVERY_VENTAS_FILE = "delivery_ventas.csv"

def cargar_inventario(productos_por_categoria):
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return json.loads(json.dumps(productos_por_categoria))

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False)

def guardar_historial(fecha, usuario, categoria, producto, cantidad, modo):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Categoría": categoria,
        "Producto": producto,
        "Cantidad": cantidad,
        "Acción": modo
    }])
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(HISTORIAL_FILE, index=False)

def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Categoría", "Producto", "Cantidad", "Acción"])

def cargar_catalogo_delivery():
    if os.path.exists(DELIVERY_CATALOG_FILE):
        with open(DELIVERY_CATALOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_catalogo_delivery(catalogo):
    with open(DELIVERY_CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False)

def guardar_venta_delivery(fecha, usuario, producto, cantidad, es_promocion):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Producto": producto,
        "Cantidad": int(cantidad),
        "Promoción": bool(es_promocion)
    }])
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)import json
import os
import pandas as pd
from datetime import date

INVENTARIO_FILE = "inventario_categorias.json"
HISTORIAL_FILE = "historial_inventario.csv"
DELIVERY_CATALOG_FILE = "delivery_catalog.json"
DELIVERY_VENTAS_FILE = "delivery_ventas.csv"

def cargar_inventario(productos_por_categoria):
    if os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return json.loads(json.dumps(productos_por_categoria))

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(inventario, f, ensure_ascii=False)

def guardar_historial(fecha, usuario, categoria, producto, cantidad, modo):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Categoría": categoria,
        "Producto": producto,
        "Cantidad": cantidad,
        "Acción": modo
    }])
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(HISTORIAL_FILE, index=False)

def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        df = pd.read_csv(HISTORIAL_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Categoría", "Producto", "Cantidad", "Acción"])

def cargar_catalogo_delivery():
    if os.path.exists(DELIVERY_CATALOG_FILE):
        with open(DELIVERY_CATALOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_catalogo_delivery(catalogo):
    with open(DELIVERY_CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False)

def guardar_venta_delivery(fecha, usuario, producto, cantidad, es_promocion):
    nuevo = pd.DataFrame([{
        "Fecha": pd.to_datetime(str(fecha)).date(),
        "Usuario": usuario,
        "Producto": producto,
        "Cantidad": int(cantidad),
        "Promoción": bool(es_promocion)
    }])
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df = pd.concat([df, nuevo], ignore_index=True)
    else:
        df = nuevo
    df.to_csv(DELIVERY_VENTAS_FILE, index=False)

def cargar_ventas_delivery():
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Producto", "Cantidad", "Promoción"])
    else:
        df = nuevo
    df.to_csv(DELIVERY_VENTAS_FILE, index=False)

def cargar_ventas_delivery():
    if os.path.exists(DELIVERY_VENTAS_FILE):
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Producto", "Cantidad", "Promoción"])
        df = pd.read_csv(DELIVERY_VENTAS_FILE)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    return pd.DataFrame(columns=["Fecha", "Usuario", "Producto", "Cantidad", "Promoción"])
