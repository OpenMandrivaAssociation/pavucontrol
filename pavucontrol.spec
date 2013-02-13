Summary:	Volume control for Pulseaudio sound server for Linux
Name:		pavucontrol
Version:	1.0
Release:	1
Source0:	http://freedesktop.org/software/pulseaudio/pavucontrol/%{name}-%{version}.tar.xz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
License:	GPLv2+
Group:		Sound
Url:		http://0pointer.de/lennart/projects/pavucontrol
BuildRequires:	gtkmm3.0-devel
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	lynx
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk-devel
Requires:	pulseaudio
Requires(post):	desktop-file-utils
Requires(postun):desktop-file-utils

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
%configure2_5x
%make

%install
%makeinstall_std

sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.glade
%{_iconsdir}/hicolor/*/apps/%{name}.*

%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-8mdv2011.0
+ Revision: 666992
- mass rebuild

* Wed Dec 22 2010 Colin Guthrie <cguthrie@mandriva.org> 0.9.10-7mdv2011.0
+ Revision: 623825
- Fix a bug where source outputs had mute and channel lock buttons which were pointless.

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-6mdv2011.0
+ Revision: 607075
- rebuild

  + John Balcaen <mikala@mandriva.org>
    - Fix BR for libcanberra-gtk-devel

* Thu Apr 22 2010 Colin Guthrie <cguthrie@mandriva.org> 0.9.10-5mdv2010.1
+ Revision: 537766
- Fix format string stuff
- Save/restore window size and add a --tab command line arg

* Tue Apr 20 2010 Colin Guthrie <cguthrie@mandriva.org> 0.9.10-4mdv2010.1
+ Revision: 537269
- Allow reconnections after PA server goes away.
- Fix display bug with recording streams

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-3mdv2010.1
+ Revision: 523592
- rebuilt for 2010.1

* Sat Oct 17 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.10-2mdv2010.0
+ Revision: 458029
- Fix the peak detect code to survive a stream move.

* Wed Oct 14 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.10-1mdv2010.0
+ Revision: 457466
- New version

* Sat Oct 03 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.9-3mdv2010.0
+ Revision: 452940
- Fix some UI problems relating to showing sound event widgets/focus stealing and relative scale adjustments

* Sun Sep 20 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.9-2mdv2010.0
+ Revision: 445924
- Patch for latest PA with updated device-manager patch

* Thu Sep 10 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.9-1mdv2010.0
+ Revision: 436469
- New version: 0.9.9
- Rebase my history branch and regenerate patch

* Wed Jul 08 2009 Götz Waschk <waschk@mandriva.org> 0.9.9-0.test1.1mdv2010.0
+ Revision: 393576
- new version
- drop patch 1

* Sun Jun 28 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-6mdv2010.0
+ Revision: 390223
- Add support for module-device-manager

* Sat Jun 27 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-5mdv2010.0
+ Revision: 390116
- Another attack from the Lesser Spotted Package Eating Monster...
- Add support for changing sink/source ports

* Fri Jun 26 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-3mdv2010.0
+ Revision: 389416
- Update the UI rework changes.

* Sat Jun 13 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-2mdv2010.0
+ Revision: 385746
- Update my UI patch.

* Tue Apr 14 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-1mdv2009.1
+ Revision: 366882
- New version 0.9.8
- Rebase ui branch patches on current upstream

* Wed Mar 25 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-0.20090325.1mdv2009.1
+ Revision: 361208
- Update to my ui branch rework which is hopefully going to be merged upstream soon.

* Fri Mar 06 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-0.20090302.2mdv2009.1
+ Revision: 349716
- Newer snapshot + rebuild for new pulse

* Mon Mar 02 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-0.20090302.1mdv2009.1
+ Revision: 347536
- New snapshot including profile switching support

* Wed Feb 04 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-0.20080204.1mdv2009.1
+ Revision: 337549
- Update to git master to work with newer PA without crashing with some stream dbs

* Sat Oct 11 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.7-1mdv2009.1
+ Revision: 292134
- Add buildrequire for intltool
- Add buildrequires for libcanberra
- New version 0.9.7
- Drop upstream patches

* Fri Sep 12 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.6-4mdv2009.0
+ Revision: 284340
- Regenerate upstream patches from git rather than legacy svn
- Add a few more upstream cherry picks (basically all the ones that are not for PA >0.9.10)
- Change the spec slightly in preparation for future upgrade to 0.9.7

  + Götz Waschk <waschk@mandriva.org>
    - fix license

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.9.6-3mdv2009.0
+ Revision: 265333
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Apr 21 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.6-2mdv2009.0
+ Revision: 196338
- Add some upstream improvements

* Sat Mar 29 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.6-1mdv2008.1
+ Revision: 191088
- New release: 0.9.7

* Thu Jan 31 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.5-4mdv2008.1
+ Revision: 160893
- Fix %%postun (#37210)

* Wed Jan 16 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.5-3mdv2008.1
+ Revision: 153654
- Fix %%post[un] macros

* Tue Jan 15 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.5-2mdv2008.1
+ Revision: 151972
- Add icons for x-desktop use (MDV#36579)
- Add x-desktop category
- Add BuildRequires on libpulse-devel >= 0.9.7

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.5-1mdv2008.1
+ Revision: 103905
- New version

* Tue Aug 21 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.4-2mdv2008.0
+ Revision: 68116
- Fix Move Stream left mouse handling


* Mon Feb 05 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.4-1mdv2007.0
+ Revision: 116259
- Import pavucontrol

* Mon Aug 28 2006 Götz Waschk <waschk@mandriva.org> 0.9.4-1mdv2007.0
- bump deps
- New release 0.9.4

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 0.9.3-1mdv2007.0
- rebuild for new cairomm

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 0.9.3-1
- New release 0.9.3

* Tue Jul 11 2006 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2007.0
- update deps
- New release 0.9.2

* Sat Jun 17 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-4mdv2007.0
- fix menu
- fix buildrequires

* Fri Jun 16 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-3mdv2007.0
- fix buildrequires

* Sat Jun 10 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-2mdv2007.0
- fix menu
- fix deps

* Tue Jun 06 2006 Jerome Soyer <saispo@mandriva.org> 0.9.1-1mdv2007.0
- Fix Provides
- Fix Menu
- New release 0.9.1

* Mon Jun 05 2006 Jerome Soyer <saispo@mandriva.org> 0.9.0-1mdv2007.0
- Initial Package for Mandriva

