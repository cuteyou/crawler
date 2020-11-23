from requests_html import HTMLSession
import csv

session = HTMLSession()

file = open('movies.csv', 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(['自我介绍第一段内容'])

links3 = ['https://www.cnblogs.com/liujiarun/p/13615667.html','https://www.cnblogs.com/Jitorun/p/13616313.html','https://www.cnblogs.com/cherry-p/p/13615536.html','https://www.cnblogs.com/yaningscnblogs/p/13619100.html','https://www.cnblogs.com/FZUwhy/p/13619971.html','https://www.cnblogs.com/YangLiFena/p/13620502.html']
links3ul_li = ['https://www.cnblogs.com/kuanyang/p/13616764.html','https://www.cnblogs.com/lumosqqq/p/13618712.html','https://www.cnblogs.com/molly-woo/p/13618613.html','https://www.cnblogs.com/flow-time/p/13617526.html','https://www.cnblogs.com/axx4136/p/13619210.html']
links3p = ['https://www.cnblogs.com/clidd/p/13617392.html','https://www.cnblogs.com/021800626-wyj/p/13617667.html','https://www.cnblogs.com/suxiaoshao/p/13619073.html','https://www.cnblogs.com/fzucsx/p/13619562.html','https://www.cnblogs.com/Luotong-cnblogs/p/13623314.html']
links2 = ['https://www.cnblogs.com/bergscl/p/13617312.html','https://www.cnblogs.com/cyj-12138/p/13618069.html','https://www.cnblogs.com/xiaobingganya/p/13617723.html','https://www.cnblogs.com/czjlfe566/p/13619538.html','https://www.cnblogs.com/tiangouyzy/p/13620425.html','https://www.cnblogs.com/li-start/p/13619866.html','https://www.cnblogs.com/tansh/p/13621802.html','https://www.cnblogs.com/xy-669/p/13624167.html']
links2p = ['https://www.cnblogs.com/vcfghch/p/13616237.html','https://www.cnblogs.com/ElizzF/p/13616315.html','https://www.cnblogs.com/matoka/p/13616639.html','https://www.cnblogs.com/blacksheep107/p/13616814.html','https://www.cnblogs.com/brunuh/p/13617443.html','https://www.cnblogs.com/minskiter/p/13617406.html','https://www.cnblogs.com/sjz000/p/13616760.html','https://www.cnblogs.com/ywl031802435/p/13616632.html','https://www.cnblogs.com/cmygood/p/13617813.html','https://www.cnblogs.com/jinnian1120/p/13617810.html','https://www.cnblogs.com/danspG/p/13618636.html','https://www.cnblogs.com/koun/p/13618444.html','https://www.cnblogs.com/jxlhshine/p/13618368.html','https://www.cnblogs.com/lmmlm/p/13618928.html','https://www.cnblogs.com/chu-3/p/13618644.html','https://www.cnblogs.com/fzujch/p/13618675.html','https://www.cnblogs.com/Wifi-yang/p/13620429.html','https://www.cnblogs.com/lqj666/p/13619984.html','https://www.cnblogs.com/liulongmei/p/13619965.html','https://www.cnblogs.com/flashlight1/p/13620396.html','https://www.cnblogs.com/somecat/p/13620980.html','https://www.cnblogs.com/dylvia/p/13620754.html','https://www.cnblogs.com/pingcuo/p/13622746.html','https://www.cnblogs.com/newboy233/p/13621902.html']
links2pre = ['https://www.cnblogs.com/gaoyichao/p/13617346.html','https://www.cnblogs.com/wlululu/p/13616441.html','https://www.cnblogs.com/biqingl/p/13620303.html']
links1 = []
links1p = ['https://www.cnblogs.com/Jelor/p/13616381.html','https://www.cnblogs.com/fzx-123/p/13619261.html','https://www.cnblogs.com/wwying/p/13622770.html','https://www.cnblogs.com/kukicookie/p/13623839.html']
links4p = []
links4ul_li = ['https://www.cnblogs.com/AYuaner/p/13617356.html','https://www.cnblogs.com/lilychannel/p/13618224.html','https://www.cnblogs.com/autism-al/p/13621462.html']
linksblock_n4 = ['https://www.cnblogs.com/fragrant-breeze/p/13618598.html','https://www.cnblogs.com/llhhlh/p/13619433.html']
links_ul_li = ['https://www.cnblogs.com/czzqvq/p/13616187.html','https://www.cnblogs.com/xiaopijiu/p/13621992.html']
links_p = ['https://www.cnblogs.com/shenshuai/p/13616797.html','https://www.cnblogs.com/ThreeSmall/p/13616722.html','https://www.cnblogs.com/chentanyu/p/13617815.html','https://www.cnblogs.com/Fzu-hwl/p/13618821.html','https://www.cnblogs.com/muyu-sg/p/13619522.html']
links_pre = ['https://www.cnblogs.com/suuuhope/p/13617269.html']
linksblock_p= ['https://www.cnblogs.com/zhloo/p/13617682.html']
links18 = ['https://www.cnblogs.com/caolanying/p/13618875.html']
links5 = []
links5p = ['https://www.cnblogs.com/lkx15260/p/13618890.html','https://www.cnblogs.com/cxr82/p/13622370.html']
links6p = ['https://www.cnblogs.com/zxh2001/p/13620784.html','https://www.cnblogs.com/baiweidou/p/13622585.html']
linkstable_9p = ['https://www.cnblogs.com/zaiyunduan7/p/13618604.html']
links6 = ['https://www.cnblogs.com/hjy0731/p/13619652.html']

for link in links3:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul:nth-child(3)', first=True)
    csvwriter.writerow(contentt.text)


    # csvwriter.writerow(title.text, year.text)
    # TypeError: writer.writerow() takes exactly one argument (2 given)

for link in links3ul_li:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul > li:nth-child(3)', first=True)
    csvwriter.writerow(contentt.text)

for link in links3p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p:nth-child(3)', first=True)
    csvwriter.writerow(contentt.text)


for link in links2:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul:nth-child(2)', first=True)
    csvwriter.writerow(contentt.text)

for link in links2p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p:nth-child(2)', first=True)
    csvwriter.writerow(contentt.text)

for link in links2pre:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > pre:nth-child(2) ', first=True)
    csvwriter.writerow(contentt.text)

for link in links1:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul:nth-child(1)', first=True)
    csvwriter.writerow(contentt.text)

for link in links1p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p:nth-child(1)', first=True)
    csvwriter.writerow(contentt.text)

for link in links4p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p:nth-child(4)', first=True)
    csvwriter.writerow(contentt.text)

for link in links4ul_li:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul > li:nth-child(4)', first=True)
    csvwriter.writerow(contentt.text)

for link in linksblock_n4:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > blockquote:nth-child(4)', first=True)
    csvwriter.writerow(contentt.text)

for link in links_ul_li:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul > li', first=True)
    csvwriter.writerow(contentt.text)

for link in links_p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p', first=True)
    csvwriter.writerow(contentt.text)

for link in links_pre:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > pre', first=True)
    csvwriter.writerow(contentt.text)

for link in linksblock_p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > blockquote > p', first=True)
    csvwriter.writerow(contentt.text)

for link in links18:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p:nth-child(18)', first=True)
    csvwriter.writerow(contentt.text)

for link in links5:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul:nth-child(5) ', first=True)
    csvwriter.writerow(contentt.text)

for link in links5p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p:nth-child(5)', first=True)
    csvwriter.writerow(contentt.text)

for link in links6p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > p:nth-child(6)', first=True)
    csvwriter.writerow(contentt.text)

for link in linkstable_9p:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > table > tbody > tr > td > p:nth-child(9)', first=True)
    csvwriter.writerow(contentt.text)

for link in links6:
    r = session.get(link)
    contentt = r.html.find('#cnblogs_post_body > ul:nth-child(6)', first=True)
    csvwriter.writerow(contentt.text)

file.close()