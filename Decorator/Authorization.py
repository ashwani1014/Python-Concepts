def authorize(func):

    def wrapper():
        user_logged_in = False

        if user_logged_in:
            func()
        else:
            print("Access Denied")

    return wrapper


@authorize
def dashboard():
    print("Welcome to Dashboard")


dashboard()