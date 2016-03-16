#coding:utf-8
#!/usr/bin/env python

import sys
import regex as re
import time
import csv
import codecs
from reg import dic
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding('utf-8')

shell_dict = dic.shell_dict
shell_dict_drop = dic.shell_dict_drop

class Shell_audit(object):
    def __init__(self, re_rule = None, re_desr = ''):
        self.re_rule = re_rule
        self.re_desr = re_desr

    # 处理正则部分代码
    def shell_regex(self, re_rule, shell_line):
        shell_hit = re.compile(self.re_rule)
        a = shell_hit.findall(shell_line)
        for i in a:
            return True

    def shell_write_title(self, shell_file):
        csvfile_r = open(shell_file, 'rb')
        reader = csv.reader(csvfile_r)
        csvfile_w = codecs.open('1.csv', 'ab', 'utf_8_sig')
        writer = csv.writer(csvfile_w)
        writer.writerows([(u'bash操作审计'+time.strftime('%Y-%m-%d',time.localtime(time.time())),),(''),('')])

    # 生成危险命令csv文件1.csv
    def shell_write(self, shell_file):

        csvfile_r = open(shell_file, 'rb')
        reader = csv.reader(csvfile_r)
        csvfile_w = codecs.open('1.csv', 'ab', 'utf_8_sig')
        writer = csv.writer(csvfile_w)
        writer.writerows(self.re_desr)
        for line in reader:
            line_str = ','.join(line)
            if self.shell_regex(self.re_rule, line_str):
                writer.writerow(line)
        writer.writerows([(''),('')])

    # 分离危险命令后的数据2.csv文件
    def shell_write_re(self, shell_file):
        csvfile_r = open(shell_file, 'rb')
        reader = csv.reader(csvfile_r)
        csvfile_w = codecs.open('2.csv', 'ab', 'utf_8_sig')
        writer = csv.writer(csvfile_w)
        for line in reader:
            line_str = ','.join(line)
            if self.shell_regex(self.re_rule, line_str):
                pass
            else:
                writer.writerow(line)
    
    # 去除冗余数据后生成3.csv文件
    def shell_write_drop(self, shell_file):
        csvfile_r = open(shell_file, 'rb')
        reader = csv.reader(csvfile_r)
        csvfile_w = codecs.open('3.csv', 'ab', 'utf_8_sig')
        writer = csv.writer(csvfile_w)
        for line in reader:
            line_str = ','.join(line)
            if self.shell_regex(self.re_rule, line_str):
                    pass
            else:
                writer.writerow(line)

if __name__ == '__main__':
    shell_start = time.time()
    shell_file = ''
    if len(sys.argv) != 2:
        print "Usage: shell_audit.py file"
    else:
        re_rule_re = []
        shell_file = sys.argv[1]
#-------------执行将写入csv文件的内容首行title-----------------------#        
        shell_title = Shell_audit()
        shell_title.shell_write_title(shell_file)
#--------------------------------------------------------------------#

        for re_rule in shell_dict.keys():
            print re_rule
#-----------执行将危险的shell命令生成另一份csv文件-------------------#
            shell = Shell_audit(re_rule,shell_dict[re_rule])
            shell.shell_write(shell_file)
#--------------------------------------------------------------------#

#-----------执行将危险的shell命令分离后生成另一份csv文件-------------#
            re_rule_re.append(re_rule)
        re_rule_rex = '|'.join(re_rule_re)
        shell_re = Shell_audit(re_rule_rex)
        shell_re.shell_write_re(shell_file)
#--------------------------------------------------------------------#

#-----------执行丢弃无用数据后生成需要审计的数据csv文件--------------#
        shell_drop = Shell_audit(shell_dict_drop)
        shell_drop.shell_write_drop('2.csv')
#--------------------------------------------------------------------#

    shell_end = time.time()
    shell_time = shell_end - shell_start
    print "----------------------------------------------------------------"
    print "The Scripts(shell_audit.py) has run for " + str(shell_time) + " seconds completed..."
    print "----------------------------------------------------------------"
