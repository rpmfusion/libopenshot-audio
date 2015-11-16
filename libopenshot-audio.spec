Name:           libopenshot-audio
Version:        0.0.6
Release:        1%{?dist}
Summary:        Audio library used by OpenShot

License:        GPLv3+
URL:            http://openshot.org/
Source0:        https://launchpad.net/libopenshot/0.0/%{version}/+download/%{name}-%{version}.tar.gz

Patch0:         libopenshot-audio-0.0.3-libs.patch

BuildRequires:  cmake
BuildRequires:  freetype-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcursor-devel

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
* Mon Nov 16 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.6-1
- Update to latest upstream release.

* Thu Jun 25 2015 Sérgio Basto <sergio@serjux.com> - 0.0.4-2
- Fixed unused-direct-shlib-dependency in cmake with global optflags.

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.0.4-1
- New upstream release 0.0.4

* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
