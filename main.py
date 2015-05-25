# -*- coding: utf-8 -*-
__author__ = 'puras'
__email__ = 'he@puras.me'

from pyquery import PyQuery as pq

import urllib
import os

def do_download(root_url):
    print '开始加载页面'
    d = pq(url=root_url)
    posts = d('div.m-post')
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
        print os.path.abspath(folder)
        print pic
        print name
        print picid
        print thumbnails
        print '开始加载子页面'
        print folder
        sd = pq(url=picurl)
        pics = sd('div.pic')
        num_file = '%s/pic_num.txt' % folder
        nf = open(num_file, 'w')
        nf.write('共有 %s 张图' % len(pics))
        nf.close()
        print '共有 %s 张图' % len(pics)
        for spic in pics:
            sdd = pq(spic)
            sexy_pic = sdd('img').attr('src')
            print sexy_pic
            sexy_name = sexy_pic.split('/')[len(sexy_pic.split('/')) - 1]
            print sexy_name
            sexy_file = '%s/%s' % (folder, sexy_name)
            if not os.path.exists(sexy_file):
                urllib.urlretrieve(sexy_pic, sexy_file)
            # break

        # break

if __name__ == '__main__':
    root_url = 'http://sexy.faceks.com/'

    do_download(root_url)

    print 'Download has finished.'
