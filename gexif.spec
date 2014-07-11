Summary:	Graphical tool to access EXIF information in JPEG files
Name:		gexif
Version:	0.5
Release:	26
License:	LGPLv2+
Group:		Graphics
Url:		http://sourceforge.net/projects/libexif
Source0:	http://belnet.dl.sourceforge.net/sourceforge/libexif/%{name}-%{version}.tar.bz2
# Bug #23536
Patch0:		gexif-0.5-warning_non_fatal.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libexif-gtk)
BuildRequires:	pkgconfig(popt)
Requires(post,postun):	desktop-file-utils

%description
Most digital cameras produce EXIF files, which are JPEG files with extra tags
that contain information about the image. The EXIF library allows you to parse
an EXIF file and read the data from those tags.

This package contains a graphical frontend for the EXIF library.

%prep
%setup -q
%apply_patches

# Make gexif compile with GTK 2.4.x or newer
perl -n -i -e '/^\s*-DGTK_DISABLE_DEPRECATED\b.*$/ || print $_' gexif/Makefile*

%build
%configure2_5x
%make

%install
%makeinstall_std

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

