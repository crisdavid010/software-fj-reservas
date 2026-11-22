import logging
from logs import iniciar_logs
from excepciones import ErrorSoftwareFJ
from modelos import Cliente, ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from sistema import SistemaSoftwareFJ

# Activar el archivo de logs
iniciar_logs()

sistema = SistemaSoftwareFJ()
print("--- INICIANDO PRUEBAS DEL SISTEMA SOFTWARE FJ ---\n")

# 1. Crear y registrar cliente válido
try:
    c1 = Cliente("C01", "Cristian Alvarez", "cristian@correo.com")
    sistema.agregar_cliente(c1)
except ErrorSoftwareFJ as e:
    logging.error(e)

# 2. Crear y registrar segundo cliente válido
try:
    c2 = Cliente("C02", "Maria Lopez", "maria@correo.com")
    sistema.agregar_cliente(c2)
except ErrorSoftwareFJ as e:
    logging.error(e)

# 3. Error al crear cliente (correo sin arroba)
try:
    c_malo = Cliente("C03", "Pedro", "pedrocorreo.com")
    sistema.agregar_cliente(c_malo)
except ErrorSoftwareFJ as e:
    logging.error(f"Validación capturada: {e}")
    print(f"[CAPTURADO] {e}\n")

# 4. Error al registrar cliente con ID repetido
try:
    c_repetido = Cliente("C01", "Otro Nombre", "otro@correo.com")
    sistema.agregar_cliente(c_repetido)
except ErrorSoftwareFJ as e:
    logging.error(e)

# 5. Registrar Servicio 1 (Sala)
s1 = ReservaSala("S01", "Sala de Juntas A", 50000, capacidad=15)
sistema.agregar_servicio(s1)

# 6. Registrar Servicio 2 (Equipo)
s2 = AlquilerEquipo("S02", "Portátil Gamer", 30000, marca="Asus")
sistema.agregar_servicio(s2)

# 7. Registrar Servicio 3 (Asesoría)
s3 = AsesoriaEspecializada("S03", "Asesoría en Python", 80000, tema="Programación")
sistema.agregar_servicio(s3)

# 8. Error al crear servicio con precio negativo
try:
    s_malo = ReservaSala("S04", "Sala Error", -20000, capacidad=5)
    sistema.agregar_servicio(s_malo)
except ErrorSoftwareFJ as e:
    logging.error(f"Servicio inválido: {e}")
    print(f"\n[CAPTURADO] {e}\n")

print("--- PROBANDO RESERVAS ---\n")

# 9. Reserva exitosa de Sala (con $10.000 de descuento)
sistema.hacer_reserva("R01", "C01", "S01", horas=3, descuento=10000)

# 10. Reserva fallida (La sala S01 ya está ocupada)
sistema.hacer_reserva("R02", "C02", "S01", horas=2)

# 11. Reserva fallida (Alquiler de equipo por 1 hora, cuando el mínimo son 2)
sistema.hacer_reserva("R03", "C02", "S02", horas=1)

# 12. Reserva exitosa de Asesoría
sistema.hacer_reserva("R04", "C02", "S03", horas=2)

# 13. Cancelar una reserva existente y liberar el servicio
try:
    reserva_a_cancelar = sistema.lista_reservas[0]
    reserva_a_cancelar.cancelar()
    logging.info(f"Reserva cancelada: {reserva_a_cancelar.mostrar_info()}")
    print(f"[CANCELADA] {reserva_a_cancelar.mostrar_info()}")
except ErrorSoftwareFJ as e:
    logging.error(e)

print("\n--- PROGRAMA TERMINADO SIN CAÍDAS ---")