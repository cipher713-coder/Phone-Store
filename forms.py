from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired, FileSize
from wtforms import StringField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    productbrand = SelectField("Product Brand", choices=[
        ("", "Select Product Brand..."),
        ("Apple", "Apple"),
        ("Samsung", "Samsung"),
        ("Xiaomi", "Xiaomi"),
        ("Google", "Google"),
        ("Oneplus", "OnePlus"),
        ("Oppo", "Oppo"),
        ("Vivo", "Vivo"),
        ("Sony", "Sony"),
    ], validators=[DataRequired()])

    devicetype = SelectField("Device Type", choices=[
        ("", "Select Device Type..."),
        ("Smartphone", "Smartphone"),
        ("Laptop", "Laptop"),
        ("TV", "TV"),
        ("Smartwatch", "Smartwatch"),
        ("Headphones", "Headphones"),
        ("Tablet", "Tablet"),
    ], validators=[DataRequired()])

    devicestorage = SelectField("Device Storage", choices=[
        ("", "Select Device Storage..."),
        ("64GB", "64GB"),
        ("128GB", "128GB"),
        ("256GB", "256GB"),
        ("512GB", "512GB"),
        ("1TB", "1TB"),
        ("2TB", "2TB"),
    ], validators=[DataRequired()])

    modelname = StringField("Model Name", validators=[DataRequired()])
    processor = StringField("Processor", validators=[DataRequired()])
    price = FloatField("Price (₾)", validators=[DataRequired()])

    profile_image = FileField("Upload Product Image", validators=[
        FileSize(max_size=10 * 1024 * 1024),
        FileAllowed(["jpg", "jpeg", "png"], "Only .jpg, .jpeg, and .png allowed"),
        FileRequired("Image file is required.")
    ])

    upload = SubmitField("Upload")



class EditUserForm(FlaskForm):
        productbrand = SelectField("Product Brand", choices=[
        ("", "Select Product Brand..."),
        ("Apple", "Apple"),
        ("Samsung", "Samsung"),
        ("Xiaomi", "Xiaomi"),
        ("Google", "Google"),
        ("Oneplus", "OnePlus"),
        ("Oppo", "Oppo"),
        ("Vivo", "Vivo"),
        ("Sony", "Sony"),
    ])

        devicetype = SelectField("Device Type", choices=[
        ("", "Select Device Type..."),
        ("Smartphone", "Smartphone"),
        ("Laptop", "Laptop"),
        ("TV", "TV"),
        ("Smartwatch", "Smartwatch"),
        ("Headphones", "Headphones"),
        ("Tablet", "Tablet"),
    ])

        devicestorage = SelectField("Device Storage", choices=[
        ("", "Select Device Storage..."),
        ("64GB", "64GB"),
        ("128GB", "128GB"),
        ("256GB", "256GB"),
        ("512GB", "512GB"),
        ("1TB", "1TB"),
        ("2TB", "2TB"),
    ])

        modelname = StringField("Model Name")
        processor = StringField("Processor")
        price = FloatField("Price (₾)")

        profile_image = FileField("Upload Product Image", validators=[
        FileSize(max_size=10 * 1024 * 1024),
        FileAllowed(["jpg", "jpeg", "png"], "Only .jpg, .jpeg, and .png allowed")
    ])

        upload = SubmitField("Save")




class SignupForm(FlaskForm):
    username = StringField("Create Your Username...", validators=[DataRequired()])

    password = PasswordField("Create New Password...", validators=[DataRequired()])

    profile_picture = FileField("Upload Profile Picture", validators=[
        FileSize(max_size=10 * 1024 * 1024),
        FileAllowed(["jpg", "jpeg", "png"], "Only .jpg, .jpeg, and .png allowed"),
        FileRequired("Image file is required.")
    ])

    upload = SubmitField("Sign Up")

class LoginForm(FlaskForm):
     username = StringField("Username", validators=[DataRequired()])
     password = PasswordField("Password", validators=[DataRequired()])
     submit = SubmitField("Log In")

class EditProfileForm(FlaskForm):
    username = StringField("Change Username")
    profile_picture = FileField("Change Profile Picture", validators=[
        FileAllowed(["jpg", "jpeg", "png"], "Only image files are allowed.")
    ])
    submit = SubmitField("Save Changes")
