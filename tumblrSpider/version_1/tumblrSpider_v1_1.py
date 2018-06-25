# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:15:29 2018
@author: icetong
iceeeee频道@tumblrSpider
"""

from urllib import request
from xml.etree import ElementTree
from queue import Queue
import re, os

class tbrblog(object):
    
    def __init__(self, url, store='./data'):
        self.blog_url = url
        self.blog_name = self.get_blog_name(url)
        self.store = store
        self.api_url = 'https://{}.tumblr.com/api/read'.format(self.blog_name)
        
        self.max_num = 200
        self.start = 0
        self.num = 50
        self.photo_post = 0
        self.video_post = 0
        self.build_proxies()
        
        self.get_post_total()
        self.build_path(self.store+'/'+self.blog_name)
        self.build_path(self.store+'/'+self.blog_name+'/'+'photo')
        self.build_path(self.store+'/'+self.blog_name+'/'+'video')
        
        
    def build_path(self, file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        
    def build_proxies(self):
        proxies = {'https': '127.0.0.1:1080'}
        handler = request.ProxyHandler(proxies)
        opener = request.build_opener(handler)
        request.install_opener(opener)
        
    def get_blog_name(self, url):
        if url.find('.') == -1:
            self.blog_url = 'https://{}.tumblr.com'.format(url)
            return url
        name = re.findall(r'http[s]*?://([^\.]+)\.tumblr\.com', url)
        if name:
            return name[0]
        else:
            print('invalid url!')
            
    def get_response(self, url, recu_num=0):
        try:
            response = request.urlopen(url, timeout=5)
            return response
        except:
            recu_num += 1
            if recu_num >= 5:
                return None
            else:
                print('connect url: {} failed, retry...'.format(self.blog_url))
                return self.get_response(url, recu_num)
            
    def get_post_total(self):
        r = self.get_response(self.api_url)
        xml_string = r.read()
        tree = ElementTree.fromstring(xml_string)
        total = tree.getchildren()[1].attrib['total']
        self.total = eval(total)
        return eval(total)
    
    def extract_xml(self, xml_string):
        data = list()
        tree = ElementTree.fromstring(xml_string)
        start = tree.getchildren()[1].attrib['start']
        posts = tree.getchildren()[1]
        for post in posts:
            post_type = post.attrib['type']
            if post_type == 'video':
                inHtml = post.find('video-player').text
                #print(inHtml)
                try:
                    Id = re.findall(r'(tumblr_[^/""_]+)', 
                                inHtml)[0]
                except:
                    #print(inHtml)
                    print('drop a Password Required video post!')
                    continue
                file_dir = self.store + '/' + self.blog_name + '/' + post_type
                data.append({'type': post_type, 'Id': Id, 'file_dir': file_dir})
                self.video_post += 1
            elif post_type == 'photo':
                photoset = post.getchildren()[-1].getchildren()
                photolist = [photo.getchildren()[0].text for photo in photoset]
                file_dir = self.store + '/' + self.blog_name + '/' + post_type
                data.append({'type': post_type, 'photolist': photolist, 
                             'file_dir': file_dir})
                self.photo_post += 1
            else:
                continue
        return int(start), data
    
    def get_post_content(self):
        self.Data = list()
        while True:
            query_string = '?start={}&num={}'.format(self.start, self.num)
            query_url = self.api_url + query_string
            r = self.get_response(query_url)
            xml_string = r.read()
            now, data = self.extract_xml(xml_string)
            self.Data += data
            print('crawl {} posts'.format(now+self.num))
            if now >= self.max_num or len(self.Data) >= self.total:
                break
            else:
                self.start = now + self.num
                if self.start >= self.total:
                    self.start = self.total - now
        return self.Data


def build_proxies():
    proxies = {'https': '127.0.0.1:1080'}
    handler = request.ProxyHandler(proxies)
    opener = request.build_opener(handler)
    request.install_opener(opener)          

def down_file(url, file_path, name='process'):
    if os.path.exists(file_path):
        print('{} exit'.format(file_path))
        return None
    try:
        request.urlretrieve(url, file_path)
        print('download {} over'.format(name))
    except:
        pass
    
def download_file(d):
    if d['type'] == '#':
        url = 'https://vtt.tumblr.com/{}.mp4'.format(d['Id'])
        file_name = d['Id'] + '.mp4'
        file_path = d['file_dir'] + '/' + file_name
        down_file(url, file_path, file_name)
    if d['type'] == 'photo':
        for url in d['photolist']:
            file_name = url.split('/')[-1]
            file_path = d['file_dir'] + '/' + file_name
            down_file(url, file_path, file_name)
            
def Downloader(Data):
    
    for d in Data:
        download_file(d)
#        print(d)
    
if __name__=="__main__":
    build_proxies()
    print('汤不热博客图片视频爬虫简易版v1.1\n')
    print('https://github.com/ice-tong/TgItem/tree/master/tumblrSpider/version_1')
    print('telegram: iceeeee频道@tumblrSpider\t author@ice_tong')
    url = input('请输入一个汤不热博客链接或用户名（形如：https://signal1992.tumblr.com 或 signal1992）\n(直接回车下载默认汤主) >')
    if not url:
        url = 'https://signal1992.tumblr.com/'
    tbr = tbrblog(url)
    print('开始爬取 {} 。。。'.format(tbr.blog_name))
    Data = tbr.get_post_content()
    print('photo post: {}, video post: {}'.format(tbr.photo_post, tbr.video_post))
    Downloader(Data)
    print('over!')
    _ = input('回车结束运行!')
