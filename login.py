from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# define a simple (insecure) dictionary of known credentials to lookup the correct passwords for users
CREDENTIALS = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract the username and password from the request.form 
        # Use the `.get()` method because the data may not exist so to avoid errors
        # we use `.get()` which will return `None` if not present
        request_username = request.form.get('username')
        request_password = request.form.get('password')
        # Check the username is not `None` and the password is not `None` to continue
        if request_username is not None and request_password is not None:
            # See if we have the username provided in our `CREDENTIALS`, again using `get()`
            found_user = CREDENTIALS.get(request_username)
            # If `found_user` is not `None` then we know the username, so now we check the password
            if found_user is not None:
                # Get the password from `CREDENTIALS` and check it with the `request_password`
                if CREDENTIALS[request_username] == request_password:
                    # If this is true, we know the username exists and the password matches
                    # the user can login and be rewarded with cake
                    return "I should show you cake!"
        # In case we don't have one of the things above (known username, valid password) 
        # we have to show the user something. In this case, the same login page.
        # Todo: Add a helpful error message
        return render_template('login.html')
    else:
        return render_template('login.html')
