from models import Pet
from app import db, app

#Create all tables
db.drop_all()
db.create_all()

# Make 5 Pets

Dozer = Pet(name="Bull Dozer", species="Dalmatian", age= 2, notes="Rescue", available=True)

SweetPea = Pet(name="Sweet Pea", species="Mutt", age= 2, notes="Rescue", available=True)

Dexter = Pet(name="Dexter", species="Black Labrador", age= 14, notes="Old Man Dog", available=False)

PupPup = Pet(name="Pup Pup", species="Mutt", age= 4, notes="Rescue", available=False)

Rebel = Pet(name="Rebel Scum", species="Leopard Gecko", age= 1, notes="Albino", available=True)

db.session.add_all([Dozer, SweetPea, Dexter, PupPup, Rebel])

db.session.commit()