Summary:	Volume control for Pulseaudio sound server for Linux
Name:		pavucontrol
Version:	6.0
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://0pointer.de/lennart/projects/pavucontrol
Source0:	https://freedesktop.org/software/pulseaudio/pavucontrol/%{name}-%{version}.tar.xz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
BuildRequires:	meson
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	lynx
BuildRequires:	pkgconfig(gtkmm-4.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(json-glib-1.0)
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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/org.pulseaudio.pavucontrol.desktop
sed -i "s@^Exec=.*@Exec=%{_bindir}/%{name}-gtk@" %{buildroot}%{_datadir}/applications/org.pulseaudio.pavucontrol.desktop

desktop-file-install --vendor="" \
	--add-category="GTK" \
	--add-category="X-MandrivaLinux-Multimedia-Sound" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
  
#icons install
install -D -m 0644 %SOURCE1 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 0644 %SOURCE2 %{buildroot}%{_iconsdir}/%{name}.png

# rename so pavucontrol-qt can take over
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-gtk
rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc README LICENSE
%{_bindir}/%{name}-gtk
%{_datadir}/applications/org.pulseaudio.pavucontrol.desktop
%{_datadir}/%{name}/%{name}.glade
%{_metainfodir}/org.pulseaudio.pavucontrol.metainfo.xml
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
