# lektorkavpraze-static

lektorkavpraze.cz web page - presentation of a private teacher in Prague (my wife).

Website is statically generated using custom shell script, see `src/util/build.sh`

There are some dynamic backend parts in python3 served through CGI shell scripts, see `src/apps`

## Install

This repository is used on a Debian-based GNU/Linux instance (although it is written pretty portably).
```
sudo apt-get install python3-markdown python3-yaml
```

To make dynamic backend parts working, CGI execution has to be allowed for `.cgi` files in `htdocs/aplikace`.

Example in Apache 2 format:
```
<Directory /var/www/lektorkavpraze-static/htdocs/aplikace>
    Options +ExecCGI -Indexes
    AddHandler cgi-script .cgi
</Directory>
```

## Authors

- Vaclav Sistek &lt;vsistek@fsfe.org&gt;
- Monika Sistkova &lt;monika.sistkova@gmail.com&gt;

## License

Apache License 2.0 for software source code

CC BY-NC for artworks and data
