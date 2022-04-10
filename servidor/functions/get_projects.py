import requests

def getTitleAndLink(HTML):
    link = HTML[HTML.index('href="')+6:]
    title = link[link.index('>')+1:]
    title = title[:title.index('<')].strip()
    link = link[:link.index('"')]
    link = 'https://github.com'+link
    return {'Link':link,'Title':title}

def getDescriptions(HTML):
    try:
        description = HTML[HTML.index('<p class="col-9 d-inline-block color-fg-muted mb-2 pr-4"'):]
        description = description[description.index('>')+1:]
        description = description[:description.index('<')].strip()
    except:
        description = '...'
    return {'Description':description}

def getTime(HTML):
    time = HTML[HTML.index('<relative-time datetime="'):]
    time = time[time.index('>')+1:]
    time = time[:time.index('<')].strip()
    time = 'Updated '+ time
    return {'Time':time}

def getLinguage(HTML):
    try:
        linguage = HTML[HTML.index('<span itemprop="programmingLanguage">'):]
        linguage = linguage[linguage.index('>')+1:]
        linguage = linguage[:linguage.index('<')]
    except:
        linguage = None
    return {'Linguage':linguage}

def getListProjects(url):
    resp = requests.get(url)
    html = resp.text
    html = html[html.index('<ul data-'):]
    html = html[:html.index('</ul')]
    projetos = html.split('<li')[1:]
    retorno = []
    for HTML in projetos:
        data = dict(**getTitleAndLink(HTML),**getDescriptions(HTML),**getTime(HTML),**getLinguage(HTML))
        if data['Linguage']:
            retorno.append(data)
    return retorno
