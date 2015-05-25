# -*- coding: utf-8 -*-
__author__ = 'puras'
__email__ = 'he@puras.me'

from pyquery import PyQuery as pq

import urllib
import os
import logging

log = logging.getLogger('mooio')
hdlr = logging.FileHandler(os.path.join('mooio.log'))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
log.addHandler(hdlr)
log.setLevel(logging.INFO)

def do_download(root_url):
    print u'开始加载页面'
    log.info(u'开始加载页面:%s' % root_url)
    d = pq(url=root_url)
    posts = d('div.m-post')
    log.info(u'本页共有 %s 组图片' % len(posts))
    for post in posts:
        dd = pq(post)
        img = dd('img')
        p = dd('p')
        picurl = dd('a.img').attr('href')
        url_arrs = picurl.split('/')
        picid = url_arrs[len(url_arrs) - 1]
        name = p.text()
        pic = img.attr('src')
        thumbnails = pic.split('/')[len(pic.split('/')) - 1]
        folder = 'sexy/%s_%s' % (name, picid)
        if not os.path.exists(folder):
            os.makedirs(folder)
        pic_file = '%s/thumbnails_%s' % (folder, thumbnails)
        if not os.path.exists(pic_file):
            urllib.urlretrieve(pic, pic_file)
        print '开始加载子页面'
        log.info(u'正在加载: %s' % name)
        log.info(u'开始加载子页面:%s' % picurl)
        log.info(u'存入文件夹: %s' % folder)
        sd = pq(url=picurl)
        pics = sd('div.pic')
        num_file = '%s/pic_num.txt' % folder
        nf = open(num_file, 'w')
        nf.write('共有 %s 张图' % len(pics))
        nf.close()
        print u'共有 %s 张图' % len(pics)
        log.info(u'共有 %s 张图' % len(pics))
        for spic in pics:
            sdd = pq(spic)
            sexy_pic = sdd('img').attr('src')
            print sexy_pic
            sexy_name = sexy_pic.split('/')[len(sexy_pic.split('/')) - 1]
            print sexy_name
            sexy_file = '%s/%s' % (folder, sexy_name)
            if not os.path.exists(sexy_file):
                log.info(u'正在下载：%s' % sexy_pic)
                urllib.urlretrieve(sexy_pic, sexy_file)
            else:
                log.info(u'本图片已下载: %s' % sexy_pic)
            # break

        # break

if __name__ == '__main__':
    root_url = 'http://sexy.faceks.com/?page='

    for i in range(1, 40):
        print i
        download_url = '%s%d' % (root_url, i)
        print download_url
        log.info(u'当前下载地址: %s' % download_url)

        do_download(download_url)

    print 'Download has finished.'
