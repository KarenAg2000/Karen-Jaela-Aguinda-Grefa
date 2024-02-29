ciudades = 3
semanas = 4

temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 21}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 39}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 39},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

ciudades = len(temperaturas)
dias_semana = len(temperaturas[0][0])

for ciudad in range(ciudades):
    print(f"Promedio de temperaturas de cada Ciudad {ciudad + 1}:")
    for semana in range(semanas):
        suma_temperaturas = sum(dia["temp"] for dia in temperaturas[ciudad][semana])
        promedio = suma_temperaturas / dias_semana
        print(f"Semana {semana + 1}: {promedio:.2f}°C")
    print()
