class Book:
    num_of_books = 0
    def __init__(self, name='NULL', nonfiction_or_fiction='fiction', author='NULL', illustrator='NULL', page_count=0, publishing_company='scholastic', genre='NULL', series='NULL', price=0.00):
        self.name, self.nonfiction_or_fiction, self.author, self.illustrator, self.page_count, self.publishing_company, self.genre, self.series, self.price = name, nonfiction_or_fiction, author, illustrator, page_count, publishing_company, genre, series, price
        Book.num_of_books += 1
    def __str__(self):
        return f'name is {self.name}, is {self.nonfiction_or_fiction}, author is {self.author} illustrator is {self.illustrator},has {self.page_count} pages, genre is {self.genre}, publishing company is {self.publishing_company}, is part of the {self.series} series and costs {self.price}.'
    def is_it_overpriced(self):
        if self.price > 15.00 and self.page_count > 500:
            return 'yes'
        else:
            return 'no'
    def if_it_is_a_bargain(self):
        if self.price < 5.00 and self.page_count > 150:
            return 'yes'
        else:
            return 'no'
    def description(self):
        if self.series.lower() == 'diary of a wimpy kid':
            if self.name.lower() == 'the deep end':
                return 'Greg Heffley and his family hit the road for a cross-country camping trip. ' \
                       'But things take an unexpected turn, and they find themselves stranded ' \
                       'at an RV park. When the skies open up and water starts to rise, the Heffleys wonder' \
                       ' if they can save their vacation—or if they\'re already in too deep.'
            elif self.name == 'NULL' or self.name.strip() == '':
                return 'It\'s a new school year, and Greg Heffley finds himself thrust into middle school, where undersized ' \
                       'weaklings share the hallways with kids who are taller, meaner, and already shaving. The hazards of ' \
                       'growing up before you\'re ready are uniquely revealed through words and drawings as Greg records them in his diary.'
            elif self.name.lower() == 'rodrick rules':
                return 'Secrets have a way of getting out, ' \
                       'especially when a diary is involved.'
            elif self.name.lower() == 'the last straw':
                return 'Let\'s face it: Greg Heffley will never change his wimpy ways. Somebody just needs to explain that to Greg\'s father.'
            elif self.name.lower() == 'dog days':
                return 'It\'s summer vacation, the weather\'s great, and all the kids are having fun outside. So where\'s Greg Heffley? Inside his house, playing video games with the shades drawn.'
            elif self.name.lower() == 'the ugly truth':
                return 'Greg Heffley has always been in a hurry to grow up. But is getting older really all it\'s cracked up to be?'
            elif self.name.lower() == 'cabin fever':
                return 'Greg Heffley is in big trouble. School property has been damaged, and Greg is the prime suspect. But the crazy thing is, he\'s innocent. Or at least sort of.'
            elif self.name.lower() == 'the third wheel':
                return 'Love is in the air—but what does that mean for Greg Heffley?'
            else:
                return 'Sorry we do not have a description for that book yet.'
        else:
            return 'Sorry we do not have a description for this book yet.'
    #continue later ⬆️
    def where_can_i_buy_it(self):
        if self.series.lower() == 'diary of a wimpy kid':
            return 'at https://www.wimpykid.com'
        else:
            return 'at https://www.amazon.com'
    def can_i_trust_it(self):
        if self.nonfiction_or_fiction.lower() == 'nonfiction':
            return 'yes'
        else:
            return 'no'
class Animal:
    def __init__(self, name='NULL', alive=True, species='NULL', age=0, number_of_legs=0):
        self.name = name
        self.species = species
        self.age = age
        self.number_of_legs = number_of_legs
        self.alive = alive
    def can_it_walk(self):
        if self.number_of_legs < 2 or not self.alive:
            return 'no'
        else:
            return 'maybe'
    def __add__(self, other):
        self.age += other
        return self.age
    def __sub__(self, other):
        self.number_of_legs -= other
        return self.number_of_legs
    def dead(self):
        self.alive = False
class Computer:
    def __init__(self, brand='NULL', price=600.00, processor='i3', model="NULL", ram=8, storage=256, year=2021):
        self.brand = brand
        self.price = price
        self.processor = processor
        self.model = model
        self.ram = ram
        self.storage = storage
        self.year = year
    def is_it_expensive(self):
        if self.price < 999:
            return 'yes'
        else:
            return 'no'
    def is_it_cheap(self):
        if self.price < 500:
            return 'yes'
        else:
            return 'no'
    def is_it_not_modern(self):
        if self.year < 2017:
            return 'yes'
        else:
            return 'no'
    def is_it_modern(self):
        if self.year < 2016:
            return 'yes'
        else:
            return 'no'
