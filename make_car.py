def make_car(brand, model, color, tow_package, **user_info):
    profile = {}
    profile['Brand'] = brand.title()
    profile['Model'] = model.title()
    profile['Color'] = color.title()
    profile['Complectation'] = tow_package
    for key, value in user_info.items():
        profile[key.title()] = value
    return profile


