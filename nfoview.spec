Name:           nfoview
Version:        1.27.1
Release:        1
Summary:        Simple viewer for NFO files

License:        GPLv3+
Group:          File tools
URL:            https://otsaloma.io/nfoview/
Source0:        https://github.com/otsaloma/nfoview/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python

Requires:       python3dist(pygobject)
Recommends:     terminus-font

BuildArch:      noarch

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a
text editor are preset font and encoding settings, automatic window
size and clickable hyperlinks.

%prep
%setup -q

%build
%py_build

%install
%py_install

%find_lang %{name}

%clean

%files -f %{name}.lang
%doc AUTHORS.md NEWS.md README.md TODO.md
%{_bindir}/nfoview
%{python_sitelib}/nfoview*
%{_datadir}/applications/io.otsaloma.nfoview.desktop
%{_mandir}/man1/nfoview.1*
%{_datadir}/nfoview/
%{_datadir}/icons/hicolor/*/apps/io.otsaloma.nfoview{,-symbolic}.*
%{_metainfodir}/io.otsaloma.nfoview.appdata.xml
