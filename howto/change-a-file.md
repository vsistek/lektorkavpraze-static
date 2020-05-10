# HOWTO Change a File

1. Check out or update the repository
```shell
git clone https://github.com/vsistek/lektorkavpraze-static.git
cd lektorkavpraze-static
# Switch to dev branch (changes should be first tested in dev / pi.lektorkavpraze.cz)
git checkout dev
# If you had the repository cloned already, pull latest changes
git pull
```
2. Do your changes - example demonstrates how to change `src/04-aplikace.md`
```shell
# Open the file in your favourite editor, e.g. vi (or Atom), and do your changes
vi src/04-aplikace.md
```
3. Let git know that you really mean it for the next commit
```shell
# examine what git thinks of your workspace
git status
# Add what's really intended to the staging area
git add src/04-aplikace.md
# check status again - your change is green, it means staged
git status
```
4. Commit your staging area (sign it and add a comment what you meant by the change)
```shell
git commit -m "change apps menu layout"
# check log to see your new commit
git log
```
5. Push your change to GitHub - bear in mind that you modified just dev branch. Your change gets deployed to pi.lektorkavpraze.cz
```shell
git push

# If you cloned using https (as in this document), bear in mind that you will have to authenticate interactively using your GitHub credentials
```
6. If your change doesn't take effect, it may be because you pushed something else recently and webhook request to rebuild got blocked by anti-DOS mechanism. Trigger rebuild manually by visiting: `http://pi.lektorkavpraze.cz/aplikace/deploy-dev.sh` 
7. If you are satisfied with your work, get your change to production (lektorkavpraze.cz itself) by creating a Pull Request on GitHub. You want to merge `master <- dev`. Go to GitHub and follow on-screen instructions: `https://github.com/vsistek/lektorkavpraze-static/compare/master...dev?expand=1`
8. Merge your Pull Request on GitHib.
9. Webhooks are still work in progress. Manual rebuild of production is needed. Visit: `http://cloud.lektorkavpraze.cz/aplikace/deploy.sh`
10. Voila, your change will appear in production
