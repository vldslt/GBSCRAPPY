from dz3 import ScrapingJob
from pprint import pprint
vacancy_db = ScrapingJob('91.122.40.86', 'vacancy', 'vacancy_db')

vacancy_db.print_salary(300_000)
vacancy_db.collection.update_one({'vacancy_link': 'https://hh.ru/vacancy/31828023'},
                                 {'$set': {'city':'Москва', 'company_name':'some compary'}})

objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)

vacancy = 'Python'

vacancy_db.search_job(vacancy)
objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)

