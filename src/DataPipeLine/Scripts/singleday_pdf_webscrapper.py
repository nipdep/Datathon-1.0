from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin, quote
import datetime
import os
from bs4 import BeautifulSoup

incomplete_url = "http://www.epid.gov.lk/web/images/pdf/corona_virus_report/sitrep-sl-en-"
today = datetime.datetime.now()
current_date = [today.month,today.day]

def dateformat(currentdate=True):
    if(currentdate):
        today = datetime.datetime.now()
        month = today.month
        day = today.day

    else:
        selected = datetime.datetime.now() - datetime.timedelta(10)
        month = selected.month
        day = selected.day

    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)


    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    return ([month, day])

Directory='F:/Deeplearning/Datathon-1.0'


url = 'http://www.epid.gov.lk/web/index.php?option=com_content&view=article&id=225&Itemid=518&lang=en'
u = urlopen(url)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html)
for link in soup.select('p a'):
    href = link.get('href')
    # print(href)
    if href.startswith('javascript:'):
        continue

    filename = href.rsplit('/', 1)[-1]
    #print('sitrep-sl-sin-'+dateformat(currentdate=False)[1]+'-'+dateformat(currentdate=False)[0]+'_10.pdf')
    print(filename)
    if (filename == 'sitrep-sl-sin-'+dateformat(currentdate=False)[1]+'-'+dateformat(currentdate=False)[0]+'_10.pdf' or filename == 'sitrep-sl-en-'+dateformat(currentdate=False)[1]+'-'+dateformat(currentdate=False)[0]+'_10.pdf'or filename == 'sitrep-gl-en-'+dateformat(currentdate=False)[1]+'-'+dateformat(currentdate=False)[0]+'_10.pdf' or filename == 'sitrep-sl-sin-30-03_10.pdf'):
        break

    parts = filename.split('-')
    dw_name = parts[4][:2] + '-' + parts[3] + '.pdf'

    month = parts[4][:2]
    day = parts[3]

    print(current_date)
    print([int(month),int(day)])
    print([int(month),int(day)] == current_date)
    print(not os.path.exists(Directory + '/data/daily_pdf/' + dw_name))
    print('*** \n \n')
    #if (parts[1] == 'sl' and parts[2] == 'en' and filename != 'dailyreportcoronavirussin.pdf'):
    #    href = urljoin(url, quote(href))
    #    filepath = urlretrieve(href, './Datathon-1.0/data/daily_pdf/' + dw_name)


    try:
        if (parts[1] == 'sl' and parts[2] == 'en' and filename != 'dailyreportcoronavirussin.pdf'):
            href = urljoin(url, quote(href))

            # print(href)
            #print('../../../data/daily_pdf/'+dw_name)
            #filepath = urlretrieve(href,'./Datathon-1.0/data/daily_pdf/' + dw_name)
            if([int(month),int(day)] == current_date and (not os.path.exists(Directory + '/data/daily_pdf/' + dw_name))):
                try:
                    filepath = urlretrieve(href, Directory + '/data/daily_pdf/' + dw_name)
                    print('Sucess :- ', filepath[0], ' created')
                except:
                    print('url:- ', href)
                    print('date:- ', parts[4][:2] + '-' + parts[3])
                    print('failed to download')
     
    except:
        print(filename)


