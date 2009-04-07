Summary:	Graphical tool to access EXIF information in JPEG files
Name:		gexif
Version:	0.5
Release:	%mkrel 14
License:	LGPLv2+
Group:		Graphics
URL:		http://sourceforge.net/projects/libexif
Source:		http://belnet.dl.sourceforge.net/sourceforge/libexif/%{name}-%{version}.tar.bz2
# Bug #23536
Patch:		gexif-0.5-warning_non_fatal.patch
Requires:	popt

Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils

BuildRequires:	libexif-devel 
BuildRequires:	libexif-gtk-devel 
BuildRequires:	popt-devel 
BuildRequires:	pkgconfig 
BuildRequires:	libgtk+2.0-devel
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

