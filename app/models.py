from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Categoria(Model):
    __tablename__ = 'categoria'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255))
    activo = Column(Boolean, default=True)
    
    # Relación con ingredientes
    ingredientes = relationship('Ingrediente', backref='categoria', lazy='dynamic')

    def __repr__(self):
        return self.nombre


class Ingrediente(Model):
    __tablename__ = 'ingrediente'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    cantidad = Column(Float, nullable=False, default=0.0)
    unidad_medida = Column(String(20), nullable=False)  # Ej: kg, lt, gr, unidades
    costo_unitario = Column(Float, nullable=False, default=0.0)
    stock_minimo = Column(Float, nullable=False, default=0.0)
    fecha_vencimiento = Column(Date, nullable=True)
    activo = Column(Boolean, default=True)
    
    # Llave foránea
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=False)

    def __repr__(self):
        return f"{self.nombre} ({self.unidad_medida})"