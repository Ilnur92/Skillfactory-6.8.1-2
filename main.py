from script import Cat

cats = [
    {
        'name': 'Барон',
        'floor': 'мальчик',
        'age': '2 года'
    },
    {
        'name': 'Сэм',
        'floor': 'мальчик',
        'age': '2 года'
    },
]

for cat in cats:
    cat_obj = Cat(name=cat.get('name'),
                  floor=cat.get('floor'),
                  age=cat.get('age'))

    print(cat_obj.name, cat_obj.floor, cat_obj.age)