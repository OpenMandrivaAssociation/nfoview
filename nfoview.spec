
Name:			nfoview
Version:		1.1.1
Release:		%mkrel 1

Summary:        Simple viewer for NFO files
License:        GPLv3+
Group:          File tools
URL:            http://home.gna.org/nfoview/
Source0:        http://download.gna.org/nfoview/1.1/%{name}-%{version}.tar.gz

BuildRequires:  python
BuildRequires:	pygtk2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%{py_requires}
Requires:	pygtk2.0
Suggests:	terminus-font

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a
text editor are preset font and encoding settings, automatic window
size and clickable hyperlinks.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%find_lang %name

%clean
rm -rf %{buildroot}

%post
%{update_mime_database}
%{update_desktop_database}
%{update_menus}

%postun
%{clean_mime_database}
%{clean_desktop_database}
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/nfoview
%{python_sitelib}/nfoview*
%{_datadir}/applications/nfoview.desktop
%{_mandir}/man1/nfoview.1*
%{_datadir}/mime/packages/nfoview.xml
%{_datadir}/nfoview
