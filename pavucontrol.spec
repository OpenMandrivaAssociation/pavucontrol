%define name pavucontrol
%define version 0.9.6
%define rel 4
%define git 0
%if %{git}
%define release %mkrel 0.%{git}.%rel
%else
%define release %mkrel %rel
%endif

Summary: Volume control for Pulseaudio sound server for Linux
Name: %{name}
Version: %{version}
Release: %{release}
%if %{git}
Source0: %{name}-%{git}.tar.lzma
%else
Source0: %{name}-%{version}.tar.gz
%endif
Source1: %{name}-16.png
Source2: %{name}-32.png

Patch1:  0001-Merge-patch-from-sjoerd-that-adds-a-new-panel-for-li.patch
Patch2:  0002-move-the-lock-mute-buttons-to-the-same-spot-as-the-m.patch
Patch3:  0003-Remove-the-white-header-drop-all-references-to-Puls.patch
Patch4:  0004-Partial-commit-of-52abd202b521826eb95fd2d347a7eb5e2c.patch
Patch5:  0005-unclutter-UI-remove-redundant-hint-bar.patch
Patch6:  0006-switch-to-sink-page-by-default-if-no-streams-are-act.patch
Patch7:  0007-properly-initialize-source-output-type-dropdown-sho.patch
Patch8:  0008-move-no_xxx-labels-in-the-middle-of-the-dialogs.patch
Patch9:  0009-Also-point-the-minimalStreamWindow-downward.patch
Patch10: 0010-more-intelligent-initial-page-selection.patch
License: GPLv2+
Group: Sound
Url: http://0pointer.de/lennart/projects/pavucontrol
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkmm2.4-devel
BuildRequires: libglademm2.4-devel
BuildRequires: libpulseaudio-devel >= 0.9.7
BuildRequires: lynx
BuildRequires: desktop-file-utils
#BuildRequires: libcanberra-devel
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
%setup -q -n %{name}
%else
%setup -q
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

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

%if %mdkversion < 200900
%post
%update_desktop_database
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_desktop_database
%clean_menus
%endif

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


