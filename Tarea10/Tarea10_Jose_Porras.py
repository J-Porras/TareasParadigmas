print("Ejericicio 1")
    
class Ciudad() :
    def __init__(self,salidaDestino,horaActual):
        self.__salidaDestino = salidaDestino
        self.__horaActual = horaActual
        
    @property
    def salidaDestino(self):
        return self.__salidaDestino
    
    @salidaDestino.setter
    def salidaDestino(self,salidaDestino):
         self.__salidaDestino = salidaDestino
         
    @property
    def horaActual(self):
        return self.__horaActual
    
    @horaActual.setter
    def horaActual(self,horaActual):
         self.__horaActual = horaActual
         
    def __str__(self):
        string = f"Salida Destino: {self.__salidaDestino } \n Hora Actual: {self.__horaActual}\n"
        return (string)

class Cliente:
    def __init(self,nombre,direccion,telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def horaActual(self,nombre):
         self.__nombre = nombre
         
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,direccion):
         self.__direccion = direccion
         
         
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,telefono):
         self.__telefono = telefono
         
    def __str__(self):
        string = f"Nombre: {self.__nombre}\n  Direccion: {self.__direccion} \n Teléfono: {self.__telefono}\n"
         
    
class BoletoAvion:
    def __init__(self,valorBoleto,impuestoSalida,horaSalida,horaLLegada,clienteNombre,clienteDireccion,
                 clienteTel,CiudadDes,CiudadSalida,HoraActual):
        self.__valorBoleto = valorBoleto
        self.__impuestoSalida = impuestoSalida
        self.__horaSalida = horaSalida
        self.__horaLlegada = horaLLegada
        self.__clienteBoleto = Cliente(clienteNombre,clienteDireccion,clienteTel)
        self.__ciudadDestino = Ciudad(CiudadDes,HoraActual)
        self.__ciudadSalida = Ciudad(CiudadSalida,HoraActual)
        
    @property
    def clienteBoleto(self):
        return self.__clienteBoleto
    
    @clienteBoleto.setter
    def clienteBoleto(self,Cliente):
         self.__clienteBoleto = Cliente
     
    @property
    def ciudadDestino(self):
        return self.__ciudadDestino
    
    @ciudadDestino .setter
    def ciudadDestino(self,ciudadDestino):
         self.__ciudadDestino = ciudadDestino 
         
    @property
    def ciudadSalida (self):
        return self.__ciudadSalida 
    
    @ciudadSalida .setter
    def ciudadSalida (self,ciudadSalida ):
         self.__ciudadSalida  = ciudadSalida 
         
    @property
    def valorBoleto(self):
        return self.__valorBoleto
    
    @valorBoleto.setter
    def valorBoleto(self,val_bol):
         self.__valorBoleto = val_bol
    
    
    @property
    def impuestoSalida(self):
        return self.__impuestoSalida
    
    @impuestoSalida.setter
    def impuestoSalida(self,imp_salida):
         self.__impuestoSalida = imp_salida
    
    @property
    def horaSalida(self):
        return self.__impuestoSalida
    
    @horaSalida.setter
    def horaSalida(self,hora_salida):
         self.__horaSalida = hora_salida
    
    @property
    def horaLLegada(self):
        return self.__horaLLegada
    
    @horaLLegada.setter
    def horaLLegada(self,hora_llegada):
         self.__horaLLegada = hora_llegada
         
    def precio_pagar(self):
        return self.__valorBoleto + self.__impuestoSalida 
    
    
    def __str__(self):
        string = ""
        titulo = "Información del boleto: \n"
        info = f"Valor Boleto: {self.__valorBoleto}\n Impuesto de Salida: {self.__impuestoSalida}\n Hora Salida: {self.__horaSalida}\n Hora Llegada: {self.__horaLlegada}\n"
        infoCliente = self.__clienteBoleto.__str__()
        infoCiudadSalida =  self.__ciudadSalida.__str__()
        infoCiudadDestino = self.__ciudadDestino.__str__()
        string = titulo + info + infoCliente+ infoCiudadSalida + infoCiudadDestino
        return (string)
    
    
#####################################################################

class AlimentoExtra:
    def __init__(self,codigo,descripcion,precio):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def horaDestino(self,codigo):
         self.__codigo = codigo

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,descripcion):
         self.__descripcion = descripcion
         
         
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,precio):
         self.__precio = precio
         
         
    def __str__(self):
        string = f"Alimento\n  Codigo: {self.__codigo} \n  Descripcion: {self.__descripcion} \n Precio: {self.__precio}\n"
        return (string)
            
        


class BoletoEjecutivo(BoletoAvion):
    def __init__(self,valorBoleto,impuestoSalida,horaSalida,horaLLegada,clienteNombre,clienteDireccion,clienteTel,CiudadDes,CiudadSalida,HoraActual,listaAlimentos):
        super().__init__(valorBoleto,impuestoSalida,horaSalida,horaLLegada,clienteNombre,clienteDireccion, clienteTel,CiudadDes,CiudadSalida,HoraActual)
        self.__listaAlimentos = listaAlimentos
    
        
    @property     
    def listaAlimentos(self):
        return self.__listaAlimentos
    
    @listaAlimentos.setter
    def listaAlimentos(self,l):
        self.__listaAlimentos = l
        
    def totalAlimentos(self):
        return sum([self.__listaAlimentos.precio for alimento in self.__listaAlimentos])
    
    def precioPagar(self):
        return self.__valorBoleto + self.__impuestoSalida + self.totalAlimentos()
        
    
    




print("- - - - - - - - - - - - - - - - - - -")    
print("Ejercicio 2")  

class Fraccion:
    def __init__(self,numerador,denominador):
        self.__numerador = numerador
        self.__denominador = denominador
        
        
    @property()
    def numerador(self):
        return self.__numerador
    
    
    @numerador.setter()
    def numerador(self,num):
         self.__numerador = num
    
    @property()
    def denominador(self):
        return self.__denominador
    
    
    @denominador.setter()
    def denominador(self,denominador):
         self.__denominador = denominador
    
    
            
        
    def __str__(self):
        return self.__numerador + "/" + self.__denominador
    
    def suma(self,f1,f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        frac = Fraccion(num,den)
        return frac.__str__()
    
    def resta(self,f1,f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        frac = Fraccion(num,den)
        return frac.__str__()
    
    
    def multiplicacion(self,f1,f2):
        frac = Fraccion(f1.numerador*f2.numerador,f1.denominador * f2.denominador)
        return frac.__str__()
    
    def division(self,f1,f2):
        num = f1.numerador * f2.denominador
        den  = f2.denominador * f2.numerador
        frac = Fraccion(num,den)
        return frac.__str__()
    
    
    
    
    
    
print("- - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("Ejercicio 3")


        
        