a = (
    "/android.widget.FrameLayout",
    "/android.widget.FrameLayout[1]",
    "/android.widget.FrameLayout[2]",
    "/android.widget.FrameLayout[3]",
    "/android.widget.FrameLayout[4]",
)
b = (
    "/android.widget.LinearLayout",
    "/android.widget.LinearLayout[1]",
    "/android.widget.LinearLayout[2]",
    "/android.widget.LinearLayout[3]",
    "/android.widget.LinearLayout[4]",
)
c = (
    "/android.view.ViewGroup",
    "/android.view.ViewGroup[1]",
    "/android.view.ViewGroup[2]",
    "/android.view.ViewGroup[3]",
    "/android.view.ViewGroup[4]",
    "/android.view.ViewGroup[5]",
    "/android.view.ViewGroup[6]",
)
homepage_short = (
    "/hierarchy"
    + a[0]
    + b[0]
    + a[0]
    + b[0]
    + a[0]
    + a[0]
    + c[0]
    + c[0]
    + c[0]
    + c[0]
    + c[0]
    + c[0]
    + c[0]
    + c[2]
    + c[0]
)
accountpage_short = (
    "/hierarchy"
    + a[0]
    + b[0]
    + a[0]
    + b[0]
    + a[0]
    + a[0]
    + c[0]
    + c[0]
    + c[0]
    + c[2]
    + c[0]
    + c[0]
    + c[0]
    + c[0]
)
sign_up_short = (
    "/hierarchy"
    + a[0]
    + b[0]
    + a[0]
    + b[0]
    + a[0]
    + a[0]
    + c[0]
    + c[0]
    + c[0]
    + c[2]
    + c[2]
    + c[0]
    + c[1]
)
sign_in_short = (
    "/hierarchy"
    + a[0]
    + b[0]
    + a[0]
    + b[0]
    + a[0]
    + a[0]
    + c[0]
    + c[0]
    + c[0]
    + c[2]
    + c[2]
    + c[0]
    + c[1]
)

HOMEPAGE = {
    "adventure": homepage_short + "/android.widget.Button[1]",
    "search": homepage_short + "/android.widget.Button[2]",
    "favorite": homepage_short + "/android.widget.Button[3]",
    "account": homepage_short + "/android.widget.Button[4]",
}

ACCOUNTPAGE = {
    "accountpage_cancel": accountpage_short + c[1],
    "sign_in_facebook": accountpage_short + c[2],
    "sign_in_line": accountpage_short + c[3],
    "sign_in_google": accountpage_short + c[4],
    "sign_in_normal": accountpage_short + c[5],
    "sign_up_page": accountpage_short + c[6],
}

FACEBOOK_SIGNIN = {
    "account_name": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText",
    "password": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText",
    "enter": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Button",
    "continue": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button",
    "cancel": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button",
}

LINE_SIGNIN = {
    "email": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.EditText",
    "password": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[3]/android.widget.EditText",
    "enter": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[4]/android.widget.Button",
    "cancel": '//android.widget.ImageButton[@content-desc="Close tab"]',
    "allow_access": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View[2]/android.widget.Button",
}

SIGNINPAGE = {
    "sign_in_cancel": sign_in_short + c[1] + c[2] + "/android.widget.ImageView",
    "email": sign_in_short + c[2] + c[1] + "/android.widget.EditText",
    "password": sign_in_short + c[2] + c[2] + "/android.widget.EditText",
    "sign_in": sign_in_short + c[2] + c[3],
    "forget_password": sign_in_short + c[2] + "/android.widget.TextView[3]",
}

SIGNUPPAGE = {
    "sign_up_cancel": sign_up_short + c[1] + c[2] + "/android.widget.ImageView",
    "last_name": sign_up_short + c[2] + c[1] + "/android.widget.EditText",
    "first_name": sign_up_short + c[2] + c[2] + "/android.widget.EditText",
    "email": sign_up_short + c[2] + c[3] + "/android.widget.EditText",
    "password": sign_up_short + c[2] + c[4] + "/android.widget.EditText",
    "password_confirmed": sign_up_short + c[2] + c[5] + "/android.widget.EditText",
    "sign_up": sign_up_short + c[2] + c[6],
    "interested_theme_finish": "/hierarchy"
    + a[0]
    + b[0]
    + a[0]
    + b[0]
    + a[0]
    + a[0]
    + c[0]
    + c[0]
    + c[0]
    + c[3]
    + c[2]
    + c[0]
    + c[1]
    + c[2]
    + c[0]
    + c[0],
}


def xpath_replace(xpath):
    xpath_clear = xpath.replace("/", " + ")
    xpath_trans1 = xpath_clear.replace("android.widget.FrameLayout", "a")
    xpath_trans2 = xpath_trans1.replace("android.widget.LinearLayout", "b")
    xpath_trans3 = xpath_trans2.replace("android.view.ViewGroup", "c")
    xpath_trans4 = xpath_trans3.replace(" + hierarchy", '"/hierarchy"')

    return xpath_trans4