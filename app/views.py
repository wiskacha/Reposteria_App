from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder
from .models import Categoria, Ingrediente

class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)

    # Etiquetas amigables en español
    label_columns = {
        "nombre": "Nombre de Categoría",
        "descripcion": "Descripción",
        "activo": "Estado Activo",
        "ingredientes": "Ingredientes Asociados"
    }

    # Columnas visibles en la tabla principal
    list_columns = ["nombre", "descripcion", "activo"]
    
    # Columnas permitidas en formularios de creación y edición
    add_columns = ["nombre", "descripcion", "activo"]
    edit_columns = ["nombre", "descripcion", "activo"]
    
    # Búsqueda y ordenamiento
    search_columns = ["nombre", "activo"]
    order_columns = ["nombre"]


class IngredienteView(ModelView):
    datamodel = SQLAInterface(Ingrediente)

    label_columns = {
        "nombre": "Ingrediente",
        "categoria": "Categoría",
        "cantidad": "Stock Actual",
        "unidad_medida": "Unidad",
        "costo_unitario": "Costo Unitario ($)",
        "stock_minimo": "Stock Mínimo Alerta",
        "fecha_vencimiento": "Vencimiento",
        "activo": "Disponible"
    }

    list_columns = [
        "nombre",
        "categoria",
        "cantidad",
        "unidad_medida",
        "costo_unitario",
        "stock_minimo",
        "fecha_vencimiento",
        "activo"
    ]

    add_columns = [
        "nombre",
        "categoria",
        "cantidad",
        "unidad_medida",
        "costo_unitario",
        "stock_minimo",
        "fecha_vencimiento",
        "activo"
    ]

    edit_columns = add_columns
    
    # Permitir buscar y filtrar de forma intuitiva
    search_columns = ["nombre", "categoria", "activo"]
    order_columns = ["nombre", "cantidad"]


# Registro ordenado de vistas bajo una categoría centralizada en el menú
appbuilder.add_view(
    CategoriaView,
    "Categorías",
    icon="fa-tags",
    category="Gestión de Repostería",
    category_icon="fa-birthday-cake"
)

appbuilder.add_view(
    IngredienteView,
    "Ingredientes y Stock",
    icon="fa-cubes",
    category="Gestión de Repostería"
)