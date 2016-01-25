Summary:	Volume control for Pulseaudio sound server for Linux
Name:		pavucontrol
Version:	3.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://0pointer.de/lennart/projects/pavucontrol
Source0:	http://freedesktop.org/software/pulseaudio/pavucontrol/%{name}-%{version}.tar.xz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Patch0:		0000-i18n-Updated-Polish-translation.patch
Patch1:		0001-mainwindow-unavailable-profiles-are-marked-as-such-i.patch
Patch2:		0002-build-sys-Depend-on-libpulse-5.0.patch
Patch3:		0003-Add-version-command-line-option.patch
Patch4:		0004-i18n-Some-fixes-for-the-Italian-translation.patch
Patch5:		0005-i18n-improve-one-Italian-string.patch
Patch6:		0006-Remove-Encoding-key-from-.desktop-file.patch
Patch7:		0007-build-sys-Use-C-11-for-building.patch
BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	lynx
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libpulse)
Requires:	pulseaudio
Requires(post,postun):	desktop-file-utils
Provides:	pulseaudio-volume-control

%description
Pulseaudio Volume Control (pavucontrol) is a simple 
GTK based volume control tool for the Pulseaudio sound 
server. In contrast to classic mixer tools this one allows 
you to control both the volume of hardware devices and of 
each playback stream separately.

%prep
%setup -q
%apply_patches

%build
autoreconf -fiv

%configure
%make

%install
%makeinstall_std

sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
	--add-category="GTK" \
	--add-category="X-MandrivaLinux-Multimedia-Sound" \
	--add-category="X-MandrivaLinux-CrossDesktop" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
  
#icons install
install -D -m 0644 %SOURCE1 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 0644 %SOURCE2 %{buildroot}%{_iconsdir}/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.glade
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png

