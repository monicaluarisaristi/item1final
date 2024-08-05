from . import db

class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmaceutica = db.Column(db.String(100), nullable=False)
    nombre_generico = db.Column(db.String(100), nullable=False)
    nombre_droga = db.Column(db.String(100), nullable=False)
    vencimiento = db.Column(db.String(10), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    stockminimo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Medicamento {self.nombre_generico}>'
