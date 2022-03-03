import json
import requests
from datetime import date


def calc_age(uid):
    yearsdate = []
    countdate = []

    r = requests.get(f'https://api.vk.com/method/users.get?v=5.81\
                     &access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_ids={uid}')
    response = r.json()
    id = response['response'][0]['id']
    r2 = requests.get(f'https://api.vk.com/method/friends.get?v=5.81\
                      &access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_id={id}&fields=bdate')

    dictData = json.loads(r2.content)

    for i in dictData['response']['items']:
        try:
            if len(i['bdate'].split('.')) == 3:
                yearsdate.append(date.today().year - int(i['bdate'].split('.')[2]))
        except:
            continue
    for i in yearsdate:
        countdate.append((i, yearsdate.count(i),))

    countdate = list(set(countdate))
    countdate = sorted(countdate, key=lambda x: (-x[1], x[0]))

    return countdate


if __name__ == '__main__':
    res = calc_age(123546)
    print(res)

