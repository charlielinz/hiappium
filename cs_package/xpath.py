a = "/android.widget.FrameLayout"
b = "/android.widget.LinearLayout"
c = "/android.view.ViewGroup"
homepage_short = (
    "/hierarchy" + a + b + a + b + a + a + c + c + c + c + c + c + c + c + "[2]" + c
)
accountpage_short = (
    "/hierarchy" + a + b + a + b + a + a + c + c + c + c + "[2]" + c + c + c + c
)
sign_up_short = (
    "/hierarchy" + a + b + a + b + a + a + c + c + c + c + "[2]" + c + "[2]" + c + c + "[1]"
)
sign_in_short = (
    "/hierarchy" + a + b + a + b + a + a + c + c + c + c + "[2]" + c + "[2]" + c + c + "[1]"
)

HOMEPAGE_XPATH = {
    "adventure": homepage_short + "/android.widget.Button[1]",
    "search": homepage_short + "/android.widget.Button[2]",
    "favorite": homepage_short + "/android.widget.Button[3]",
    "account": homepage_short + "/android.widget.Button[4]",
}

ACCOUNTPAGE_XPATH = {
    "accountpage_cancel": accountpage_short + "/android.view.ViewGroup[1]",
    "sign_in_facebook": accountpage_short + "/android.view.ViewGroup[2]",
    "sign_in_line": accountpage_short + "/android.view.ViewGroup[3]",
    "sign_in_google": accountpage_short + "/android.view.ViewGroup[4]",
    "sign_in_normal": accountpage_short + "/android.view.ViewGroup[5]",
    "sign_up_page": accountpage_short + "/android.view.ViewGroup[6]",
}

SIGNUPPAGE_XPATH = {
    "sign_up_cancel": sign_up_short,
    "last_name": sign_up_short + "/android.widget.EditText[1]",
    "first_name": sign_up_short + "/android.widget.EditText[2]",
    "email": sign_up_short + c + "[2]" + "/android.widget.EditText",
    "password": sign_up_short + c + "[3]" + "/android.widget.EditText",
    "password_confirmed": sign_up_short + c + "[4]" + "/android.widget.EditText",
    "sign_up": sign_up_short + "/android.view.ViewGroup[5]",
}

SIGNINPAGE_XPATH = {
    "sign_in_cancel": sign_in_short + c + "[1]" + c + "[2]" + "/android.widget.ImageView",
    "email": sign_in_short + c + "[2]" + "/android.widget.EditText",
    "password": sign_in_short + c + "[3]" + "/android.widget.EditText",
    "sign_in": sign_in_short + c + "[4]",
    "forget_password": sign_in_short + "/android.widget.TextView[3]"
}
