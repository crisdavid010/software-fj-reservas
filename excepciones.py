class ErrorSoftwareFJ(Exception):
    """Clase base para los errores propios del sistema."""
    pass

class DatoInvalidoError(ErrorSoftwareFJ):
    """Cuando un dato está vacío, es negativo o no tiene el formato correcto."""
    pass

class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Cuando se intenta reservar un servicio que ya está ocupado."""
    pass

class OperacionInvalidaError(ErrorSoftwareFJ):
    """Cuando se intenta confirmar o cancelar algo que no corresponde."""
    pass