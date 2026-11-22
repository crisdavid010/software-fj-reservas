from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError, ServicioNoDisponibleError, OperacionInvalidaError

# Clase abstracta base
class Entidad(ABC):
    def __init__(self, id_entidad):
        if not id_entidad:
            raise DatoInvalidoError("El ID no puede estar vacío.")
        self._id = id_entidad

    @property
    def id(self):
        return self._id

    @abstractmethod
    def mostrar_info(self):
        pass


# Clase Cliente con encapsulación
class Cliente(Entidad):
    def __init__(self, id_cliente, nombre, correo):
        super().__init__(id_cliente)
        if not nombre or len(nombre) < 3:
            raise DatoInvalidoError("El nombre debe tener al menos 3 letras.")
        if "@" not in correo:
            raise DatoInvalidoError(f"El correo '{correo}' no es válido (le falta '@').")
        
        self._nombre = nombre
        self._correo = correo

    @property
    def nombre(self):
        return self._nombre

    def mostrar_info(self):
        return f"Cliente [{self._id}]: {self._nombre} ({self._correo})"


# Clase abstracta Servicio
class Servicio(Entidad, ABC):
    def __init__(self, id_servicio, nombre, precio_hora):
        super().__init__(id_servicio)
        if precio_hora <= 0:
            raise DatoInvalidoError("El precio por hora debe ser mayor a 0.")
        
        self._nombre = nombre
        self._precio_hora = precio_hora
        self.disponible = True

    @abstractmethod
    def validar_horas(self, horas):
        pass

    @abstractmethod
    def calcular_costo(self, horas, iva=0.19, descuento=0.0):
        pass

    def mostrar_info(self):
        estado = "Libre" if self.disponible else "Ocupado"
        return f"Servicio [{self._id}]: {self._nombre} - ${self._precio_hora}/hora ({estado})"


# Servicio 1: Reserva de Salas
class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, precio_hora, capacidad):
        super().__init__(id_servicio, nombre, precio_hora)
        if capacidad <= 0:
            raise DatoInvalidoError("La capacidad de la sala debe ser mayor a 0.")
        self.capacidad = capacidad

    def validar_horas(self, horas):
        if horas < 1 or horas > 10:
            raise OperacionInvalidaError("Las salas se reservan mínimo 1 hora y máximo 10 horas.")

    def calcular_costo(self, horas, iva=0.19, descuento=0.0):
        self.validar_horas(horas)
        subtotal = self._precio_hora * horas
        total = (subtotal - descuento) * (1 + iva)
        if total <= 0:
            raise DatoInvalidoError("El costo total no puede ser cero o negativo.")
        return round(total, 2)


# Servicio 2: Alquiler de Equipos
class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, precio_hora, marca):
        super().__init__(id_servicio, nombre, precio_hora)
        if not marca:
            raise DatoInvalidoError("Debe indicar la marca del equipo.")
        self.marca = marca

    def validar_horas(self, horas):
        if horas < 2:
            raise OperacionInvalidaError("El alquiler de equipos requiere mínimo 2 horas.")

    def calcular_costo(self, horas, iva=0.19, descuento=0.0):
        self.validar_horas(horas)
        subtotal = (self._precio_hora * horas) + 10000  # Seguro fijo de $10.000
        total = (subtotal - descuento) * (1 + iva)
        return round(total, 2)


# Servicio 3: Asesoría Especializada
class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio, nombre, precio_hora, tema):
        super().__init__(id_servicio, nombre, precio_hora)
        if not tema:
            raise DatoInvalidoError("Debe indicar el tema de la asesoría.")
        self.tema = tema

    def validar_horas(self, horas):
        if horas <= 0:
            raise OperacionInvalidaError("Las horas de asesoría deben ser mayores a 0.")

    def calcular_costo(self, horas, iva=0.19, descuento=0.0):
        self.validar_horas(horas)
        subtotal = self._precio_hora * horas
        total = (subtotal - descuento) * (1 + iva)
        return round(total, 2)


# Clase Reserva
class Reserva(Entidad):
    def __init__(self, id_reserva, cliente, servicio, horas):
        super().__init__(id_reserva)
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "PENDIENTE"
        self.total_pagar = 0

    def confirmar(self, descuento=0.0):
        if self.estado != "PENDIENTE":
            raise OperacionInvalidaError("Esta reserva ya fue procesada anteriormente.")
        if not self.servicio.disponible:
            raise ServicioNoDisponibleError(f"El servicio {self.servicio.id} no está disponible.")

        self.total_pagar = self.servicio.calcular_costo(self.horas, descuento=descuento)
        self.estado = "CONFIRMADA"
        self.servicio.disponible = False

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise OperacionInvalidaError("La reserva ya estaba cancelada.")
        if self.estado == "CONFIRMADA":
            self.servicio.disponible = True
        self.estado = "CANCELADA"

    def mostrar_info(self):
        return (f"Reserva [{self._id}] | Estado: {self.estado} | "
                f"Cliente: {self.cliente.nombre} | Servicio: {self.servicio.id} | "
                f"Total: ${self.total_pagar}")