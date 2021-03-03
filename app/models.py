from app import db



attendances = db.Table(
    "attendance",
    db.Column("userID", db.String, db.ForeignKey("user.id"), primary_key=True),
    db.Column("formID", db.Integer, db.ForeingKey("form.id"), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    role = db.Column(db.String(35), unique=True, nullable=False),
    firstname = db.Column(db.String(25), nullable=False),
    lastname = db.Column(db.String(25), nullable=False),
    email = db.Column(db.String(35), nullable=False),
    phone = db.Column(db.String(35), nullable=True)

    attendances = db.relationship("Form", secondary=attendances, back_populates="users")


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(15), unique=True, nullable=False),
    sitepath = db.Column(db.String(21), unique=True, nullable=False)

    users = db.relationship("User", secondary=attendances, back_populates="attendances")