Name:           libopenshot-audio
Version:        0.2.2
Release:        1%{?dist}
Summary:        Audio library used by OpenShot

License:        GPLv3+
URL:            http://openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Disabling libopenshot-audio due to libopenshot exclusion, see rfbz #5528
ExcludeArch:    ppc64le

BuildRequires:  gcc-c++
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  alsa-lib-devel
BuildRequires:  zlib-devel

%description
OpenShot Audio Library (libopenshot-audio) is an open-source 
project powered by JUCE, and enables high-quality audio editing 
and playback for libopenshot.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake3
%cmake3_build


%install
%cmake3_install

%if 0%{?rhel} && 0%{?rhel} <= 7
  %ldconfig_scriptlets
%endif

%files
%doc AUTHORS COPYING README.md
%{_libdir}/%{name}.so.*

%files devel
%doc
%{_bindir}/openshot-audio-demo
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/cmake/OpenShotAudio/
%{_mandir}/man1/openshot-audio-demo.1*


%changelog
* Tue Sep 07 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.2-1
- New upstream release

* Thu Aug 26 2021 Leigh Scott <leigh123linux@gmail.com> - 0.2.1-1
- New upstream release

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Aug 04 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.2.0-2
- Update build configs for Fedora 33

* Sat Mar 07 2020 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.0-1
- New upstream release

* Thu Feb 13 2020 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.9-1
- New upstream release

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.8-4.20190405git7001b68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.8-3.20190405git7001b68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.8-2
- Upgrade to latest git revision, to fix FTBFS with GCC9 on Fedora 30
- libopenshot-audio upgraded to JUCE 5.4.3 internally
- Drop patches upstreamed or made unnecessary by JUCE update

* Fri Mar 22 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.8-1
- New upstream release

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.7-2
- Update patch to completely remove Xinerama dependency

* Mon Sep 24 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.7-1
- New upstream release

* Tue Jul 31 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.6-1
- New upstream release

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Richard Shaw <hobbes1069@gmail.com> - 0.1.5-1
- Update to latest upstream release.

* Sat Sep 02 2017 Sérgio Basto <sergio@serjux.com> - 0.1.4-1
- Update libopenshot-audio to 0.1.4

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.2-1
- Update to latest upstream release.

* Fri Apr  8 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-1
- Update to latest upstream release.

* Mon Nov 16 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.6-1
- Update to latest upstream release.

* Thu Jun 25 2015 Sérgio Basto <sergio@serjux.com> - 0.0.4-2
- Fixed unused-direct-shlib-dependency in cmake with global optflags.

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.0.4-1
- New upstream release 0.0.4

* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
