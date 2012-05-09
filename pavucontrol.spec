%define name pavucontrol
%define version 1.0
%define git 0
%define rel 2
%if %{git}
%define rel 0.%{git}.%rel
%endif

%define release %mkrel %rel

Summary: Volume control for Pulseaudio sound server for Linux
Name: %{name}
Version: %{version}
Release: %{release}
%if %{git}
Source0: %{name}-%{git}.tar.xz
%else
Source0: %{name}-%{version}.tar.xz
%endif
Source1: %{name}-16.png
Source2: %{name}-32.png

License: GPLv2+
Group: Sound
Url: http://0pointer.de/lennart/projects/pavucontrol
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkmm3.0-devel
BuildRequires: libglademm2.4-devel
BuildRequires: libpulseaudio-devel >= 0.99.1
BuildRequires: lynx
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libcanberra-gtk-devel
Requires: pulseaudio
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Provides: pulseaudio-volume-control

%description
Pulseaudio Volume Control (pavucontrol) is a simple 
GTK based volume control tool for the Pulseaudio sound 
server. In contrast to classic mixer tools this one allows 
you to control both the volume of hardware devices and of 
each playback stream separately.

%prep
%if %{git}
%setup -q -n %{name}-%{git}
%else
%setup -q
%endif

%apply_patches

%build
%if %{git}
echo "clean:" > Makefile
./bootstrap.sh -V
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

# Icons
install -D -m 0644 %SOURCE1 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 0644 %SOURCE2 %{buildroot}%{_iconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/%name
%{_datadir}/applications/%name.desktop
%{_datadir}/%name/%name.glade
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png




