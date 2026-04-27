// 1. CONFIGURACIÓN INICIAL Y GRÁFICOS (Chart.js)
let weightChart;

document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('weightChart').getContext('2d');
    
    // Inicializamos un gráfico vacío para el progreso del peso
    weightChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
            datasets: [{
                label: 'Peso del Perrito (Kg)',
                data: [12.5, 12.2, 11.8, 11.5], // Datos de ejemplo
                borderColor: '#2563eb',
                backgroundColor: 'rgba(37, 99, 235, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            }
        }
    });
});

// 2. LÓGICA DE ROLES (VETERINARIO VS DUEÑO)
function toggleRole() {
    const body = document.body;
    const label = document.getElementById('role-label');
    
    if (body.classList.contains('user-view')) {
        body.classList.remove('user-view');
        body.classList.add('admin-view');
        label.innerText = "MODO: VETERINARIO (ADMIN)";
        alert("Cambiando a Panel Clínico: Acceso a expedientes de pacientes.");
    } else {
        body.classList.remove('admin-view');
        body.classList.add('user-view');
        label.innerText = "MODO: DUEÑO";
    }
}

// 3. MOTOR DE LA IA (GENERACIÓN DE PLAN SEMANAL)
async function generarPlanIA() {
    // Captura de datos del formulario
    const nombre = document.getElementById('p_nombre').value;
    const peso = parseFloat(document.getElementById('p_peso').value);
    const objetivo = document.getElementById('p_objetivo').value;
    const actividad = parseFloat(document.getElementById('p_actividad').value);
    const alergias = document.getElementById('p_alergias').value.toLowerCase();

    if (!nombre || !peso) {
        alert("Por favor, completa los datos básicos del perrito.");
        return;
    }

    // SIMULACIÓN DE PROCESAMIENTO IA (Lógica de Inferencia)
    // Fórmula RER: 70 * (peso)^0.75
    const rer = 70 * Math.pow(peso, 0.75);
    
    // Factor de ajuste por objetivo
    let factor = actividad;
    if (objetivo === 'perder') factor *= 0.85; // Reducción calórica segura
    if (objetivo === 'ganar') factor *= 1.20;  // Superávit para masa muscular

    const kcalDiarias = Math.round(rer * factor);

    // Lógica de Recomendaciones Dinámicas
    let receta = "";
    let rutina = "";

    // IA: Selección de proteína según alergias
    if (alergias.includes("pollo") || alergias.includes("aves")) {
        receta = "Proteína Hidrolizada o Salmón con camote al vapor.";
    } else if (alergias.includes("granos") || alergias.includes("arroz")) {
        receta = "Dieta 'Grain-Free': Carne de res magra con espinacas y zanahoria.";
    } else {
        receta = "Mix balanceado: Pechuga de pollo, arroz integral y un toque de aceite de coco.";
    }

    // IA: Selección de rutina según objetivo y actividad
    switch(objetivo) {
        case 'perder':
            rutina = "Ciclo de quema: 45 min de caminata a paso constante + juegos de cobro (pelota).";
            break;
        case 'ganar':
            rutina = "Fortalecimiento: Ejercicios de propiocepción y 15 min de arrastre de peso ligero.";
            break;
        default:
            rutina = "Mantenimiento: 20 min de trote suave y estimulación mental (alfombra de olfato).";
    }

    // MOSTRAR RESULTADOS EN EL DASHBOARD
    document.getElementById('ai-plan').classList.remove('hidden');
    document.getElementById('recipe-content').innerHTML = `
        <strong>Calorías:</strong> ${kcalDiarias} kcal/día<br>
        <strong>Sugerencia:</strong> ${receta}
    `;
    document.getElementById('activity-content').innerText = rutina;
    
    document.getElementById('ia-status').innerHTML = `
        <span style="color: green">● IA Activa</span><br>
        Plan generado para <b>${nombre}</b><br>
        Objetivo: ${objetivo.toUpperCase()}
    `;

    // Actualizar gráfico con el peso actual para mostrar el "Hoy"
    updateChart(peso);
    
    // Desplazar suavemente hacia el plan
    document.getElementById('ai-plan').scrollIntoView({ behavior: 'smooth' });
}

// 4. ACTUALIZACIÓN DINÁMICA DE GRÁFICOS
function updateChart(nuevoPeso) {
    weightChart.data.datasets[0].data.push(nuevoPeso);
    weightChart.data.labels.push('Hoy');
    weightChart.update();
}