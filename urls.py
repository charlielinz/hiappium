a = "/android.widget.FrameLayout"
b = "/android.widget.LinearLayout"
c = "/android.view.ViewGroup"
homepage_short = (
    "/hierarchy" + a + b + a + b + a + a + c + c + c + c + c + c + c + c + "[2]" + c
)
accountpage_short = (
    "/hierarchy" + a + b + a + b + a + a + c + c + c + c + "[2]" + c + c + c + c
)
register_short = (
    "/hierarchy" + a + b + a + b + a + a + c + c + c + c + "[2]" + c + "[2]" + c + c + "[1]"
)

HOMEPAGE_URLS = {
    "adventure": homepage_short + "/android.widget.Button[1]",
    "search": homepage_short + "/android.widget.Button[2]",
    "favorite": homepage_short + "/android.widget.Button[3]",
    "account": homepage_short + "/android.widget.Button[4]",
}

ACCOUNTPAGE_URLS = {
    "cancel": accountpage_short + "/android.view.ViewGroup[1]",
    "login_facebook": accountpage_short + "/android.view.ViewGroup[2]",
    "login_line": accountpage_short + "/android.view.ViewGroup[3]",
    "login_google": accountpage_short + "/android.view.ViewGroup[4]",
    "login_normal": accountpage_short + "/android.view.ViewGroup[5]",
    "register_page": accountpage_short + "/android.view.ViewGroup[6]",
}

REGISTER_URLS = {
    "cancel": register_short,
    "last_name": register_short + "/android.widget.EditText[1]",
    "first_name": register_short + "/android.widget.EditText[2]",
    "email": register_short + c + "[2]" + "/android.widget.EditText",
    "password": register_short + c + "[3]" + "/android.widget.EditText",
    "password_confirmed": register_short + c + "[4]" + "/android.widget.EditText",
    "resigter": register_short + "/android.view.ViewGroup[5]",
}
