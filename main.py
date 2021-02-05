print("Sos")
# че каво?

def faind_film(link, count_page, like_count):
    for i in range(count_page):
        link_page = f"{link}/page/{i + 1}/"

        # print(f'\nСтраница № {i+1},\n')
        response = requests.get(link_page)

        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup.title.text)
        zagolovki = soup.find_all(class_="zagolovki")
        rating = soup.find_all(class_="ratingtypeplusminus ignore-select ratingplus")

        rating_list = list(rating)  # список для готовых ссылок