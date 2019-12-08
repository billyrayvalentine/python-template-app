Name: template-app
Version: 0.1        
Release: 1
Summary: A simple Python boiler plate application
License: TODO

Url: https://github.com/billyrayvalentine/python-template-app
Source0: https://github.com/billyrayvalentine/python-template-app/archive/template-app-%{version}.tar.gz
Requires: python3

%description
The longer description for out application

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -d /usr/local/%{name} -s /sbin/nologin -c "System user for %{name}" %{name}

%prep
# Archive does not have a sub directory so use setup -c
# See https://rpm-packaging-guide.github.io/#setup
%setup -c

%install
mkdir -p %{buildroot}/usr/local/%{name}
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/{%_sysconfdir}
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}/var/log/%{name}

chmod 0755 %{buildroot}/usr/local/%{name}
install -m 0644 src/*.py %{buildroot}/usr/local/%{name}
install -m 0644 template-app.conf %{buildroot}/%{_sysconfdir}
install -m 0644 %{name}.service %{buildroot}/%{_unitdir}
install -m 0644 %{name}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

%files
%defattr(-, root, root)
/usr/local/%{name}/*.py
%{_sysconfdir}/template-app.conf
%{_sysconfdir}/sysconfig
%_unitdir
%doc README.md 
%attr(0775,%{name},%{name}) /var/log/%{name}/

%changelog
* Sun Nov 17 2019 Billy Ray Valentine 
- Initial release
