appid = "e988b3e629e467ce468058a4321b5ce9"
import requests
from bs4 import BeautifulSoup as BS


def parser():
    r = requests.get('https://sinoptik.com.by/погода-минск')
    html = BS(r.text, 'html.parser')
    container = html.find('div', {"class":"weather__content_tab current dateFree"})
    temperature_elements = container.find_all('b')
    day_name = html.find('p', {"class":"weather__content_tab-day"}).text
    date = html.find('p', {"class":"weather__content_tab-date day_red"}).text
    mouth = html.find('p', {"class":"weather__content_tab-month"}).text
    temperature_list = [(element.text) for element in temperature_elements]
    min, max = temperature_list[0], temperature_list[1]
    some_text = html.find('div', {"class":"weather__article_description-text"}).text
    all_day_inf = (f'                    '
                   f'{day_name}  {date}  {mouth}\n'
                   f'Минмиальная температура: {min}\n'
                   f'Максимальная температура: {max}\n'
                   f'{some_text}')

    return  all_day_inf



