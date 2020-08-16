from flask import Flask, render_template, redirect, flash, session
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
""" Pets application """

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "gettimjiggywithit9999999"
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG'] = True

connect_db(app)
db.create_all()

# homepage routes ##########################################################################

@app.route('/')
def root():
    """Show recent list of Pets, most-recent first."""
    pets = Pet.query.all()
    return render_template("/homepage.html", pets=pets)

@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""

    return render_template('404.html'), 404

# pet routes ###############################################################################
@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ add pet form """
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        age = form.age.data
        notes = form.notes.data
        flash(f"Added {name} the {species}")

        new_pet = Pet(name=name, species=species, image_url=image_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template(
            "add.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/')

    else:
        # failed; re-present form for editing
        return render_template("pet_edit.html", form=form, pet=pet)

