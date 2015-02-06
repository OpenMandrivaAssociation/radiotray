Summary:	Radio Tray is a streaming player for listening to online radios
Name:		radiotray
Version:	0.7.3
Release:	2
Group:		Sound
License:	GPLv1
URL:		http://radiotray.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pyxdg
BuildRequires:	python-devel
Requires:	gstreamer0.10-python
Requires:	pygtk2
Requires:	python-lxml
Requires:	python-pyinotify
BuildArch:	noarch 

%description
Radio Tray is an online radio streaming player that runs on a Linux system
tray. Its goal is to have the minimum interface possible, making it very
straightforward to use. Radio Tray is not a full featured music player,
there are plenty of excellent music players already. However, there was a
need for a simple application with minimal interface just to listen to online
radios. And that's the sole purpose of Radio Tray.

%prep
%setup -q
sed -i -e '/^#!\//, 1d' src/radiotray.py

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/radiotray.desktop
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_docdir}/%{name}-%{version}/*
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*egg-info


%changelog
* Tue Aug 14 2012 Denis Silakov <dsilakov@mandriva.org> 0.7.3-1
+ Revision: 814781
- Updated to version 0.7.3

* Tue May 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.2-1
+ Revision: 801134
- imported package radiotray


* Wed Oct 26 2011  Matthew Dawkins <mdawkins@unity-linux.org> 0.6.4-1-unity2011
- new version 0.6.4

* Mon Mar 21 2011 mdawkins <mattydaw@gmail.com> 0.6.3-2-unity2011
- rebuild

* Mon Feb 07 2011 KDulcimer <kdulcimer@unity-linux.org> 0.6.3-1
- 0.6.3 (autoupdatebot)

* Thu Sep 23 2010 KDulcimer <kdulcimer@unity-linux.org> 0.6-1
- Import to Unity Linux
- 0.6.1

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul  8 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.6-1
- Update to new upstream version

* Tue May 25 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.1-3
- Change license to match COPYING
- Add comments to SPEC file
- Add comment for the explicit dependencies

* Fri May  7 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.1-2
- Fix as per the recommendations of bug #583102
- Change the python_sitelib definition to the new way of doing it for >F-12
- Add build CFLAGS
- Use the __python macro
- Make some modifications to help not break when python version change

* Wed Apr 14 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.5.1-1
- Initial build for Fedora
