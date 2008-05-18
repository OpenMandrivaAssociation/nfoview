Name:           nfoview
Version:        1.2
Release:        %mkrel 1
Summary:        Simple viewer for NFO files
License:        GPLv3+
Group:          File tools
URL:            http://home.gna.org/nfoview/
Source0:        http://download.gna.org/nfoview/%{version}/nfoview-%{version}.tar.bz2
Source1:        http://download.gna.org/nfoview/%{version}/nfoview-%{version}.tar.bz2.sig
Source2:        http://download.gna.org/nfoview/%{version}/nfoview-%{version}.md5sum
Requires:       pygtk2.0
Requires:       pygtk2.0-libglade
Suggests:       terminus-font
Requires(post): desktop-common-data
Requires(postun): desktop-common-data
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python-devel
BuildRequires:  pygtk2.0
BuildRequires:  pygtk2.0-libglade
%{py_requires}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
%find_lang %{name}
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/nfoview.desktop

%clean
%{__rm} -rf %{buildroot}

%post
%{update_mime_database}
%{update_desktop_database}
%{update_menus}

%postun
%{clean_mime_database}
%{clean_desktop_database}
%{clean_menus}

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS PKG-INFO README TODO
%attr(0755,root,root) %{_bindir}/nfoview
%{python_sitelib}/nfoview*
%{_datadir}/applications/nfoview.desktop
%{_mandir}/man1/nfoview.1*
%{_datadir}/nfoview
