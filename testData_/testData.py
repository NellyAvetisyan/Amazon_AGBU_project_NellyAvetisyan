class User:
    def __init__(self, username, password):
        self.username =username
        self.password = password


# User Data

validUser = User("Nellikoko91@gmail.com", "Korea2022")
userWithInvalidPassword = User("Nellikoko91@gmail.com", "112332233")
userWithInvalidUsername = User("hhshjahja@gmail.com", "1211211")

# URLs

signInPageUrl = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
mainPageUrl = "https://www.amazon.com/"
