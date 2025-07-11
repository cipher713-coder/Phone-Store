from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from functools import wraps
from werkzeug.security import check_password_hash
from ext import app, db, login_manager
from models import Product, Signup
from forms import UploadForm, EditUserForm, SignupForm, LoginForm, EditProfileForm
from os import path

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash("You don't have permission to access this page.", "danger")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function



UPLOAD_FOLDER = path.join(app.root_path, "static")

@app.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)

@app.route("/about/<int:product_id>")
def about(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("about.html", product=product)

@app.route("/upload", methods=["GET", "POST"])
@login_required
@admin_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.profile_image.data
        filename = secure_filename(file.filename)
        file.save(path.join(UPLOAD_FOLDER, filename))

        new_product = Product(
            productbrand=form.productbrand.data,
            devicetype=form.devicetype.data,
            devicestorage=form.devicestorage.data,
            modelname=form.modelname.data,
            processor=form.processor.data,
            price=form.price.data,
            profile_image=filename
        )

        db.session.add(new_product)
        db.session.commit()
        flash("Product uploaded successfully!", "success")
        return redirect(url_for("home"))

    return render_template("upload.html", form=form)

@app.route("/editproduct/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = EditUserForm(productbrand = product.productbrand, devicetype = product.devicetype, devicestorage = product.devicestorage, modelname = product.modelname, processor = product.processor, price = product.price)


    if form.validate_on_submit():
        product.productbrand = form.productbrand.data
        product.devicetype = form.devicetype.data
        product.devicestorage = form.devicestorage.data
        product.modelname = form.modelname.data
        product.processor = form.processor.data
        product.price = form.price.data

        if form.profile_image.data:
            file = form.profile_image.data
            filename = secure_filename(file.filename)
            file.save(path.join(UPLOAD_FOLDER, filename))
            product.profile_image = filename

        db.session.commit()
        flash("Product updated successfully!", "success")
        return redirect(url_for("about", product_id=product.id))

    return render_template("editproduct.html", form=form, product=product)

@app.route("/deleteproduct/<int:product_id>", methods=["POST"])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted successfully.", "info")
    return redirect(url_for("home"))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Signup.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("home"))
        flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("home"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        file = form.profile_picture.data
        filename = secure_filename(file.filename)
        file.save(path.join(UPLOAD_FOLDER, filename))

        # Set role based on whether this is the first user
        if Signup.query.count() == 0:
            assigned_role = 'admin'
        else:
            assigned_role = 'user'

        new_user = Signup(
            username=form.username.data,
            profile_picture=filename,
            role=assigned_role
        )
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for("login"))

    return render_template("signup.html", form=form)

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@app.route("/editprofile", methods=["GET", "POST"])
@login_required
def editprofile():
    form = EditProfileForm(current_user = current_user.username)

    if form.validate_on_submit():
        current_user.username = form.username.data

        if form.profile_picture.data:
            file = form.profile_picture.data
            filename = secure_filename(file.filename)
            file.save(path.join(UPLOAD_FOLDER, filename))
            current_user.profile_picture = filename

        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for("profile"))

    return render_template("editprofile.html", form=form, user=current_user)

@app.route("/deleteprofile", methods=["POST"])
@login_required
def delete_profile():
    db.session.delete(current_user)
    db.session.commit()
    flash("Your profile has been deleted.", "success")
    logout_user()
    return redirect(url_for("home"))





@login_manager.user_loader
def load_user(user_id):
    return Signup.query.get(int(user_id))