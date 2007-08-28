Summary:	Graphical tool to access EXIF extensions in JPEG files
Name:		gexif
Version:	0.5
Release:	%mkrel 12
License:	GPL
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif
Source:		http://belnet.dl.sourceforge.net/sourceforge/libexif/%{name}-%{version}.tar.bz2
# Bug #23536
Patch:		gexif-0.5-warning_non_fatal.patch
Requires:	popt
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	libexif-devel libexif-gtk-devel popt-devel pkgconfig libgtk+2.0-devel
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
#configure2_5x
%configure
%make

%install
rm -rf %{buildroot}

%makeinstall

# menu stuff
install -d %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(gexif): \
command="%{_bindir}/%{name}" \
title="GEXIF" \
longtitle="View and edit the info which digital cameras add to your photos" \
needs="x11" \
section="Multimedia/Graphics" \
icon="graphics_section.png" \
xdg="true"
EOF

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=GEXIF
Comment=View and edit the info which digital cameras add to your photos
Exec=%{_bindir}/%{name}
Icon=graphics_section.png
Terminal=false
Type=Application
Categories=Graphics;GTK;X-MandrivaLinux-Multimedia-Graphics;
EOF

%find_lang %{name}

%post
%update_menus
%update_desktop_database

%postun
%clean_menus
%clean_desktop_database

%clean
rm -fr %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_bindir}/%{name}
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop


