# lektorkavpraze-static

lektorkavpraze.cz web page - presentation of a private teacher in Prague (my wife).

Website is statically generated using custom shell script, see `src/util/build.sh`

There are some dynamic parts in python3 served as tiny ajax web services (CGI shell scripts), see `src/apps`

## Install

This repository is used on a Debian-based GNU/Linux instance (although it is written pretty portably).
```
sudo apt-get install python3-markdown python3-yaml
# for github webhook
sudo apt-get install jq
```


## Author

Vaclav Sistek &lt;vsistek@fsfe.org&gt;

## Credits

Some python3 scripts and data in `src/apps` are original work or derived from original work of Monika Sistkova &lt;monika.sistkova@gmail.com&gt;

## License

Apache License 2.0 for software source code
CC BY-NC for artworks and data
