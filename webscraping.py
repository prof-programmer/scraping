from bs4 import BeautifulSoup
import requests
import time

# filtr - biz bilmaydigan skildan tashqari vakansiyalarni chiqarish
# todo: kamchiligi bor: katta yoki kichkina harflarga bogliq, togirlash kerak
# todo: bir nechta skil uchun filtr qilish kerak

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

# sayt adresini kiritish
# agar requests.get('').text deb kiritmasa (ya'ni oxirida text metodni qollamasa) html matnni olib bolmaydi
# faqat nimadir raqam qaytaradi
# shu sababli sayd adresi oxirida .text metodni qollash kerak
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    # lxml - bu parser
    soup = BeautifulSoup(html_text, 'lxml')
    # har bir vakansiya royxatda 'clearfix job-bx wht-shd-bx' klas bilan yozilgani uchun
    # aynan shu klasdagi 'li' teglarni izlaymiz
    # vakansiyalar 'li' teglari bilan saytga kiritilgan ekan
    # saytda 20mingdan kop python vakansiyalar bor ekan, lekin bu kod
    # faqat bir betdagi vakansiyalarni chiqaradi

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # index - bu sanovchi ekan, qanaqadir
    # enumerate - vakansiyalarni sanovchi metod, matnni chiroyli korinishi uchun ishlatildi
    for index, job in enumerate(jobs):
        # span tegni ichida yana 1ta span bolgani uchun text metoddan oldin span tegni ham metodga oxshab yozamiz
        # ya'ni ().span.text
        published_date = job.find('span', class_='sim-posted').span.text

        # blokda 'few' sozi bolsagina bizga vakansiyalarni chiqaradi
        if 'few' in published_date:
            # blokkka kompaniya nomi berilgan ekan
            # har bir blokni kompaniya nomi bolgani uchun osha blok
            # kompaniya nomini olish uchun aynan shu variable'ga find metodni ishlatishimiz
            # kerak ekan
            # .replace(' ', '') - chiqqan ma'lumotda kop bosh maydon bolgani uchun
            # bosh joylarni almashtirish uchun shu metod ishlatildi
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')

            # endi esa talab qilinadigan skillar izlanyapti, bu span tegda ekan
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')

            # kerakli ma'lumot qaysi tegda bolsa, osha teggacha bolgan teglar ketma-ket yoziladi
            # a tegni ichida href adresni olish uchun dictionary dagiday qavs ishlatildi a['href']
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                # har bir vakansiya alohida txt faylga kiritiladi
                # har bir fayl nomi raqamlanadi, chunki index qoyildi
                # w - argument write degani, faylga yozish uchun
                # f - variable
                with open(f'posts/{index}.txt', 'w') as f:
                    # strip() qoysa, Company Name: dan keyin kompaniya nomi bir qatorda chiqadi, bolmasa keyingi qatorda chiqarkan
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write((f'Required Skills: {skills.strip()} \n'))
                    f.write(f'More Info: {more_info}')
                print(f'File saved: {index}')


# if da keltirilgan kod - bunda fayl togridan - togri ochilsa, funksiya ishga tushadi
# agar shu fayl modul sifatida boshqa faylda korsatilsa yoq
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting time {time_wait} minutes...')
        # har millisekundda programma qayta ishga tushmasligi uchun uxlab turish vaqtini korsatamiz 10 minutni sekundda korsatamiz
        time.sleep(time_wait * 60)