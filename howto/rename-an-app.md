# HOWTO Rename an Application

1. Check out or update the repository
```shell
git clone https://github.com/vsistek/lektorkavpraze-static.git
cd lektorkavpraze-static
# Switch to dev branch
git checkout dev
# If you had the repository cloned already, pull latest changes
git pull
```
2. Navigate to apps dir and rename files
```shell
cd lektorkavpraze-static/src/apps
git mv anglicke-vety.md anglictina-predmentne-vety.md
git mv anglicke-vety.yaml anglictina-predmentne-vety.yaml
```
3. Edit app metadata in the markdown file
```
vi anglictina-predmentne-vety.md
[//]: # (##NAME## anglictina-predmentne-vety)
[//]: # (##DESCRIPTION## Aplikace: Angličtina: Předmětné věty)
[//]: # (##APICALL## genrandomtask.cgi?anglictina-predmentne-vety)
```
4. Update link in app page
```shell
vi ../04-aplikace.md
* [&#9881; Předmětné věty](/aplikace/anglictina-predmentne-vety.html)
```
4. Commit and push
```shell
git status
On branch dev
Your branch is up to date with 'origin/dev'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	renamed:    anglicke-vety.md -> anglictina-predmentne-vety.md
	renamed:    anglicke-vety.yaml -> anglictina-predmentne-vety.yaml

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   ../04-aplikace.md
	modified:   anglictina-predmentne-vety.md

# Note that renames done using 'git mv' are aleady staged
git add ../04-aplikace.md anglictina-predmentne-vety.md
git commit -m "anglicke-vety -> anglictina-predmentne-vety"
git push
```
