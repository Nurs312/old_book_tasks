def build_profile(first, last, **user_info):
    '''Строит словарь с информацией о пользователе'''
    profile = {}
    profile['firs_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return  profile


user_profile = build_profile('nurs', 'kadr',
                             location='bishkek',
                             field='it')
print(user_profile)