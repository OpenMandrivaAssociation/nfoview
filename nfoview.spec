Name:           nfoview
Version:        1.14
Release:        1
Summary:        Simple viewer for NFO files

License:        GPLv3+
Group:          File tools
URL:            http://home.gna.org/nfoview/
Source0:        http://download.gna.org/nfoview/1.14/%{name}-%{version}.tar.xz
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

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a
text editor are preset font and encoding settings, automatic window
size and clickable hyperlinks.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}
%find_lang %{name}

%clean

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS NEWS README TODO
%{_bindir}/nfoview
%{py_puresitedir}/nfoview*
%{_datadir}/applications/nfoview.desktop
%{_mandir}/man1/nfoview.1*
%{_datadir}/nfoview
%{_datadir}/icons/hicolor/*/apps/nfoview.*
%{_datadir}/appdata/nfoview.appdata.xml
