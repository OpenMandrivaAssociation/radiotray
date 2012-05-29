Summary:	Radio Tray is a streaming player for listening to online radios
Name:		radiotray
Version:	0.7.2
Release:	1
BuildArch:	noarch 
Group:		Sound
License:	GPLv1
URL:		http://radiotray.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pyxdg
BuildRequires:	python-devel

# Explicit dependencies required because there is no automatic dependencies
# resolution for the python modules.
Requires:	gstreamer0.10-python
Requires:	pygtk2
Requires:	python-lxml
Requires:	python-pyinotify

%description
Radio Tray is an online radio streaming player that runs on a Linux system
tray. Its goal is to have the minimum interface possible, making it very
straightforward to use. Radio Tray is not a full featured music player,
there are plenty of excellent music players already. However, there was a
need for a simple application with minimal interface just to listen to online
radios. And that's the sole purpose of Radio Tray.

%prep
%setup -q

# Remove unnecessary shebang
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

