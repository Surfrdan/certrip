Simply supply hostname as single argument and return list of all Subejct Alternative Names for the TLS certificate
```
$ certrip example.com
www.example.org
example.com
example.edu
example.net
example.org
www.example.com
www.example.edu
www.example.net
```

You can also supply an optional port number

```
$ certrip -p 8443 example.com
www.example.org
example.com
```
