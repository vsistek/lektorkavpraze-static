# HOWTO Add a Quote

The web presentation has a box with a random quote or review for given topic of the page. This box loads quotes dynamically by calling `src/apps/getrandomquote.cgi` script. This script has its data in individual yaml files with naming convention `src/apps/quotes-##QUOTE##.yaml` where `##QUOTE##` is defined in `.md` file for each page (e.g. `src/01-anglictina.md`).

To add a new quote, follow [HOWTO Change a File](change-a-file.md) and modify respective yaml file (e.g. `src/apps/quotes-anglictina.yaml`).

Note that the format is:

```yaml
- [1, "Unicode string representing a quote with non-breakable spaces ensured using &nbsp;", "Author"]
```

The index number (`1` in the example above) must be unique. It is used to ensure that we don't display the same quote twice in a row (bear in mind that quotes are being randomly shuffled).
