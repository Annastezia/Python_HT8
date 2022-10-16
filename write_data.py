
def write_data():
    with open('data.csv', 'a', encoding='UTF-8') as f:
        keys = ['name', 'number', 'work']
        new_user = []
        for item in keys:
            new_user.append(input(f'Введите данные о пользователе: {item}: '))
        f.write('\n')
        f.write(','.join(new_user))
    return new_user