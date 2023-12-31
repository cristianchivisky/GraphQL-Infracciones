from graphene import (
    ObjectType,
    Field,
    String,
    List,
    Int
)

from models.vehiculo import Vehiculo as VehiculoModel
from models.registro import Registro as RegistroModel
from models.infraccion import Infraccion as InfraccionModel
from models.objects import Vehiculo, Registro, Infraccion

class Query(ObjectType):
    all_infracciones = List(lambda: Infraccion)
    all_vehiculos = List(lambda: Vehiculo)
    all_registros = List(lambda: Registro)
    infracciones = List(lambda: Infraccion, numero_infraccion=Int(),  codigo_infraccion=String(), fecha=String(), hora=String())
    vehiculos = List(lambda: Vehiculo, patente_vehiculo=String(), anio_fabricacion=Int(), nombreyapellido_propietario=String(), domicilio_propietario=String())
    registros = List(lambda: Registro, numero_registro=Int(), nombreyapellido=String(), domicilio=String(), edad=Int(), fecha_emision=String(), fecha_vencimiento=String())
    infraccion = Field(lambda: Infraccion, numero_infraccion=Int())
    vehiculo = Field(lambda: Vehiculo, patente_vehiculo=String())
    registro = Field(lambda: Registro, numero_registro=Int())


    def resolve_all_infracciones(self, info):
        query = Infraccion.get_query(info=info)
        return query.all()

    def resolve_infracciones(self, info, numero_infraccion=None, codigo_infraccion=None, fecha=None, hora=None):
        query = Infraccion.get_query(info=info)
        if numero_infraccion:
            query = query.filter(InfraccionModel.numero_infraccion==numero_infraccion)
        if codigo_infraccion:
            query = query.filter(InfraccionModel.codigo_infraccion==codigo_infraccion)
        if fecha:
            query = query.filter(InfraccionModel.fecha==fecha)
        if hora:
            query = query.filter(InfraccionModel.hora == hora)
        return query.all()

    def resolve_infraccion(self, info, numero_infraccion):
        infraccion = InfraccionModel.query.get(numero_infraccion)
        return infraccion
    
    def resolve_all_vehiculos(self, info):
        query = Vehiculo.get_query(info=info)
        return query.all()

    def resolve_vehiculos(self, info, patente_vehiculo=None, anio_fabricacion=None, nombreyapellido_propietario=None, domicilio_propietario=None):
        query = Vehiculo.get_query(info=info)
        if patente_vehiculo:
            query = query.filter(VehiculoModel.patente_vehiculo==patente_vehiculo)
        if anio_fabricacion:
            query = query.filter(VehiculoModel.anio_fabricacion==anio_fabricacion)
        if nombreyapellido_propietario:
            query = query.filter(VehiculoModel.nombreyapellido_propietario==nombreyapellido_propietario)
        if domicilio_propietario:
            query = query.filter(VehiculoModel.domicilio_propietario==domicilio_propietario)
        return query.all()
    
    def resolve_vehiculo(self, info, patente_vehiculo):
        vehiculo = VehiculoModel.query.get(patente_vehiculo)
        return vehiculo
    
    def resolve_all_registros(self, info):
        query = Registro.get_query(info=info)
        return query.all()
    
    def resolve_registros(self, info, numero_registro=None, nombreyapellido=None, domicilio=None, edad=None, fecha_emision=None, fecha_vencimiento=None):
        query = Registro.get_query(info=info)
        if numero_registro:
            query = query.filter(RegistroModel.numero_registro==numero_registro)
        if nombreyapellido:
            query = query.filter(RegistroModel.nombreyapellido==nombreyapellido)
        if domicilio:
            query = query.filter(RegistroModel.domicilio==domicilio)
        if edad:
            query = query.filter(RegistroModel.edad==edad)
        if fecha_emision:
            query = query.filter(RegistroModel.fecha_emision==fecha_emision)
        if fecha_vencimiento:
            query = query.filter(RegistroModel.fecha_vencimiento==fecha_vencimiento)
        return query.all()

    def resolve_registro(self, info, numero_registro):
        registro = RegistroModel.query.get(numero_registro)
        return registro