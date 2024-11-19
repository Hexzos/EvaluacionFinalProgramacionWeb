from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ""
    edad = ""
    cantidad_tarros = ""
    precio_por_tarro = 9000
    descuento = 0
    total_sin_descuento = None
    monto_descuento = None
    total_con_descuento = None

    if request.method == 'POST':

        nombre = request.form.get('nombre', '').strip()
        edad = request.form.get('edad', '').strip()
        cantidad_tarros = request.form.get('cantidad_tarros', '').strip()

        if edad.isdigit() and cantidad_tarros.isdigit():
            edad = int(edad)
            cantidad_tarros = int(cantidad_tarros)


            if 18 <= edad <= 30:
                descuento = 0.15
            elif edad > 30:
                descuento = 0.25

            total_sin_descuento = cantidad_tarros * precio_por_tarro
            monto_descuento = total_sin_descuento * descuento
            total_con_descuento = total_sin_descuento - monto_descuento

    return render_template(
        'ejercicio1.html',
        nombre=nombre,
        edad=edad,
        cantidad_tarros=cantidad_tarros,
        total_sin_descuento=total_sin_descuento,
        monto_descuento=monto_descuento,
        total_con_descuento=total_con_descuento
    )


    return render_template('ejercicio1.html', total_con_descuento=None)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }

    usuario = ""
    contrasena = ""
    mensaje = None

    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip().lower()
        contrasena = request.form.get('contrasena', '').strip()

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = f"Bienvenido administrador {usuario}"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template('ejercicio2.html', usuario=usuario, contrasena=contrasena, mensaje=mensaje)

    return render_template('ejercicio2.html', mensaje=None)

if __name__ == '__main__':
    app.run()
