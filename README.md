# python-template-app
A boilerplate for a Linux Python3 application which includes:

 * systemd servicefile 
 * /etc/sysconfig/ config file
 * RPM Build spec - also creates a system user which the application runs as
 * Includes a sample Polkit rules template

The Python application template itself is a simple boilerplate which sets up:

 * commandline parsing
 * Read params from a config file in /etc
 * Setup logging module
 * Logs to a file

The application, although just a boilerplate can be run.  It prints "Hello" to
console every second.  If ```-d DEBUG``` is set on the commandline 
or ```TEMPLATE_ARGS=-d DEBUG``` is set in /etc/sysconfig/template-app then the
log file in /var/log/template-app/template-app.log is written to with "Printed" + 1 second increment 

The RPM file installs the application into /usr/local/template-app 

The application runs as uid:gid template-app:template-app

The RPM look like this once installed
```
/etc/sysconfig
/etc/sysconfig/template-app
/etc/template-app.conf
/usr/lib/systemd/system
/usr/lib/systemd/system/template-app.service
/usr/local/template-app/template-app.py
/usr/share/doc/packages/template-app
/usr/share/doc/packages/template-app/README.md
/var/log/template-app
```

# Build the RPM
Install ```rpmdevtools``` and ```rpm-build```

Create the rpmbuild environment:
```
rpmdev-setuptree ~/rpmbuild
```

Run rpmbuild 
```
# --undefine=_disable_source_fetch - this enables download from spec Source0
rpmbuild --undefine=_disable_source_fetch -ba template-app.spec
```

# References 
https://rpm-packaging-guide.github.io

https://en.opensuse.org/openSUSE:Package_group_guidelines
