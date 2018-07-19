# Mail server for development
It is common to use mail server to email notification when we are developing application. Lets setup a simple mail server in **Linux** and send / receive emails.

# Prerequisites
- RedHat Linux server - Any linux operating system can be used,  this article is tested with Red Hat Enterprise Linux Server release 7.0 (Maipo)
- PostFix mail Server

# Installation of PostFix mail server
- Lets find whether mail server is installed or not
```bash
[root@localhost ~]# rpm -q postfix
postfix-2.10.1-6.el7.x86_64
```   
The above command shows that mail server is installed
- Check wheter mail server is running are not
```bash
root@localhost ~]# systemctl status postfix
postfix.service - Postfix Mail Transport Agent
   Loaded: loaded (/usr/lib/systemd/system/postfix.service; enabled)
   Active: active (running) since Fri 2018-03-16 00:46:16 EDT; 5min ago
```
Mail server is installed and running

# Create two users
- Lets create two users named **tom** and **jerry** . Send an email from tom to jerry
```bash
[root@localhost ~]# useradd tom
[root@localhost ~]# useradd jerry
```
# Send Mail
Lets send mail from tom to jerry. You can use **mail** client program to send mail
- Switch to user tom from root
```bash
[root@localhost ~]# su - tom
Last failed login: Tue Mar 13 12:46:04 EDT 2018 from airavath on ssh:notty
There were 2 failed login attempts since the last successful login.
```
- Send mail from tom
```bash
[tom@localhost ~]$ mail jerry@localhost.localdomain
Subject: Hello Jerry                               
Hi Jerry,                                          
How are you. Hope things are well from your end.   
Thank you,                                         
Tom                                                
EOT                                                
```
Press **Ctrl+D** to send mail after typing
# Read Mail
Read mail using **mail** client program.
- Switch to Jerry user from root
```bash
[root@localhost ~]# su - jerry
[jerry@localhost ~]$
```
- Read email

```bash
[jerry@localhost ~]$ mail                                              
Heirloom Mail version 12.5 7/5/10.  Type ? for help.                   
/var/spool/mail/jerry: 1 message 1 new                               
>N  1 tom@localhost.locald  Fri Mar 16 00:57  22/699   Hello Jerry   
& 1                                                                    
Message  1:                                                            
From tom@localhost.localdomain  Fri Mar 16 00:57:43 2018               
Return-Path: <tom@localhost.localdomain>                               
X-Original-To: jerry@localhost.localdomain                             
Delivered-To: jerry@localhost.localdomain                              
Date: Fri, 16 Mar 2018 00:57:43 -0400                                  
To: jerry@localhost.localdomain                                        
Subject: Hello Jerry                                                   
User-Agent: Heirloom mailx 12.5 7/5/10                                 
Content-Type: text/plain; charset=us-ascii                             
From: tom@localhost.localdomain                                        
Status: R                                                              

Hi Jerry,                                                              
How are you. Hope things are well from your end.                       
Thank you,                                                             
Tom                                                                   
&                                                               
```

Press **q** to quit the mail program.
