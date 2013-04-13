Summary:	Graphical tool to access EXIF information in JPEG files
Name:		gexif
Version:	0.5
Release:	20
License:	LGPLv2+
Group:		Graphics
URL:		http://sourceforge.net/projects/libexif
Source:		http://belnet.dl.sourceforge.net/sourceforge/libexif/%{name}-%{version}.tar.bz2
# Bug #23536
Patch:		gexif-0.5-warning_non_fatal.patch

Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils

BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libexif-gtk)
BuildRequires:	popt-devel 
BuildRequires:	pkgconfig 
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Most digital cameras produce EXIF files, which are JPEG files with extra tags
that contain information about the image. The EXIF library allows you to parse
an EXIF file and read the data from those tags.

This package contains a graphical frontend for the EXIF library.

%prep

%setup -q
%patch -p1 -b .warning_non_fatal

# Make gexif compile with GTK 2.4.x or newer
perl -n -i -e '/^\s*-DGTK_DISABLE_DEPRECATED\b.*$/ || print $_' gexif/Makefile*

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gexif
Comment=Access EXIF information from pictures
Exec=%{_bindir}/%{name}
Icon=graphics_section
Terminal=false
Type=Application
Categories=Graphics;GTK;
EOF

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%clean
rm -fr %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5-19mdv2011.0
+ Revision: 664825
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-18mdv2011.0
+ Revision: 605448
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-17mdv2010.1
+ Revision: 522720
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5-16mdv2010.0
+ Revision: 424872
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5-15mdv2010.0
+ Revision: 424838
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.5-14mdv2009.1
+ Revision: 364957
- use standard configure2_5x

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.5-14mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.5-14mdv2008.1
+ Revision: 150104
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.5-13mdv2008.0
+ Revision: 91188
- rebuild for 2008
- don't package COPYING
- correct new menu
- drop old menu
- correct license, new license policy
- spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Mar 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-12mdv2007.1
+ Revision: 148365
- fix the xdg menu stuff

* Mon Jan 15 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.5-11mdv2007.1
+ Revision: 109335
- Use mkrel macro for release.
- Added patch warning_non_fatal. Closes #23536
  Warnings are Warnings, not Fatal errors.
- Import gexif

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.5-10mdk
- Rebuild

* Wed Mar 16 2005 Till Kamppeter <till@mandrakesoft.com> 0.5-9mdk
- Shorter menu entry.

* Sat Nov 27 2004 Till Kamppeter <till@mandrakesoft.com> 0.5-8mdk
- Rebuilt for libexif12-0.6.11 and libexif-gtk5-0.3.5.

