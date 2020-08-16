"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Seed sample data 
SAMPLE_NOTES = "Doggo ipsum dat tungg tho big ol pupper pupperino wow very biscit, such treat. Blop borkdrive long bois, maximum borkdrive. Big ol very hand that feed shibe vvv long doggo, doggo ruff long water shoob h*ck, floofs bork. Such treat shibe much ruin diet the neighborhood pupper big ol doggorino puggorino yapper extremely cuuuuuute, corgo heckin good boys and girls doggorino such treat much ruin diet shoob."
IMAGE_URL_1 = "https://images.pexels.com/photos/2023384/pexels-photo-2023384.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
IMAGE_URL_2 = "https://images.pexels.com/photos/46505/swiss-shepherd-dog-dog-pet-portrait-46505.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
IMAGE_URL_3 = "https://images.pexels.com/photos/2361/nature-animal-wolf-wilderness.jpg?auto=compress&cs=tinysrgb&dpr=1&w=500"

# If table isn't empty, empty it
Pet.query.delete()

# Add User
Goodboy = Pet(name='Goodboy', species="Dog", image_url=IMAGE_URL_1, age=7, notes=SAMPLE_NOTES, available=True)
Buddyboy = Pet(name='Buddyboy', species="DogBear", image_url=IMAGE_URL_2, age=6, notes=SAMPLE_NOTES, available=False)
Bestboy = Pet(name='Bestboy', species="Wolf", image_url=IMAGE_URL_3, age=4, notes=SAMPLE_NOTES, available=True)


# Add new objects to session, so they'll persist
db.session.add(Goodboy)
db.session.add(Buddyboy)
db.session.add(Bestboy)

# Commit--otherwise, this never gets saved!
db.session.commit()
