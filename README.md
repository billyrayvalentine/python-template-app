# template-app
A boiler plate for a Linux Python3 application which includes:

 * systemd servicefile 
 * /etc/sysconfig/ config file
 * RPM Build spec

The Python application template itself is a simple boiler plate which sets up:

 * commandline parsing
 * Read params from a config file in /etc
 * Setup logging module

The application although just a boiler can be run.  It just prints "Hello" to
console every second.  If ```-d DEBUG``` is set on the commandline 
or ```TEMPLATE_ARGS=-d DEBUG``` is set in /etc/sysconfig/template-app then the
log file in /var/log/template-app/template-app.log is written to with "Printed"
+ 1 second increment 

The RPM file installs the application into /usr/local/template-app 
A shell wrapper is installed into  /usr/local/bin/template-app which is the
entry point to the application

The application runs as uid:gid template-app:template-app

# References 
https://rpm-packaging-guide.github.io

https://en.opensuse.org/openSUSE:Package_group_guidelines
