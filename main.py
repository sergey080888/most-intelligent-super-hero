import requests


class Superhero:

    def get_superheros(self):
        url = "https://akabab.github.io/superhero-api/api/all.json"
        response = requests.get(url).json()
        hero_intelligence = 0
        hero_name = ''
        for hero in list_heroes:
            for item in response:
                if hero == item['name'] and item["powerstats"]['intelligence'] > hero_intelligence:
                    hero_intelligence = item["powerstats"]['intelligence']
                    hero_name = item['name']
        return f'Самый умный супер герой {hero_name} с интеллектом {hero_intelligence}'


if __name__ == '__main__':
    list_heroes = ['Hulk', 'Captain America', 'Thanos']
    most_intelligent_hero = Superhero()
    print(most_intelligent_hero.get_superheros())
