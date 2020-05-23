# HOWTO Rename an Application

1. Check out or update the repository
```shell
git clone https://github.com/vsistek/lektorkavpraze-static.git
cd lektorkavpraze-static
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
git add ../04-aplikace.md anglictina-predmentne-vety.md
git commit -m "anglicke-vety -> anglictina-predmentne-vety"
git push
```
