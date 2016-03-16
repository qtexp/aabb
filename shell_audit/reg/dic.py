#coding:utf-8
#!/usr/bin/env python
from collections import OrderedDict

shell_dict = OrderedDict([
("yum install redis|redis start|redis-server|redis-cli",
[(u'redis登录未带密码，可能未配置口令',),('')]),

("useradd",
[(u'发现在服务器上建立了账号',),('')]),

("chmod.*777",
[(u'发现建立危险权限目录',),('')]),

("-xu.*-xp.*-f|sftp .*:.*@|lftp .*:.*@|lftp -u .*,.*|keytool.*keypass |keytool.*storepass |keytool.*keypasswd |java -jar ygload.jar.*orcl|mysql .*-u.*-p[~!@#$%^&*()_+-=`{\[\]}\|\\:\"\<\>\?\;\'\,\.\/a-zA-Z]?\w|mysqldump .*-u.*-p[~!@#$%^&*()_+=`{\[\]}\|\\:\"\<\>\?\;\'\,\.\/a-zA-Z]+",
[(u'发现登录mysql服务器在命令中带密码的情况',),('')]),

("password=",
[(u'wget和curl、ftp带有密码参数',),('')]),

("yum install nc$|nc .*\d+.\d+.\d+.\d+.* \d+|nc -lk \d+|nc -vv",
[(u'发现安装使用黑客工具NC的情况(这里很有可能是检测某台服务器的端口是否为打开，是正常使用)',),('')]),

("ssh \w+@\d+.\d+.\d+.\d+|ssh \d+.\d+.\d+.\d+|ssh [0-9a-zA-Z]+",
[(u'发现登录并未使用key而使用密码的账号',),('')]),

("scp\s+-i\s+.*\s+.*kp-.*@\d+.\d+.\d+.\d+|scp\s+\.ssh/.*\.pub.*@\d+.\d+.\d+.\d+",
[(u'发现复制登录的ssh key的行为',),('')]),

("rm .*-rf",
[(u'发现不安全的命令使用系统，使用rm删除命令时带有 –rf  参数，易造成误操作',),('')]),

("rm .*log",
[(u'删除日志文件',),('')]),

("telnet.*\d+",
[(u'telnet验证端口开放情况',),('')]),

("vi\s+.*passwd|vim\s+.*passwd|cat\s+.*passwd|cat\s+.*authorized_keys|cat\s+.*id_rsa.pub|cat\s+.*root|cat\s+kp-|cat\s+~/\.ssh/kp-|cat\s+\./ssh/kp-|cat\s+.*\.key|vi\s+.*id_rsa|vi\s+.*authorized_keys|vim\s+.*id_rsa|vim\s+.*authorized_keys",
[(u'查看秘钥',),('')]),

("mongoexport",
[(u'导出mongodb数据库',),('')]),

("traceroute",
[(u'探测网络结构',),('')]),

("sz push|\/tmp\/push",
[(u'ssh登陆key放在/tmp目录下，且有下载ssh登录key的行为',),('')]),

("mysqlbinlog",
[(u'mysql二进制日志导出成文本',),('')]),

("rpm -ivh|yum install.*\.rpm",
[(u'安装rpm包',),('')]),

("passwd \w+",
[(u'修改系统账号密码，说明不是使用key登录',),('')]),

("shutdown|reboot|halt|poweroff|init 0|init 1",
[(u'发现可能重启或关机的命令',),('')])

])


shell_dict_drop = "nginx .*reload|nginx -s -c|\.\/\d+(\.\d+)*\.sh|\.\/yii\s|nginx -t|php -f|sshd restart|php\s+datadiff.*\.php|php .*test.*\.php|;s\b|;ls|alias|auc|beta|billing|cd |cdb|cde|cdt|cdl|CDT|chmod 600.*|chmod 700.*key|clear|clean|crontab -e|crontab -l|data$|date$|dat3$|data -s|db$|db_enterprise|db_jdb|db_pass|depl-|deploy_pass|df |dir$|do$|done$|du |exit|enterprise|entr$|except|exit$|find |gcdt|git$|git branch|git |grep |head |hiboot |hips -a|history$|history |ifconfig|ip a|java -version|jdb$|jdb -A|jdb_cloud|jenkins$|jy|kill |last |less |ll$|ll |log$|log\d+|logout|ls$|ls |lsof |man |mfind|mkdir |mv |mysqlJDB|ngjy|open$|owd$|pay$|paydb$|php$|php \.\/.* \d+|prod_|ps |pwd$|qc$|qc\d?|risk$|riskdb|rz$|s$|scpBonus|screen |sed |sendmsg |sh \d{1,3}\.sh|sh [a-z]{1,3}\.sh|sh mysql\.sh|sh payment\.sh|sh php.*\.sh|sh tail.*\.sh|ssh\d+|sshbeta|ssh-keygen|sshn|sshQ|sshr|sshserver|ssht|sshu|su |sudo |tail |tailf|todb|top$|vi .*\.trc|vi \.bashrc|vi.*sshd_config|vi .*php|vi.*xml|vi.*XML|vi.*\.out|vi.*conf|vi.*\.new|vi.*\.old|vi.*\.jsp|view$|view |vi.*\.java|vi.*\.txt|vi.*log\.sh|sz$|'$|cat .*\.json|jdb-cmd|more|service influxdb|!mysql|!netstat|.*ditui\.sh|\./main|\./mongo|\./.*_dev\.sh|\./nginx|\./php-fpm|\./reward.*\.sh|\./rsync.*\.sh|\./run.*\.sh|\./scp.*\.sh|\./shutdown\.sh|redis-c|redis-trib|sshFace|start\.sh|startup\.sh|update\.sh|yii-dev|/mongo|nginx\s+-c|nginx\s+-t|nginx\s+-s|php\s+.*\.php|php-fpm |catalina|Rename|\.XML|ldconfig|awk\s+access\.log|cat\s+.*influxdb|cat\s+.*rsync|cat\s+.*runinfo|cat/s+.*nginx|cd$|celar|cd\.\.|cdd$|cp\s+.*\.XML|cp\s+.*\.php|curl\s+.*localhost|date\s+.*|db$|df$|do$|gulp|hireboot|influx|more\s+.*\.trc|php.*yii|qiye\s?|sz\s+.*\.new|sz\s+.*\.old|sz\s+.*\.XML|vi\s+\d+\.sh|vi\s+.*\.dat|\.\/auto\.sh\s*?.*\.php|\./installmodel|\./java_install|\./listmodels|\./logstash-install|\./monitormodel|\./ng\.sh|\./sshditui|\./startmodel\.sh|\./uninstallmodel|<bean|bash\s*?\d*?login\.sh|cat\s*?\.bashrc"