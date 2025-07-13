from ext import app
from routes import home, about, upload, edit_product, delete_product, login, logout, signup, profile, editprofile, delete_profile, load_user



app.run(debug=True, host='0.0.0.0')
