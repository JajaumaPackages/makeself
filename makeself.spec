Name:           makeself
Version:        2.3.1
Release:        1%{?dist}
BuildArch:      noarch
Summary:        Make self-extractable archives on Unix
Group:          Development/Tools

License:        GPLv2+
URL:            http://%{name}.io/
Source:         http://github.com/megastep/%{name}/archive/release-%{version}.tar.gz

# This patch changes the path to the sourced header script
Patch0:         move_header.patch

BuildRequires:  %{_bindir}/iconv

Recommends:     gnupg
Recommends:     openssl


%description
makeself.sh is a shell script that generates a self-extractable
tar.gz archive from a directory. The resulting file appears as a shell
script, and can be launched as is. The archive will then uncompress
itself to a temporary directory and an arbitrary command will be
executed (for example an installation script). This is pretty similar
to archives generated with WinZip Self-Extractor in the Windows world.


%prep
%setup -q -n %{name}-release-%{version}
%patch0


%build
iconv --from-code=ISO-8859-1 --to-code=UTF-8 %{name}.1 | gzip > %{name}.1.gz


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_mandir}/man1

install -p -m755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -p -m644 %{name}-header.sh %{buildroot}%{_libexecdir}
install -p -m644 %{name}.1.gz %{buildroot}%{_mandir}/man1


%files
%doc README.md COPYING %{name}.lsm
%{_mandir}/man1/*
%{_libexecdir}/*
%{_bindir}/*


%changelog
* Mon Aug 21 2017 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 2.3.1-1
- Bump version to 2.3.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 2.3.0-1
- Bump version to 2.3.0
- Update the URL
- Rename the patch
- Use more macros
- Require iconv
- Install the LSM file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 2.2.0-2
- Preserve timestamps during installation

* Sun Jul 07 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 2.2.0-1
- GPLv2 license update

* Mon Jun 24 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 2.2.0-1
- Initial spec
