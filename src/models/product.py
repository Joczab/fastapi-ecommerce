import json
import logging
from pathlib import Path

# Preparar logger para poder ver los logs en el servidor
logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

# Obtener ruta ABSOLUTA de nuestro json que funciona como db
DB_PATH = Path(__file__).resolve().parent.parent / 'db' / 'mock.json'


def read_db() -> dict | None:
    """Leer archivo JSON que funciona como base de datos"""
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        logger.debug(str(e))
        return None
    

def write_db(data: dict):
    """Actualizar JSON que funciona como base de datos"""
    try:
        with open(DB_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        logger.debug(str(e))
        return None
    

def get_products():
    """Obtener todos los productos"""
    try:
        return read_db()['products']
    except Exception as e:
        logger.debug(str(e))
        return None
    

def create_product(new_product: dict):
    """Crear nuevo producto"""
    try:
        db = read_db()
        products = db['products']

        # Generar nuevo id
        new_id = max((p['id'] for p in products), default=0) + 1

        # Spread operator (pasar las propiedades de un objeto a otro)
        product = {'id': new_id, **new_product, 'is_active': True}

        # Insertar nuevo producto a la lista
        products.append(product)

        # Actualizar database
        write_db(db)
        return product
    except Exception as e:
        logger.debug(str(e))
        return None

    
def update_product(product_id: int, changes: dict) -> dict:
    """Actualizar solo los campos del producto que llegan desde la peticion"""
    try:
        db = read_db()
        
        for product in db['products']:
            if product['id'] == product_id:
                product.update(changes)
                write_db(db)
                return product
    except Exception as e:
        logger.debug(str(e))
        return None
    

def delete_product(product_id: int):
    """Eliminar producto"""
    try:
        db = read_db()
        products = db['products']

        # Filtrar los productos que tengan el id diferente del que queremos eliminar
        remaining = [p for p in products if p['id'] != product_id]

        # Verificamos si hubo o no eliminacion de productos, si no hubo entonces las longitudes son iguales
        if len(remaining) == len(products):
            return False
        
        db['products'] = remaining
        write_db(db)

        return {'message': 'Producto eliminado'}
    except Exception as e:
        logger.debug(str(e))
        return None
    