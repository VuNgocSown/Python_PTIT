# 5-1. Person
person = {
    'ho': 'Ngoc',
    'ten': 'Son',
    'tuoi': 25,
    'thanh_pho': 'Ha Noi'
}
print(person['ho'])
print(person['ten'])
print(person['tuoi'])
print(person['thanh_pho'])

# 5-2. Favorite Numbers
favorite_numbers = {
    'An': 7,
    'Binh': 42,
    'Cuong': 3
}
for name, number in favorite_numbers.items():
    print(f"So yeu thich cua {name} la {number}.")

# 5-3. Glossary
glossary = {
    'bien': 'mot vi tri duoc dat ten de luu tru du lieu trong bo nho.',
    'vong lap': 'mot chuoi cac lenh duoc lap lai lien tuc cho den khi dat duoc mot dieu kien nhat dinh.',
    'ham': 'mot khoi ma chi chay khi no duoc goi.'
}
for word, meaning in glossary.items():
    print(f"{word}: {meaning}")

# 5-4. Glossary 2
glossary = {
    'bien': 'mot vi tri duoc dat ten de luu tru du lieu trong bo nho.',
    'vong lap': 'mot chuoi cac lenh duoc lap lai lien tuc cho den khi dat duoc mot dieu kien nhat dinh.',
    'ham': 'mot khoi ma chi chay khi no duoc goi.',
    'danh sach': 'mot tap hop cac muc theo thu tu nhat dinh.',
    'tu dien': 'mot tap hop cac cap khoa-gia tri.'
}
for word, meaning in glossary.items():
    print(f"{word}: {meaning}")

# 5-5. Rivers
rivers = {
    'mekong': 'viet nam',
    'hong': 'viet nam',
    'sai gon': 'viet nam'
}
for river, country in rivers.items():
    print(f"Song {river.title()} chay qua {country.title()}.")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# 5-6. Polling
favorite_languages = {
    'ha': 'python',
    'son': 'c',
    'linh': 'ruby',
    'phuc': 'python',
}
people_to_poll = ['ha', 'son', 'linh', 'phuc', 'minh', 'anh']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Cam on {person.title()} da tham gia cuoc tham do.")
    else:
        print(f"{person.title()}, vui long tham gia cuoc tham do cua chung toi!")

# 5-7. People
person1 = {
    'ho': 'Ngoc',
    'ten': 'Son',
    'tuoi': 25,
    'thanh_pho': 'Ha Noi'
}
person2 = {
    'ho': 'Minh',
    'ten': 'Anh',
    'tuoi': 22,
    'thanh_pho': 'Ho Chi Minh'
}
person3 = {
    'ho': 'Ha',
    'ten': 'Linh',
    'tuoi': 28,
    'thanh_pho': 'Da Nang'
}
people = [person1, person2, person3]
for person in people:
    print(person)

# 5-8. Pets
pet1 = {
    'loai_dong_vat': 'cho',
    'chu_so_huu': 'ngoc'
}
pet2 = {
    'loai_dong_vat': 'meo',
    'chu_so_huu': 'minh'
}
pet3 = {
    'loai_dong_vat': 'chuot hamster',
    'chu_so_huu': 'ha'
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(pet)

# 5-9. Favorite Places
favorite_places = {
    'ngoc': ['ha noi', 'ha long', 'sapa'],
    'minh': ['ho chi minh', 'vung tau'],
    'ha': ['da nang', 'hoi an']
}
for person, places in favorite_places.items():
    print(f"Nhung dia diem yeu thich cua {person.title()} la:")
    for place in places:
        print(f"- {place.title()}")

# 5-10. Favorite Numbers
favorite_numbers = {
    'An': [7, 14, 21],
    'Binh': [42, 56],
    'Cuong': [3, 9, 27]
}
for name, numbers in favorite_numbers.items():
    print(f"So yeu thich cua {name} la: {', '.join(map(str, numbers))}")

# 5-11. Cities
cities = {
    'ha noi': {
        'quoc gia': 'viet nam',
        'dan so': '8 trieu',
        'su_that': 'Thu do cua Viet Nam.'
    },
    'ho chi minh': {
        'quoc gia': 'viet nam',
        'dan so': '9 trieu',
        'su_that': 'Thanh pho lon nhat Viet Nam.'
    },
    'da nang': {
        'quoc gia': 'viet nam',
        'dan so': '1 trieu',
        'su_that': 'Noi tieng voi bai bien My Khe.'
    }
}
for city, info in cities.items():
    print(f"Thanh pho: {city.title()}")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")

# 5-12. Extensions
favorite_languages = {
    'ha': 'python',
    'son': 'c',
    'linh': 'ruby',
    'phuc': 'python',
}
people_to_poll = ['ha', 'son', 'linh', 'phuc', 'minh', 'anh']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Cam on {person.title()} da tham gia cuoc tham do.")
    else:
        print(f"{person.title()}, vui long tham gia cuoc tham do cua chung toi!")
additional_languages = {
    'minh': 'java',
    'anh': 'javascript'
}
favorite_languages.update(additional_languages)
for person, language in favorite_languages.items():
    print(f"Ngon ngu yeu thich cua {person.title()} la {language.title()}.")

# 7-13. User Profile
def build_profile(first, last, **user_info):
    profile = {}
    profile['ho'] = first
    profile['ten'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile('Vu', 'Ngoc Son', tuoi=22, dia_diem='Hanoi', nganh='Khoa hoc may tinh')
print(my_profile)

# 7-14. Cars
def make_car(manufacturer, model, **car_info):
    car = {}
    car['nha_san_xuat'] = manufacturer
    car['mau'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', mau_sac='xanh', goi_keo=True)
print(car)
