class Book:
    def __init__(self, name='NULL', nonfiction_or_fiction='fiction', author='NULL', illustrator='NULL', page_count=0, publishing_company='scholastic', genre='NULL', series='NULL', price=0.00):
        self.name, self.nonfiction_or_fiction, self.author, self.illustrator, self.page_count, self.publishing_company, self.genre, self.series, self.price = name, nonfiction_or_fiction, author, illustrator, page_count, publishing_company, genre, series, price
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
            else:
                return 'Sorry we do not have \a description for that book yet.'
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
