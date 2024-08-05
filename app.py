from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import  request, redirect, url_for, flash
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Medicamento(db.Model):
    __tablename__ = "medicamentos"
    id = db.Column(db.Integer, primary_key=True)
    farmaceutica = db.Column(db.String(100), nullable=False)
    nombre_generico = db.Column(db.String(100), nullable=False)
    nombre_droga = db.Column(db.String(100), nullable=False)
    vencimiento = db.Column(db.String(10), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    stockminimo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Medicamento {self.nombre_generico}>' # Importa aquí después de inicializar db

@app.route('/')
def index():
    medicamentos = Medicamento.query.all()
    return render_template('index.html', medicamentos=medicamentos)

@app.route('/add', methods=['GET', 'POST'])
def add_medicamento():
    if request.method == 'POST':
        farmaceutica = request.form['farmaceutica']
        nombre_generico = request.form['nombre_generico']
        nombre_droga = request.form['nombre_droga']
        vencimiento = request.form['vencimiento']
        cantidad = request.form['cantidad']
        stockminimo = request.form['stockminimo']
        
        nuevo_medicamento = Medicamento(
            farmaceutica=farmaceutica,
            nombre_generico=nombre_generico,
            nombre_droga=nombre_droga,
            vencimiento=vencimiento,
            cantidad=cantidad,
            stockminimo=stockminimo
        )
        
        db.session.add(nuevo_medicamento)
        db.session.commit()
        flash('Medicamento agregado correctamente.', 'success')
        return redirect(url_for('index'))

    return render_template('add_edit_medicamento.html', medicamento=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_medicamento(id):
    medicamento = Medicamento.query.get_or_404(id)
    if request.method == 'POST':
        medicamento.farmaceutica = request.form['farmaceutica']
        medicamento.nombre_generico = request.form['nombre_generico']
        medicamento.nombre_droga = request.form['nombre_droga']
        medicamento.vencimiento = request.form['vencimiento']
        medicamento.cantidad = request.form['cantidad']
        medicamento.stockminimo = request.form['stockminimo']
        db.session.commit()
        flash('Medicamento actualizado correctamente.', 'success')
        return redirect(url_for('index'))

    return render_template('add_edit_medicamento.html', medicamento=medicamento)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_medicamento(id):
    medicamento = Medicamento.query.get_or_404(id)
    db.session.delete(medicamento)
    db.session.commit()
    flash('Medicamento eliminado correctamente.', 'success')
    return redirect(url_for('index'))

@app.route('/medicamento/<int:id>')
def medicamento_detail(id):
    medicamento = Medicamento.query.get_or_404(id)
    return render_template('medicamento_detail.html', medicamento=medicamento)

if __name__ == "__main__":
    app.run(debug=True)
