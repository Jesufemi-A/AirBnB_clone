#!/usr/bin/python3
"""
Contains class Place
"""

from base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    amenity_ids = [""]
