from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_card = soup.find_all('div', class_='card') #hamma div teglarni qaytaradi, card klasdagilarni
    for course in course_card:
        course_name = course.h5.text # h5 tegdagi matnni qaytaradi, bunda kurs nomi yozilgan
        # kurs narxlari a tegda yozilgani uchun, a tegdagi matnlarni olamiz
        # a tegni ichida narx oxirgi soz bolgani uchun faqat oxirgi elementni olish uchun split()[-1] ishlatildi
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')
