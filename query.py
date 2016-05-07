"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    query = Model.query.filter(Model.year == year).all()
    output = ""
    for car in query:
        if car.brand:
            output += "\nName: {}, Brand: {}, HQ: {}".format(car.name,
                                                             car.brand.name,
                                                             car.brand.headquarters)
    print output


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()

    output = ""
    for brand in brands:
        output += "\n" + brand.name + ": "
        if brand.models:
            for model in brand.models:
                output += "\n  - " + model.name
        else:
            output += "\n  No models for this brand are listed in the database"
    print output


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# When I run the query I get this: <flask_sqlalchemy.BaseQuery object at 0x107467510>
# So, I think it returns a flask_sqlalchemy.BaseQuery object! 
# Adding .one() would return the brand object, though. 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is a table that is used between two tables that have a 
# many to many relationship. For example, a teacher has many students and a 
# student has many teachers, so an association table between the student and 
# the teacher objects would have the student id's and the teacher id's and can
# represent each unique student-teacher relationship in queries that wouldn't
# be possible using just foreign keys from the two original student and teacher
# class tables. 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Returns a list of brand objects containing the input string"""

    return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all


def get_models_between(start_year, end_year):
    """Returns a list of model objects between input years"""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
