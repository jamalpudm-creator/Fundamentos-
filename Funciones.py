
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 19}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 7},
            {"day": "Domingo", "temp": 11}
        ]
    ]
]

ciudades = ["Quito", "Santo Domingo", "Ambato"]

# Función def para calcular promedios de cada ciudad

def calcular_promedio_ciudades(temperaturas, ciudades):

    resultados = {}

    for ciudad_idx, ciudad in enumerate(temperaturas):
        print("\n" + "★" * 40)
        print(f"📍 Ciudad: {ciudades[ciudad_idx]}")
        print("★" * 40)

        suma_ciudad = 0
        contador_dias = 0
        promedios_semanales = []

        for semana_idx, semana in enumerate(ciudad):
            suma_semana = sum([dia["temp"] for dia in semana])                      #Calculos
            promedio_semana = suma_semana / len(semana)
            print(f"  📅 Semana {semana_idx + 1}: {promedio_semana:.2f} °C")

            # guardar promedio de la semana
            promedios_semanales.append(promedio_semana)

            # acumular para el promedio de la ciudad
            suma_ciudad += suma_semana
            contador_dias += len(semana)

        promedio_ciudad = suma_ciudad / contador_dias
        print(f"  ➡️ Promedio total de {ciudades[ciudad_idx]}: {promedio_ciudad:.2f} °C")

        resultados[ciudades[ciudad_idx]] = {
            "promedios_semanales": promedios_semanales,
            "promedio_total": promedio_ciudad
        }

    return resultados

# ==============================
# Ejecución
# ==============================
resultado = calcular_promedio_ciudades(temperaturas, ciudades)