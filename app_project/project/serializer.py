import datetime

class ResourceSerializer:
    @staticmethod
    def serialize_trayecto_creado(resource) -> dict:
        return {
            "id": resource.id,
            "createAt": datetime.date.isoformat(resource.createAt),
            "expireAt": datetime.date.isoformat(resource.createAt + datetime.timedelta(30))
        }
    
    @staticmethod
    def serialize_trayecto_encontrado(resource) -> dict:
        return {
            "id": resource.id,
            "sourceAirportCode": resource.sourceAirportCode,
            "sourceCountry": resource.sourceCountry,
            "destinyAirportCode": resource.destinyAirportCode,
            "destinyCountry": resource.destinyCountry,
            "bagCost": resource.bagCost,
            "createAt": datetime.date.isoformat(resource.createAt),
            "expireAt": datetime.date.isoformat(resource.createAt + datetime.timedelta(30))
        }
