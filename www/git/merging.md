# Merging
Merging branches
# Merge a local branch
Merge a local branch named **bug-fix-1** to **master** branch
```bash
vagrant@git-m1:~/git-demo(master)$ git merge bug-fix-1
Updating 7f84bd4..d574154
Fast-forward
 Hello.txt | 2 ++
 1 file changed, 2 insertions(+)
```
# Merge a remote branch
Merge changes in **master** branch on github to local **master** branch
```bash
vagrant@git-m1:~/git-demo(master)$ git pull origin master
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/padmacho/git-demo
 * branch            master     -> FETCH_HEAD
   7f84bd4..9c73542  master     -> origin/master
Merge made by the 'recursive' strategy.
 README.md | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```
#[Git Home](index.html)
