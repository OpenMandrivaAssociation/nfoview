Name:           nfoview
Version:        1.9.5
Release:        %mkrel 1
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


%changelog
* Sun May 29 2011 Jani Välimaa <wally@mandriva.org> 1.9.5-1mdv2011.0
+ Revision: 681714
- update to new version 1.9.5

* Tue Apr 05 2011 Jani Välimaa <wally@mandriva.org> 1.9.4-1
+ Revision: 650731
- update to new version 1.9.4

* Sun Mar 27 2011 Jani Välimaa <wally@mandriva.org> 1.9.3-1
+ Revision: 648604
- update to new version 1.9.3

* Sun Oct 31 2010 Jani Välimaa <wally@mandriva.org> 1.9.2-2mdv2011.0
+ Revision: 590974
- drop py_requires macro
- drop support for old (2008.1 and older) mdv releases
- rebuild for new python 2.7

* Tue Oct 05 2010 Jani Välimaa <wally@mandriva.org> 1.9.2-1mdv2011.0
+ Revision: 583131
- update to new version 1.9.2

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 1.9.1-1mdv2011.0
+ Revision: 550036
- new version 1.9.1

* Sun Apr 25 2010 Jani Välimaa <wally@mandriva.org> 1.9-1mdv2010.1
+ Revision: 538523
- update to new version 1.9

* Fri Nov 06 2009 Jani Välimaa <wally@mandriva.org> 1.8-1mdv2010.1
+ Revision: 461168
- new version 1.8

* Sun Sep 27 2009 Jani Välimaa <wally@mandriva.org> 1.7-1mdv2010.0
+ Revision: 449724
- update to version 1.7

* Sun Aug 16 2009 Jani Välimaa <wally@mandriva.org> 1.6-1mdv2010.0
+ Revision: 417025
- update to new version 1.6

* Tue Jun 02 2009 Jani Välimaa <wally@mandriva.org> 1.5-1mdv2010.0
+ Revision: 382281
- New version 1.5
- Removed unneeded sources

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 332873
- New upstream release

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.2-4mdv2009.1
+ Revision: 325768
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.2-3mdv2009.0
+ Revision: 268277
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 19 2008 David Walluck <walluck@mandriva.org> 1.2-2mdv2009.0
+ Revision: 208852
- spec cleanup

* Mon May 19 2008 David Walluck <walluck@mandriva.org> 1.2-1mdv2009.0
+ Revision: 208830
- 1.2

* Sat May 10 2008 Anssi Hannula <anssi@mandriva.org> 1.1.2-1mdv2009.0
+ Revision: 205369
- new version
- drop fix-build-without-x.patch, fixed upstream

* Wed May 07 2008 Anssi Hannula <anssi@mandriva.org> 1.1.1-1mdv2009.0
+ Revision: 203749
- do not reference nfoview for __version__ in setup.py to allow building
  without X (fix-build-without-x.patch)
- initial Mandriva release

