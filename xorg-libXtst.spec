Summary:	X tst library
Name:		xorg-libXtst
Version:	1.2.2
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXtst-%{version}.tar.bz2
# Source0-md5:	25c6b366ac3dc7a12c5d79816ce96a59
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X tst extension library.

%package devel
Summary:	Header files for libXtst library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X extension library.

This package contains the header files needed to develop programs that
use libXtst.

%prep
%setup -qn libXtst-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXtst.so.?
%attr(755,root,root) %{_libdir}/libXtst.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXtst.so
%{_includedir}//X11/extensions/*.h
%{_pkgconfigdir}/xtst.pc

