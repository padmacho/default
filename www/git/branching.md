# Branching
A branch in Git is simply a lightweight movable pointer to one of these commits. The default branch name in Git is **master**

As you add additional commits on a branch, the branch will move along

# Listing Branches
## List the local branch
```bash
vagrant@git-m1:~/git-demo(master)$ git branch
* master
```
The above command lists the branch and shows that we are working on master
## List the remote branch
List the remote branch
```bash
vagrant@git-m1:~/git-demo(master)$ git branch -r
  origin/HEAD -> origin/master
  origin/master
```
The above command lists remote branches and shows HEAD is pointing to remote master    
# Creating a Branch
Create a branch named bug-fix
```bash
vagrant@git-m1:~/git-demo(master)$ git checkout -b bug-fix
Switched to a new branch 'bug-fix'
```
The above command creates are new branch named **bug-fix** and update the working copy with new branch. Note this branch is created from **master**
# Know the branch on which you are working
git status gives the branch on with you are working

```bash
vagrant@git-m1:~/git-demo(bug-fix)$ git status
On branch bug-fix
nothing to commit, working directory clean
```
# Add and commit a file to branch
Lets add a file **fix.txt** to the branch **bug-fix**.
```bash
vagrant@git-m1:~/git-demo(bug-fix)$ echo "Hello" >> fix.txt            
vagrant@git-m1:~/git-demo(bug-fix)$ git add fix.txt                    
vagrant@git-m1:~/git-demo(bug-fix)$ git commit -m "added fix file"     
[bug-fix a8d0a15] added fix file                                       
 create mode 100644 fix.txt                                            
```
# Push a branch to remote repository
Push the local branch **bug-fix** remote repository **git-demo** which is present on the git hub server
```bash
vagrant@git-m1:~/git-demo(bug-fix)$  git push --set-upstream origin bug-fix
Username for 'https://github.com': padmacho
Password for 'https://padmacho@github.com':
Counting objects: 2, done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 266 bytes | 0 bytes/s, done.
Total 2 (delta 0), reused 0 (delta 0)
To https://github.com/padmacho/git-demo.git
 * [new branch]      bug-fix -> bug-fix
Branch bug-fix set up to track remote branch bug-fix from origin.
```
**origin** points to remote repository . **--set-upstream** helps to push to remote branch
# Switch Branch
Switch to branch **bug-fix-1**
```bash
vagrant@git-m1:~/git-demo(enhancement-1)$ git checkout bug-fix-1
Switched to branch 'bug-fix-1'
```
The above command will switch to branch **bug-fix-1** from the current working branch **enhancement-1**
# Renaming a branch
Rename branch **bug-fix** to **bug1**
```bash
vagrant@git-m1:~/git-demo(bug-fix)$ git branch -m bug-fix bug1
vagrant@git-m1:~/git-demo(bug1)$
```
# Deleting a branch
Delete the branch **bug1**
```bash
vagrant@git-m1:~/git-demo(master)$ git branch -d bug1
warning: deleting branch 'bug1' that has been merged to
         'refs/remotes/origin/bug-fix', but not yet merged to HEAD.
Deleted branch bug1 (was a8d0a15).
```
**Note**: Git complains that you are deleting a branch that was not merged,You cannot delete a branch on which you are currently working on.

**-D** to do a force delete

# [Git Home](index.html)
