import math

class MotorIA:
    def __init__(self):
        # Base de conocimientos: Ingredientes prohibidos por la IA
        self.prohibidos = ["Chocolate", "Cebolla", "Uvas", "Xilitol", "Ajo"]

    def calcular_plan(self, datos_perro):
        """
        Inferencia Lógica para generar planes de 7 días.
        Argumentos: peso, actividad, objetivo, alergias.
        """
        peso = float(datos_perro['peso'])
        actividad = float(datos_perro['actividad'])
        objetivo = datos_perro['objetivo']
        alergias = datos_perro['alergias'].lower()

        # 1. Algoritmo RER (Requerimiento Energético en Reposo)
        # Fórmula científica: 70 * (peso ^ 0.75)
        rer = 70 * math.pow(peso, 0.75)

        # 2. Lógica de Ajuste por Objetivo (Pilar 3 del proyecto)
        # Ajuste dinámico de calorías según el objetivo de la mascota
        if objetivo == "perder":
            multiplicador = actividad * 0.8  # Déficit calórico
        elif objetivo == "ganar":
            multiplicador = actividad * 1.2  # Superávit para masa muscular
        else:
            multiplicador = actividad        # Mantenimiento

        kcal_diarias = round(rer * multiplicador)

        # 3. Motor de Recomendación Dinámica de Recetas
        receta = self._seleccionar_receta(alergias)
        
        # 4. Generación de Rutina (Actividad Física)
        rutina = self._generar_rutina(objetivo)

        return {
            "kcal_diarias": kcal_diarias,
            "plan_semanal_kcal": kcal_diarias * 7,
            "receta_sugerida": receta,
            "rutina_ejercicios": rutina,
            "advertencia_ia": f"Evitar estrictamente: {', '.join(self.prohibidos)}"
        }

    def _seleccionar_receta(self, alergias):
        if "pollo" in alergias:
            return "Dieta Hipoalergénica: Cordero con arroz integral y calabaza."
        if "granos" in alergias or "gluten" in alergias:
            return "Dieta Grain-Free: Salmón con camote y espinacas."
        return "Plan Estándar: Pollo magro, zanahoria, guisantes y arroz."

    def _generar_rutina(self, objetivo):
        if objetivo == "perder":
            return "Cardio: 40 min de caminata rápida y 10 min de juego con pelota."
        if objetivo == "ganar":
            return "Fuerza: Ejercicios de tracción (tug-of-war) y caminata en subida."
        return "Salud: 20 min de trote suave y ejercicios de olfato."