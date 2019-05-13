%global gitrev 7001b68787c0881a44bcafba98cccae509a31644
%global shortrev %(c=%{gitrev}; echo ${c:0:7})
%global gitdate 20190405

Name:           libopenshot-audio
Version:        0.1.8
Release:        2.%{gitdate}git%{shortrev}%{?dist}
Summary:        Audio library used by OpenShot

License:        GPLv3+
URL:            http://openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/%{gitrev}.tar.gz#/%{name}-%{shortrev}.tar.gz

# No longer necessary with JUCE 5.4.3 configuration
#Patch0:	libopenshot-audio-noXinerama.patch
# Upstreamed
#Patch1:	libopenshot-audio-isfinite.patch

# Fix cmake configuration to remove X11 dependency
Patch2:		libopenshot-audio-noX11.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  alsa-lib-devel
BuildRequires:  zlib-devel
# Graphical dependencies in JUCE code removed upstream
#BuildRequires:  freetype-devel
#BuildRequires:  libX11-devel
#BuildRequires:  libXcursor-devel
#BuildRequires:  libXrandr-devel
#BuildRequires:  libXinerama-devel

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
%autosetup -p1 -n %{name}-%{gitrev}


%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake3 .
make %{?_smp_mflags}


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README.md
%{_libdir}/*.so.*

%files devel
%doc
%{_bindir}/openshot-audio-test-sound
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man1/*.1*


%changelog
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
