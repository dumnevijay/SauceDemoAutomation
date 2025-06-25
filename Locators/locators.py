class Locators():

    #Login page objects
    username_input_id = "user-name"
    password_input_id = "password"
    login_button_id = "login-button"
    alert_message_xpath = "//h3[@data-test='error']"

    #Home page objects (/cart.html page)
    hamburger_menu_id = "react-burger-menu-btn"
    logout_link_id = "logout_sidebar_link"
    price_bar_class_name = "pricebar"
    shopping_cart_badge_class_name = "shopping_cart_badge"
    shopping_cart_link_class_name = "shopping_cart_link"
    checkout_button_id = "checkout"

    #Checkout page objects(/checkout-step-one.html page)
    first_name_input_id = "first-name"
    last_name_input_id = "last-name"
    postal_code_input_id = "postal-code"
    continue_button_id = "continue"

    #Checkout page objects(/checkout-step-two.html page)
    finish_button_id = "finish"

    #Checkout page objects(/checkout-complete.html page)
    checkout_complete_container_id = "checkout_complete_container"
    back_home_button_id = "back-to-products"
