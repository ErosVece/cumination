'''
    Cumination
    Copyright (C) 2015 Whitecream

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import re
import os
import sqlite3
from six.moves import urllib_parse
import six
import json
import random
from resources.lib import utils
from resources.lib.adultsite import AdultSite

bu = 'https://chaturbate.com/'
site = AdultSite('chaturbate', '[COLOR hotpink]Chaturbate[/COLOR]', bu, 'chaturbate.png', 'chaturbate', True)

addon = utils.addon
HTTP_HEADERS_IPAD = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4'}


@site.register(default_mode=True)
def Main():
    female = addon.getSetting("chatfemale") == "true"
    male = addon.getSetting("chatmale") == "true"
    couple = addon.getSetting("chatcouple") == "true"
    trans = addon.getSetting("chattrans") == "true"

    site.add_dir('[COLOR red]Refresh Chaturbate images[/COLOR]', '', 'clean_database', '', Folder=False)
    site.add_dir(
        '[COLOR hotpink]Look for Online Models[/COLOR]',
        f'{bu}?keywords=',
        'Search',
        site.img_search,
    )
    site.add_dir('[COLOR hotpink]Featured[/COLOR]', f'{bu}?page=1', 'List', '', '')
    site.add_dir(
        '[COLOR yellow]Current Hour\'s Top Cams[/COLOR]',
        f'{bu}api/ts/contest/leaderboard/',
        'topCams',
        '',
        '',
    )
    site.add_dir('[COLOR yellow]Online Favorites[/COLOR]', bu, 'onlineFav', '', '')
    site.add_dir(
        '[COLOR yellow]Followed Cams[/COLOR]',
        f'{site.url}followed-cams/',
        'List',
        '',
        '',
    )

    if female:
        site.add_dir(
            '[COLOR violet]Female[/COLOR]',
            f'{bu}female-cams/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Tags - Female[/COLOR]',
            f'{bu}api/ts/hashtags/tag-table-data/?sort=ht&page=1&g=f&limit=50',
            'Tags',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]New Cams - Female[/COLOR]',
            f'{bu}new-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Teen Cams (18+) - Female[/COLOR]',
            f'{bu}teen-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]18 to 21 Cams - Female[/COLOR]',
            f'{bu}18to21-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]20 to 30 Cams - Female[/COLOR]',
            f'{bu}20to30-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]30 to 50 Cams - Female[/COLOR]',
            f'{bu}30to50-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Mature Cams (50+) - Female[/COLOR]',
            f'{bu}mature-cams/female/?page=1',
            'List',
            '',
            '',
        )
        # site.add_dir('[COLOR hotpink]HD Cams - Female[/COLOR]', bu + 'hd-cams/female/?page=1', 'List', '', '')
        site.add_dir(
            '[COLOR hotpink]North American Cams - Female[/COLOR]',
            f'{bu}north-american-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]South American Cams - Female[/COLOR]',
            f'{bu}south-american-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Euro Russian Cams - Female[/COLOR]',
            f'{bu}euro-russian-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Asian Cams - Female[/COLOR]',
            f'{bu}asian-cams/female/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Other Region Cams - Female[/COLOR]',
            f'{bu}other-region-cams/female/?page=1',
            'List',
            '',
            '',
        )
    if couple:
        site.add_dir(
            '[COLOR violet]Couple[/COLOR]',
            f'{bu}couple-cams/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Tags - Couple[/COLOR]',
            f'{bu}api/ts/hashtags/tag-table-data/?sort=ht&page=1&g=c&limit=50',
            'Tags',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]New Cams - Couple[/COLOR]',
            f'{bu}new-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Teen Cams (18+) - Couple[/COLOR]',
            f'{bu}teen-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]18 to 21 Cams - Couple[/COLOR]',
            f'{bu}18to21-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]20 to 30 Cams - Couple[/COLOR]',
            f'{bu}20to30-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]30 to 50 Cams - Couple[/COLOR]',
            f'{bu}30to50-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Mature Cams (50+) - Couple[/COLOR]',
            f'{bu}mature-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        # site.add_dir('[COLOR hotpink]HD Cams - Couple[/COLOR]', bu + 'hd-cams/couple/?page=1', 'List', '', '')
        site.add_dir(
            '[COLOR hotpink]North American Cams - Couple[/COLOR]',
            f'{bu}north-american-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]South American Cams - Couple[/COLOR]',
            f'{bu}south-american-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Euro Russian Cams - Couple[/COLOR]',
            f'{bu}euro-russian-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Asian Cams - Couple[/COLOR]',
            f'{bu}asian-cams/couple/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Other Region Cams - Couple[/COLOR]',
            f'{bu}other-region-cams/couple/?page=1',
            'List',
            '',
            '',
        )
    if male:
        site.add_dir(
            '[COLOR violet]Male[/COLOR]',
            f'{bu}male-cams/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Tags - Male[/COLOR]',
            f'{bu}api/ts/hashtags/tag-table-data/?sort=ht&page=1&g=m&limit=50',
            'Tags',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]New Cams - Male[/COLOR]',
            f'{bu}new-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Teen Cams (18+) - Male[/COLOR]',
            f'{bu}teen-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]18 to 21 Cams - Male[/COLOR]',
            f'{bu}18to21-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]20 to 30 Cams - Male[/COLOR]',
            f'{bu}20to30-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]30 to 50 Cams - Male[/COLOR]',
            f'{bu}30to50-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Mature Cams (50+) - Male[/COLOR]',
            f'{bu}mature-cams/male/?page=1',
            'List',
            '',
            '',
        )
        # site.add_dir('[COLOR hotpink]HD Cams - Male[/COLOR]', bu + 'hd-cams/male/?page=1', 'List', '', '')
        site.add_dir(
            '[COLOR hotpink]North American Cams - Male[/COLOR]',
            f'{bu}north-american-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]South American Cams - Male[/COLOR]',
            f'{bu}south-american-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Euro Russian Cams - Male[/COLOR]',
            f'{bu}euro-russian-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Asian Cams - Male[/COLOR]',
            f'{bu}asian-cams/male/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Other Region Cams - Male[/COLOR]',
            f'{bu}other-region-cams/male/?page=1',
            'List',
            '',
            '',
        )
    if trans:
        site.add_dir(
            '[COLOR violet]Transsexual[/COLOR]',
            f'{bu}trans-cams/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Tags - Transsexual[/COLOR]',
            f'{bu}api/ts/hashtags/tag-table-data/?sort=ht&page=1&g=t&limit=50',
            'Tags',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]New Cams - Transsexual[/COLOR]',
            f'{bu}new-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Teen Cams (18+) - Transsexual[/COLOR]',
            f'{bu}teen-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]18 to 21 Cams - Transsexual[/COLOR]',
            f'{bu}18to21-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]20 to 30 Cams - Transsexual[/COLOR]',
            f'{bu}20to30-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]30 to 50 Cams - Transsexual[/COLOR]',
            f'{bu}30to50-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Mature Cams (50+) - Transsexual[/COLOR]',
            f'{bu}mature-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        # site.add_dir('[COLOR hotpink]HD Cams - Transsexual[/COLOR]', bu + 'hd-cams/trans/?page=1', 'List', '', '')
        site.add_dir(
            '[COLOR hotpink]North American Cams - Transsexual[/COLOR]',
            f'{bu}north-american-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]South American Cams - Transsexual[/COLOR]',
            f'{bu}south-american-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Euro Russian Cams - Transsexual[/COLOR]',
            f'{bu}euro-russian-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Asian Cams - Transsexual[/COLOR]',
            f'{bu}asian-cams/trans/?page=1',
            'List',
            '',
            '',
        )
        site.add_dir(
            '[COLOR hotpink]Other Region Cams - Transsexual[/COLOR]',
            f'{bu}other-region-cams/trans/?page=1',
            'List',
            '',
            '',
        )

    utils.eod()


@site.register()
def List(url, page=1):
    if 'followed' in url and 'offline' not in url:
        site.add_dir(
            '[COLOR yellow]Offline Rooms[/COLOR]',
            f'{site.url}followed-cams/offline/',
            'List',
            '',
            '',
        )
        if 'followed' in url:
            login()
    if addon.getSetting("chaturbate") == "true":
        clean_database(False)

    listhtml = utils._getHtml(url)
    match = re.compile(r'room_list_room.+?href="([^"]+).+?src="([^"]+).+?</a>(.*?)<div class="details.+?href[^>]+>([^<]+)<.+?age">([^<]*).+?class="subject"(.+?)data-slug=', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, status, name, age, data in match:
        subject, location, duration, viewers = '', '', '', ''
        if '/followed-cams/offline/' in url:
            match = re.compile(r'class="cams">([^<]+)<', re.DOTALL | re.IGNORECASE).findall(data)
            if match:
                age = match[0].strip()
        else:
            match = re.compile(r'>.+?>(.*?)</li.+?location.+?>([^<]*).+?time">([^<]+).+?viewers">([^<]+)', re.DOTALL | re.IGNORECASE).findall(data)
            if match:
                subject, location, duration, viewers = match[0]

        follow = 'title="Follow"' in data
        name = utils.cleantext(name)
        age = age.replace('&nbsp;', '')
        tags = re.findall(r'>#([^<]+)', subject)
        subject = re.sub(r'<.+>', '', subject)
        subject = f"{utils.cleantext(subject)}[CR][CR][COLOR deeppink]Location: [/COLOR]{utils.cleantext(location)}[CR][COLOR deeppink]Duration: [/COLOR]{utils.cleantext(duration)}[CR][COLOR deeppink]Watching: [/COLOR]{utils.cleantext(viewers)}"
        if tags:
            tags = '[COLOR deeppink]#[/COLOR]' + ', [COLOR deeppink]#[/COLOR]'.join(tags)
            subject += f"[CR][CR]{tags}"
        status = utils.cleantext(status.replace("[CR]", ""))
        if status:
            status = status.split('>')[1].split('<')[0]
        name = f"{name} [COLOR deeppink][{age}][/COLOR] {status}"
        id = videopage[1:-1]
        videopage = bu[:-1] + videopage

        contextfollow = f"{utils.addon_sys}?mode=chaturbate.Follow&id={urllib_parse.quote_plus(id)}"
        contextunfollow = f"{utils.addon_sys}?mode=chaturbate.Unfollow&id={urllib_parse.quote_plus(id)}"
        contextmenu = (
            [
                (
                    f'[COLOR violet]Follow [/COLOR]{name}',
                    f'RunPlugin({contextfollow})',
                )
            ]
            if follow
            else [
                (
                    f'[COLOR violet]Unfollow [/COLOR]{name}',
                    f'RunPlugin({contextunfollow})',
                )
            ]
        )

        site.add_download_link(name, videopage, 'Playvid', img, subject, contextm=contextmenu, noDownload=True)

    if nextp := re.compile(
        r'<a\s*href="([^"]+)"\s*class="next', re.DOTALL | re.IGNORECASE
    ).search(listhtml):
        page = page + 1 if page else 2
        next = bu[:-1] + nextp[1]
        site.add_dir(f'Next Page ({str(page)})', next, 'List', site.img_next, page)

    utils.eod()


@site.register(clean_mode=True)
def clean_database(showdialog=True):
    conn = sqlite3.connect(utils.TRANSLATEPATH("special://database/Textures13.db"))
    try:
        with conn:
            list = conn.execute("SELECT id, cachedurl FROM texture WHERE url LIKE '%%%s%%';" % ".highwebmedia.com")
            for row in list:
                conn.execute(f"DELETE FROM sizes WHERE idtexture LIKE '{row[0]}';")
                try:
                    os.remove(utils.TRANSLATEPATH(f"special://thumbnails/{row[1]}"))
                except:
                    pass
            conn.execute("DELETE FROM texture WHERE url LIKE '%%%s%%';" % ".highwebmedia.com")
            if showdialog:
                utils.notify('Finished', 'Chaturbate images cleared')
    except:
        pass


@site.register()
def Playvid(url, name):
    playmode = int(addon.getSetting('chatplay'))
    listhtml = utils._getHtml(url, headers=HTTP_HEADERS_IPAD)

    if r := re.search(r'initialRoomDossier\s*=\s*"([^"]+)', listhtml):
        data = six.b(r[1]).decode('unicode-escape')
        data = data if six.PY3 else data.encode('utf8')
        data = json.loads(data)
    else:
        data = False

    m3u8stream = data['hls_source'] if data else False
    if playmode == 0 and m3u8stream:
        videourl = "{0}|{1}".format(m3u8stream, urllib_parse.urlencode(HTTP_HEADERS_IPAD))
    elif playmode == 0 or playmode == 1 and not data:
        utils.notify('Oh oh', 'Couldn\'t find a playable webcam link')
        return

    elif playmode == 1:
        streamserver = f"rtmp://{m3u8stream.split('/')[2]}/live-edge"
        # streamserver = "rtmp://{}/live-edge".format(data['flash_host'])
        modelname = data['broadcaster_username']
        username_full = data['viewer_username']
        username = 'anonymous'
        room_pass = data['room_pass']
        swfurl = 'https://ssl-ccstatic.highwebmedia.com/theatermodeassets/CBV_TS_v1.0.swf'
        edge_auth = data['edge_auth']
        videourl = f"{streamserver} app=live-edge swfUrl={swfurl} pageUrl={url} conn=S:{username_full} conn=S:{modelname} conn=S:3.22 conn=S:{username} conn=S:{room_pass} conn=S:{edge_auth} playpath=mp4"
    vp = utils.VideoPlayer(name)
    vp.play_from_direct_link(videourl)


@site.register()
def Search(url, keyword=None):
    if not keyword:
        site.search_dir(url, 'Search')
    else:
        title = urllib_parse.quote_plus(keyword)
        url += title
        List(url)


@site.register()
def topCams(url):
    response = utils._getHtml(url)
    jsonTop = json.loads(response)['top']
    for iTop in jsonTop:
        subject = '[COLOR deeppink]Name: [/COLOR]' + iTop['room_user'] + '[CR]' \
            + '[CR][COLOR deeppink]Duration: [/COLOR]' + str(iTop['points']) + '[CR]' \
            + '[COLOR deeppink]Watching: [/COLOR]' + str(iTop['viewers'])
        site.add_download_link(iTop['room_user'], bu + iTop['room_user'] + '/', 'Playvid',
                               iTop['image_url'], subject, noDownload=True)
    utils.eod()


@site.register()
def Tags(url, page=1):
    cat = re.search(r'&g=([^&]*)', url)[1]
    categories = {
        'f': '/female/',
        'c': '/couple/',
        'm': '/male/',
        't': '/trans/',
    }
    category = categories.get(cat, '/')

    html = utils.getHtml(url, site.url)
    jdata = json.loads(html)
    total = jdata["total"]
    for tag in jdata["hashtags"]:
        name = tag["hashtag"]
        count = tag["room_count"]
        img = tag["top_rooms"][0].get("img", '') if tag["top_rooms"] else ''
        tagurl = f'{bu}tag/{name}{category}'
        name += f' [COLOR hotpink][{str(count)}][/COLOR]'
        site.add_dir(name, tagurl, 'List', img, 1)
    if page * 50 <= total:
        np_url = url.replace(f'&page={page}', f'&page={page + 1}')
        site.add_dir(
            f'Next Page ({str(page + 1)})',
            np_url,
            'Tags',
            site.img_next,
            page=page + 1,
        )
    utils.eod()


@site.register()
def onlineFav(url):
    wmArray = ["C9m5N", "tfZSl", "jQrKO", "5XO2a", "WXomN", "zM6MR", "Lb2aB", "cIbs3", "zM6MR", "mnzQo", "N6TZA"]
    chaturbate_url = 'https://chaturbate.com/affiliates/api/onlinerooms/?format=json&wm=' + random.choice(wmArray)
    data_chat = utils._getHtml(chaturbate_url, '')
    model_list = json.loads(data_chat)
    conn = sqlite3.connect(utils.favoritesdb)
    conn.text_factory = str
    c = conn.cursor()
    c.execute("SELECT DISTINCT name, url, image FROM favorites WHERE mode='chaturbate.Playvid'")
    result = c.fetchall()
    c.close()
    for (name, url, image) in result:
        model = [item for item in model_list if item["username"] == name.split('[COLOR')[0].strip()]
        if model:
            image = model[0]["image_url"]
            current_show = ''
            if "current_show" in model[0]:
                if model[0]["current_show"] != "public":
                    current_show = '[COLOR blue] {}[/COLOR]'.format(model[0]["current_show"])
            subject = model[0]["room_subject"] if utils.PY3 else model[0]["room_subject"].encode('utf8')
            subject = utils.cleantext(subject.split(' #')[0]) + "[CR][CR][COLOR deeppink]Location: [/COLOR]" + utils.cleantext(model[0]["location"]) + "[CR]" \
                + "[COLOR deeppink]Duration: [/COLOR]" + str(round(model[0]["seconds_online"] / 3600, 1)) + " hrs[CR]" \
                + "[COLOR deeppink]Watching: [/COLOR]" + str(model[0]["num_users"]) + " viewers"
            tags = '[COLOR deeppink]#[/COLOR]' + ', [COLOR deeppink]#[/COLOR]'.join(model[0]["tags"])
            tags = tags if utils.PY3 else tags.encode('utf8')
            subject += "[CR][CR]" + tags

            site.add_download_link(name + current_show, url, 'Playvid', image, utils.cleantext(subject), noDownload=True)
    utils.eod()


def login():
    url = 'https://chaturbate.com/followed-cams/'
    loginurl = 'https://chaturbate.com/auth/login/?next=/followed-cams/'

    loginhtml = utils._getHtml(url, site.url)
    if '<h1>Chaturbate Login</h1>' not in loginhtml:
        return

    username = utils._get_keyboard(default='', heading='Input your Chaturbate username')
    password = utils._get_keyboard(default='', heading='Input your Chaturbate password', hidden=True)

    match = re.compile(r'"csrfmiddlewaretoken"\s+value="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(loginhtml)
    if not match:
        return

    csrfmiddlewaretoken = match[0]
    hdr = utils.base_hdrs
    hdr.update({'Referer': 'https://chaturbate.com/auth/login/?next=/followed-cams/'})
    postRequest = {"next": "/followed-cams/",
                   "csrfmiddlewaretoken": csrfmiddlewaretoken,
                   "username": username,
                   "password": password,
                   "rememberme": "on"}
    response = utils._postHtml(loginurl, headers=hdr, form_data=postRequest)
    if 'title="Username Dropdown">{}<'.format(username) not in response:
        utils.notify('Chaturbate', 'Login failed please check your username and password')


@site.register()
def Unfollow(id):
    url = 'https://chaturbate.com/follow/unfollow/{}/'.format(id)
    html = utils._getHtml(url, site.url)
    if '<h1>Chaturbate Login</h1>' in html:
        login()
        html = utils._getHtml(url, site.url)
    match = re.compile(r'"csrfmiddlewaretoken"\s+value="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(html)
    if not match:
        return
    csrfmiddlewaretoken = match[0]
    hdr = utils.base_hdrs
    hdr.update({'Referer': 'https://chaturbate.com/'})
    postRequest = {"csrfmiddlewaretoken": csrfmiddlewaretoken}
    response = utils._postHtml(url, headers=hdr, form_data=postRequest)
    if '"following": false' in response:
        utils.notify('Chaturbate', 'NOT FOLLOWING [COLOR hotpink]{}[/COLOR]'.format(id))
        utils.refresh()


@site.register()
def Follow(id):
    url = 'https://chaturbate.com/follow/follow/{}/'.format(id)
    html = utils._getHtml(url, site.url)
    if '<h1>Chaturbate Login</h1>' in html:
        login()
        html = utils._getHtml(url, site.url)
    match = re.compile(r'"csrfmiddlewaretoken"\s+value="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(html)
    if not match:
        return
    csrfmiddlewaretoken = match[0]
    hdr = utils.base_hdrs
    hdr.update({'Referer': 'https://chaturbate.com/'})
    postRequest = {"csrfmiddlewaretoken": csrfmiddlewaretoken}
    response = utils._postHtml(url, headers=hdr, form_data=postRequest)
    if '"following": true' in response:
        utils.notify('Chaturbate', 'FOLLOWING [COLOR hotpink]{}[/COLOR]'.format(id))
        utils.refresh()
