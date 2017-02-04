"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# flask_sqlalchemy.BaseQuery (It's a query object)


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is one that doesn't contain any information of it's own,
# it's purpose is to connect two tables that would otherwise have a many to many relationship. 
# With the association table, you now have two many to one relationships instead of 
# a many to many relationship.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = "your query here"
# ram_cars = db.session.query(Brand.name).filter(Brand.brand_id == 'ram').all()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "your query here"
# cvt = db.session.query(Model.name).filter(Model.brand_id == 'che', Model.name == 'Corvette').all()

#You could also add distinct.() if you only want to see the result one time.
# I didn't do that here since I was a bit confused by the wording of the question
# to include All models with the name Corvette, but the query could easily be 
# modified if you only wanted to see the distinct model name once


# Get all models that are older than 1960.
q3 = "your query here"
# older_models = db.session.query(Model.name).filter(Brand.founded < 1960).distinct().all()



# Get all brands that were founded after 1920.
q4 = "your query here"
# after_1920 = db.session.query(Brand.name).filter(Brand.founded > 1920).distinct().all()



# Get all models with names that begin with "Cor."
q5 = "your query here"
# Cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# also:
# Cr_mdls = db.session.query(Model.name).filter(Model.name.like('Cor%')).all()

# The first gives you a list of object repr's and the second gives you a list of model names


# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = "your query here"

# yr3 = db.session.query(Brand.name).filter(Brand.founded == 1903)
# yr3.filter(Brand.discontinued == None).all()

# I also tried chaining them together and that worked, as well:
# old_running = db.session.query(Brand.name).filter(Brand.founded == 1903, Brand.discontinued == None).all()

# In [34]: print yr3
# [(u'Ford',), (u'Buick',)]


# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = "your query here"

# old_disc = db.session.query(Brand.name).filter(db.or_(Brand.founded < 1950, Brand.discontinued != None)).all()



# Get any model whose brand_id is not "for."
q8 = "your query here"

# db.session.query(Model.name).filter(Model.brand_id != 'for').all()

# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    results = db.session.query(Model.name, Brand.name, Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for model, brand, hq in results:
        print model, brand, hq

   
get_model_info(1955)

def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    results = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()
    
    for brand, model, year in results:
        print brand, model, year

get_brands_summary()

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    results = db.session.query(Brand).filter(Brand.name.like(mystr)).all()

    return results

search_brands_by_name('Chev%')

#I wasn't sure how to build the % into the query instead of passing them through
# as part of the argument. I kept getting a syntax error when I tried to include
# them within the function


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    results = db.session.query(Model).filter(Model.year >= start_year, Model.year < end_year).all()

    return results

get_models_between(1903, 1955)

