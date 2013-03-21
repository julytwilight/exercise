# -*- coding: utf-8 -*-
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import MySQLdb

#content mysql
conn = MySQLdb.connect(host='localhost', user='root', passwd='Shouke*liutie')
cursor = conn.cursor()
cursor.execute('use InstHub')
ii = 1
while True:
    try:
        list = urlopen('http://stackoverflow.com/questions/tagged/ios?page=' + str(ii) + '&sort=newest&pagesize=15')
    except Exception, e:
        exit()

    soup = BeautifulSoup(list)

    pre = 'http://stackoverflow.com'
    
    for header in soup('h3'):
        links = header('a', 'question-hyperlink')
        if not links: continue
        link = links[0]

        #text = urlopen(pre + link['href'])
        html = urlopen(pre + link['href'])
        sp = BeautifulSoup(html)
        for question in sp('div', attrs={'class':'question'}):
            #get id
            qid =  int(question['data-questionid'])

            #get content
            text = question.find('div', attrs={'class':'post-text'}).contents
            l = [repr(i) for i in text if not isinstance(i, unicode)]
            m_text = MySQLdb.escape_string(''.join(l)).decode('utf-8')
            
            #get addtime
            time = question.find('span', attrs={'class':'relativetime'})
            addtime = time['title'].decode('utf-8')
            try:
                cursor.execute("insert into questionss (id, title, post, addtime) values(%d, '%s', '%s', '%s')" % (qid, link.string.decode('utf-8'), m_text, addtime))
            except Exception, e:
                log = "question:" + str(qid) + "\n"
                continue

        for answer in sp('div', attrs={'class':'answer'}):
            #get id
            aid =  int(answer['data-answerid'])

            #get contetn
            text = answer.find('div', attrs={'class':'post-text'}).contents
            l = [repr(i) for i in text if not isinstance(i, unicode)]
            m_text = MySQLdb.escape_string(''.join(l)).decode('utf-8')

            #get addtime
            time = answer.find('span', attrs={'class':'relativetime'})
            addtime = time['title'].decode('utf-8')

            try:
                cursor.execute("insert into answerss (id, qid, post, addtime) values(%d, %d, '%s', '%s')" % (aid, qid, m_text, addtime))
            except Exception, e:
                log =  "answer:" + str(aid) + "\n"

        html.close()
        print qid, 'ok'
    
    ii += 1

list.close()
conn.close()
#print '\n'.join(sorted(jobs, key=lambda s: s.lower()))
def write_log(log):
    f = open("log.txt", "wa")
    f.write(log)
    f.close()
