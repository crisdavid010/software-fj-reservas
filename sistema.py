import logging
from modelos import Reserva
from excepciones import ErrorSoftwareFJ, OperacionInvalidaError

class SistemaSoftwareFJ:
    def __init__(self):
        self.lista_clientes = []
        self.lista_servicios = []
        self.lista_reservas = []
        logging.info("=== INICIO DEL SISTEMA SOFTWARE FJ ===")

    def agregar_cliente(self, cliente):
        try:
            for c in self.lista_clientes:
                if c.id == cliente.id:
                    raise OperacionInvalidaError(f"El cliente con ID {cliente.id} ya existe.")
        except ErrorSoftwareFJ as error:
            logging.error(f"Error al agregar cliente: {error}")
            print(f"[ERROR] {error}")
        else:
            self.lista_clientes.append(cliente)
            logging.info(f"Cliente registrado: {cliente.mostrar_info()}")
            print(f"[OK] {cliente.mostrar_info()}")
        finally:
            print("-> Proceso de cliente finalizado.\n")

    def agregar_servicio(self, servicio):
        try:
            for s in self.lista_servicios:
                if s.id == servicio.id:
                    raise OperacionInvalidaError(f"El servicio {servicio.id} ya existe.")
        except ErrorSoftwareFJ as error:
            logging.error(f"Error al agregar servicio: {error}")
            print(f"[ERROR] {error}")
        else:
            self.lista_servicios.append(servicio)
            logging.info(f"Servicio registrado: {servicio.mostrar_info()}")
            print(f"[OK] {servicio.mostrar_info()}")

    def hacer_reserva(self, id_reserva, id_cliente, id_servicio, horas, descuento=0.0):
        try:
            cliente_encontrado = None
            for c in self.lista_clientes:
                if c.id == id_cliente:
                    cliente_encontrado = c
            if cliente_encontrado is None:
                raise OperacionInvalidaError(f"No existe el cliente {id_cliente}.")

            servicio_encontrado = None
            for s in self.lista_servicios:
                if s.id == id_servicio:
                    servicio_encontrado = s
            if servicio_encontrado is None:
                raise OperacionInvalidaError(f"No existe el servicio {id_servicio}.")

            nueva_reserva = Reserva(id_reserva, cliente_encontrado, servicio_encontrado, horas)
            nueva_reserva.confirmar(descuento)

        except ErrorSoftwareFJ as error_original:
            try:
                raise OperacionInvalidaError(f"No se pudo completar la reserva {id_reserva}") from error_original
            except OperacionInvalidaError as error_encadenado:
                logging.error(f"{error_encadenado} -> Motivo: {error_encadenado.__cause__}")
                print(f"[ERROR RESERVA] {error_encadenado.__cause__}")
        else:
            self.lista_reservas.append(nueva_reserva)
            logging.info(f"Reserva exitosa: {nueva_reserva.mostrar_info()}")
            print(f"[OK RESERVA] {nueva_reserva.mostrar_info()}")
        finally:
            print(f"-> Auditoría de reserva {id_reserva} guardada.\n")