from datetime import time

def test_time_for_dark(): # включение темной темы, если позже 10 вечера и раньше 6 утра
    current_hour = time(hour=0)
    is_dark_theme = None
    if current_hour.hour>=22 or current_hour.hour<6:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True

def test_user_choose_theme(): #включение темной темы по желанию пользователя
    current_hour = time(hour=16)
    #no_sleep = (current_hour.(hour>=22) or current_hour.(hour<6))
    is_dark_theme = None
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
         is_dark_theme = current_hour.hour>=22 or current_hour.hour<6

    assert is_dark_theme is True

def test_name_search_from_list(): #поиск юзера с именем Ольга
     suitable_user = None
     users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
     for user in users:
         if user["name"] == 'Olga':
             suitable_user = user
             break

     assert suitable_user == {"name": "Olga", "age": 45}

def test_search_young_user(): #поиск пользователей младше 20 лет
    suitable_user = []
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    for user in users:
        if user["age"] < 20:
            suitable_user.append(user)

    assert suitable_user == [{"name": "Stanislav", "age": 15}, {"name": "Maria", "age": 18}]

#функции работы с браузером

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def print_name(func, *args):
    readable_func_name = func.__name__.replace('_', ' ').title()
    readable_args_names = ", ".join(args)
    print(f"{readable_func_name} [{readable_args_names}]")
    return f"{readable_func_name} [{readable_args_names}]"


def open_browser(browser_name):
    actual_result = print_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_name(find_registration_button_on_login_page,page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
