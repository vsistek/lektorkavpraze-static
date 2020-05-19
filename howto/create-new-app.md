# HOWTO Create a New App

This guide documents how to create a new app within lektorkavpraze-static framework. The app consists of a html page rendered from a source Markdown file, specific cgi call (can be parametrized) and typically a python program (executed by the cgi script) and its data (yaml). Some apps share python programs, this example documents an app based on genrandomtask.py - a program which renders a pair of task and solution strings based on randomly filled templates (useful for modeling language grammar excercises).

1. Check out or update the repository
```shell
git clone https://github.com/vsistek/lektorkavpraze-static.git
cd lektorkavpraze-static
# Switch to dev branch (changes should be first tested in dev / pi.lektorkavpraze.cz)
git checkout dev
# If you had the repository cloned already, pull latest changes
git pull
```
2. Start by copying a Markdown (`.md`) file from a similar existing app
```shell
cp src/apps/anglictina-predmentne-vety.md src/apps/anglictina-zakladni-gramatika.md
```
3. Edit `src/apps/anglictina-zakladni-gramatika.md` in your favourite text editor (Atom, vim...)
```markdown
[//]: # (##NAME## anglictina-zakladni-gramatika)
[//]: # (##DESCRIPTION## Aplikace: Angličtina: Základní gramatika)
[//]: # (##APICALL## genrandomtask.cgi?anglictina-zakladni-gramatika)

# [&#9881;](/aplikace.html) Angličtina
## Základní gramatika

**Aplikace na procvičení základů anglické gramatiky**

Malý moment...
{: #task }

Malý moment...
{: #solution }

<button onclick="toggleSolution()">Řešení</button>
<button onclick="getTask()">Další</button>
```
In `vi`, you can use these commands:
```vim
:%s/anglictina-predmentne-vety/anglictina-zakladni-gramatika/g
:%s/Předmětné věty/Základní gramatika/g
```
4. In this case, we are using `genrandomtask.py` and its helper cgi script. It expects one parameter, which is appended by `.yaml` and used as data for `genrandomtask.py`. This is defined as ##APICALL## symbol for templating, see the `.md` file above. So we need `anglictina-zakladni-gramatika.yaml` file.
```shell
cp ~/Downloads/english.yaml src/apps/anglictina-zakladni-gramatika.yaml
```
5. That's all for the app itself. To make it accessible from the apps page / menu, you need to add it to `src/04-aplikace.md`
```markdown
...
### Angličtina

* [&#9881; Základní gramatika](/aplikace/anglictina-zakladni-gramatika.html)
* [&#9881; Předmětné věty](/aplikace/anglictina-predmentne-vety.html)
{: .appsmenu }
...

```
In `vi`, you can use these commands:
```vim
/anglictina-predmentne-vety
yyp
1G
:/anglictina-predmentne-vety/s/anglictina-predmentne-vety/anglictina-zakladni-gramatika/
:/Předmětné věty/s/Předmětné věty/Základní gramatika/
```
6. Commit and push your changes to git
```shell
git status
git add src/04-aplikace.md src/apps/anglictina-zakladni-gramatika.md src/apps/anglictina-zakladni-gramatika.yaml
git commit -m "anglictina-zakladni-gramatika app
git push
7. Stat's it. Your app gets deployed to staging. To promote it to production, create a merge request for 'master' branch.
```
