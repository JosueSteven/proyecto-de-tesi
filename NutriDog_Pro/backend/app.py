from unicodedata import name

from flask import Flask, request, jsonify
# Simulamos una IA de sistema experto
app = Flask(_name_) # type: ignore

@app.route('/api/generar-plan', methods=['POST'])
def generar_plan():
    data = request.json
    peso = float(data['peso'])
    objetivo = data['objetivo']
    actividad = float(data['actividad'])
    alergias = data['alergias'].lower()

    # MOTOR DE IA: Cálculo de Requerimiento Energético (RER)
    rer = 70 * (peso ** 0.75)
    
    # Ajuste dinámico según objetivo (IA de reglas)
    ajuste = {'perder': 0.8, 'mantener': 1.0, 'ganar': 1.2}
    kcal_final = round(rer * actividad * ajuste.get(objetivo, 1.0))

    # Recomendación de proteína según IA
    proteina = "Salmón" if "pollo" in alergias else "Pollo y Arroz"

    return jsonify({
        "status": "success",
        "plan_semanal": {
            "kcal_diarias": kcal_final,
            "proteina_base": proteina,
            "rutina": "Caminata de 20min" if objetivo == 'perder' else "Juego intenso"
        }
    })

if name == '_main_':
    app.run(port=5000, debug=True)