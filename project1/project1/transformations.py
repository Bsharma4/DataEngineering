import logging

VALID_TYPES = [
    'cat',
    'dog',
    'mouse',
    'duck'
]

def transform_type(animal_type, locator=-1):
    animal_type = str(animal_type).lower()
    if animal_type not in VALID_TYPES:
        logging.warning(f'Animal type not recognized on row {locator}: {animal_type}')
        return 'other'
    else:
        return animal_type

def transform_breed(breed, locator=-1):
    if breed is None:
        return None
    else:
        return str(breed).lower()

def transform_name(name, locator=-1):
    if name is None:
        return None
    else:
        return str(name).title()
