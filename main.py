import requests as req
from bs4 import BeautifulSoup


def track_now():
    resp = req.get("https://onlineradiobox.com/ru/svoefm/playlist/?cs=ru.svoefm")
    soup = BeautifulSoup(resp.text, 'lxml')
    track_now1 = soup.find('tr').a.string

    return f'{track_now1}.mp3'


def load_track():
    r = req.get("https://r51-15-210-236.relay.radiotoolkit.com:30003/svoefm", stream=True)

    while True:
        track_name = track_now()
        print(track_name)

        with open(track_name, 'ab') as f:
            for block in r.iter_content(131072):
                if track_now() == track_name:
                    f.write(block)
                else:
                    break


if __name__ != "__main__":
    load_track()
