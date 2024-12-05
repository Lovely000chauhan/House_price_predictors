from pydantic import BaseModel

class Pricing(BaseModel):
    area:float
    bedrooms: int
    bathrooms:int
    stories:int
    mainroad:int
    guestroom:int
    basement:int
    airconditioning:int
    parking:int
    prefarea:int
    furnishingstatus:int
