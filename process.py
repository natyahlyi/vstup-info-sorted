import click

import csv
import urllib.request as urllib2
from bs4 import BeautifulSoup


def prepare(url):
    request = urllib2.Request(url)
    request.add_header('Accept-Encoding', 'utf-8')
    response = urllib2.urlopen(request)
    global soup
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.find(class_="title-description").parent)


def process():
    global soup
    try:
        table = soup.find_all('table')[3]
    except IndexError:
        table = soup.find_all('table')[1]

    tbody = table.find('tbody')

    priority = 9

    data = []
    try:
        rows = tbody.find_all('tr')
    except AttributeError:
        table = soup.find_all('table')[2]
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        score = cols[3]
        try:
            p = int(cols[2])
        except ValueError:
            data.append([ele for ele in cols if ele])
            continue

        if p <= priority:
            data.append([ele for ele in cols if ele])

    output_file = open('output.csv', 'w', newline='')

    output_writer = csv.writer(output_file)

    heads = ['№', '#', 'ПІБ', 'П', 'Σ', 'Д']
    output_writer.writerow(heads)
    counter = 1

    priorities = list(range(1, priority + 1))
    for p in priorities:
        for entry in data:
            try:
                p1 = int(entry[2])
            except ValueError:
                output_writer.writerow([counter] + entry)
                data.remove(entry)
                counter += 1
                continue
            if p == p1:
                output_writer.writerow([counter] + entry)
                counter += 1

    output_file.close()


@click.command()
@click.option('--url', prompt='Enter vstup.info rating url')
def main(url):
    # for dummy benchmarking vstup.info response time
    import time

    start = time.time()
    prepare(url)
    end = time.time()
    print("prepare: " + str(end - start))

    start = time.time()
    process()
    end = time.time()
    print("process: " + str(end - start))

if __name__ == '__main__':
    main()