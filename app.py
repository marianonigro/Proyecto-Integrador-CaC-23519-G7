# Importa las clases Flask, jsonify y request del módulo flask
from flask import Flask, jsonify, request
# Importa la clase CORS del módulo flask_cors
from flask_cors import CORS
# Importa la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow

# Crea una instancia de la clase Flask con el nombre de la aplicación
app = Flask(__name__)
# Configura CORS para permitir el acceso desde el frontend al backend
CORS(app)

# Configura la URI de la base de datos con el driver de MySQL, usuario, contraseña y nombre de la base de datos
# URI de la BD == Driver de la BD://user:password@UrlBD/nombreBD
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/proyecto"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/bookshop" # Comentar en despliegue https://marianus.pythonanywhere.com/api/productos
# Configura el seguimiento de modificaciones de SQLAlchemy a False para mejorar el rendimiento
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Crea una instancia de la clase SQLAlchemy y la asigna al objeto db para interactuar con la base de datos
db = SQLAlchemy(app)
# Crea una instancia de la clase Marshmallow y la asigna al objeto ma para trabajar con serialización y deserialización de datos
ma = Marshmallow(app)

class Producto(db.Model):  # Producto hereda de db.Model
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.BigInteger)
    titulo = db.Column(db.String(250))
    autor = db.Column(db.String(200))
    categoria = db.Column(db.String(150))
    editorial = db.Column(db.String(150))
    imagen = db.Column(db.String(400))
    precio = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)

    def __init__(self, isbn, titulo, autor, categoria, editorial, imagen, precio, cantidad):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.editorial = editorial
        self.imagen = imagen
        self.precio = precio
        self.cantidad = cantidad

# Se pueden agregar más clases para definir otras tablas en la base de datos

with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos

# Definición del esquema para la clase Producto
class ProductoSchema(ma.Schema):

    class Meta:
        fields = ("id", "isbn", "titulo", "autor", "categoria", "editorial", "imagen", "precio", "cantidad")

producto_schema = ProductoSchema()  # Objeto para serializar/deserializar un producto
productos_schema = ProductoSchema(many=True)  # Objeto para serializar/deserializar múltiples productos

@app.route('/')
def index():
    return "<h1>API Ok!!!</h1>"

@app.route("/api/productos", methods=["GET"])
def get_productos():
    """
    Endpoint para obtener todos los productos de la base de datos.

    Retorna un JSON con todos los registros de la tabla de productos.
    """
    try:
        all_productos = Producto.query.all()  # Obtiene todos los registros de la tabla de productos
        result = productos_schema.dump(all_productos)  # Serializa los registros en formato JSON
        return jsonify(result)  # Retorna el JSON de todos los registros de la tabla
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/productos/<id>", methods=["GET"])
def get_producto(id):
    """
    Endpoint para obtener un producto específico de la base de datos.

    Retorna un JSON con la información del producto correspondiente al ID proporcionado.
    """
    try:
        producto = Producto.query.get(id)  # Obtiene el producto correspondiente al ID recibido
        if producto:
            return producto_schema.jsonify(producto)  # Retorna el JSON del producto
        else:
            return jsonify({"message": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/productos/<id>", methods=["DELETE"])
def delete_producto(id):
    """
    Endpoint para eliminar un producto de la base de datos.

    Elimina el producto correspondiente al ID proporcionado y retorna un JSON con el registro eliminado.
    """
    try:
        producto = Producto.query.get(id)  # Obtiene el producto correspondiente al ID recibido
        if producto:
            db.session.delete(producto)  # Elimina el producto de la sesión de la base de datos
            db.session.commit()  # Guarda los cambios en la base de datos
            return producto_schema.jsonify(producto)  # Retorna el JSON del producto eliminado
        else:
            return jsonify({"message": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)})


    
    
# Programa Principal: Solo para uso local - Comentar en despliegue -
# Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
if __name__ == "__main__":
    app.run(debug=True, port=5000)