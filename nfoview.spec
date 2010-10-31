Name:           nfoview
Version:        1.9.2
Release:        %mkrel 2
Summary:        Simple viewer for NFO files
License:        GPLv3+
Group:          File tools
URL:            http://home.gna.org/nfoview/
Source0:        http://download.gna.org/nfoview/1.9/nfoview-%{version}.tar.bz2
Requires:       pygtk2.0
Requires:       pygtk2.0-libglade
Suggests:       terminus-font
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python-devel
BuildRequires:  pygtk2.0
BuildRequires:  pygtk2.0-libglade
Requires(post): desktop-common-data
Requires(postun): desktop-common-data
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS NEWS README TODO
%{_bindir}/nfoview
%{python_sitelib}/nfoview*
%{_datadir}/applications/nfoview.desktop
%{_mandir}/man1/nfoview.1*
%{_datadir}/nfoview
%{_datadir}/icons/hicolor/*/apps/nfoview.*
