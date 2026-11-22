# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

Proyecto desarrollado para la Fase 4 del curso **Programación (213023)** - UNAD (ECBTI).

## Descripción
Aplicación orientada a objetos desarrollada en Python sin uso de bases de datos. Gestiona clientes, servicios (salas, equipos y asesorías) y reservas mediante listas en memoria, aplicando herencia, polimorfismo, encapsulación y manejo avanzado de excepciones con registro en archivos de log.

## Estructura del Proyecto
- `excepciones.py`: Jerarquía de excepciones personalizadas.
- `logs.py`: Configuración del archivo `registro_sistema.log`.
- `modelos.py`: Clases abstractas (`Entidad`, `Servicio`) y concretas (`Cliente`, `ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`, `Reserva`).
- `sistema.py`: Controlador principal con bloques `try/except/else/finally` y encadenamiento de excepciones.
- `main.py`: Simulación de 13 operaciones (válidas y con errores controlados).

## Ejecución
```bash
python main.py

Cristian David Alvarez Quiroz - Ingeniería de Sistemas, UNAD.