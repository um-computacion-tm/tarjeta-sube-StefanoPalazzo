import unittest


PRIMARIO = 'estudiante_primario'
SECUNDARIO = 'estudiante_secundario'
UNIVERSITARIO = 'estudiante_universitario'
JUBILADO = 'jubilado'
PRECIO_TICKET = 70
ACTIVADO = 'activado'
DESACTIVADO = 'desactivado'

DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}


class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

class Sube():
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = "activado"

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == None:
            return PRECIO_TICKET
        else: 
            return int(PRECIO_TICKET - PRECIO_TICKET*(DESCUENTOS[self.grupo_beneficiario]/100))
            

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        if self.grupo_beneficiario == None:
            if self.saldo < self.obtener_precio_ticket():
                raise NoHaySaldoException()
            else:
                self.saldo -= self.obtener_precio_ticket()
           
        else: 
            if self.saldo < self.obtener_precio_ticket():
                raise NoHaySaldoException()
            else:
                self.saldo -= self.obtener_precio_ticket()

    def cambiar_estado(self,nuevoEstado):
        if nuevoEstado == ACTIVADO or nuevoEstado == DESACTIVADO:
            self.estado = nuevoEstado
        else:
            raise EstadoNoExistenteException()
        
    




if __name__ == '__main__':
    unittest.main()