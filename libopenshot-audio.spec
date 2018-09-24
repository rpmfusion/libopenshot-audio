Name:           libopenshot-audio
Version:        0.1.7
Release:        2%{?dist}
Summary:        Audio library used by OpenShot

License:        GPLv3+
URL:            http://openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         libopenshot-audio-noXinerama.patch
Patch1:         libopenshot-audio-isfinite.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  freetype-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXrandr-devel

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
%setup -q
%patch0 -p1 -b .libs
%patch1 -p1 -b .finite


%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake .
make %{?_smp_mflags}


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%doc
%{_bindir}/openshot-audio-test-sound
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man1/*.1*


%changelog
* Mon Sep 24 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.7-2
- Update patch to completely remove Xinerama dependency

* Mon Sep 24 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.7-1
- New upstream release

* Tue Jul 31 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.1.6-1
- New upstream release

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
