# Creating a Local repository
Create an empty directory
```bash
$ mkdir my-local-repo
```
Convert the local empty directory to git local repo
Change to created directory
```bash
~/my-local-repo$ git init
Initialized empty Git repository in /home/ubuntu/my-local-repo/.git/
```
The above command will create .git folder that has meta data
```bash
~/my-local-repo$ ls -a
.  ..  .git
```
# Adding files to repository
Add file named Hello.txt
```bash
~/my-local-repo$ echo "Hello Wrold!!" > Hello.txt
echo "Hello Wroldls" > Hello.txt
```
### [Git Home](index.html)
