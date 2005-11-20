Summary:	Enlightenment Widget Library
Summary(pl):	Biblioteka widgetów Enlightenmenta (Enlightenment Widget Library)
Name:		ewl
Version:	0.0.4.004
%define	_snap	20051118
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/libs/%{name}-%{_snap}.tar.bz2
# Source0-md5:	f5b5701f01006e88ace5f7339403615e
URL:		http://enlightenment.org/Libraries/Ewl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EWL is a widget library which uses the E Foundation Libraries (EFL).

%description -l pl
EWL to biblioteka widgetów u¿ywaj±ca EFL (E Foundation Libraries -
podstawowych bibliotek Englightenmenta).

%package libs
Summary:	EWL library
Group:		X11/Libraries

%description libs
EWL library.

%package devel
Summary:	EWL header files and test programs
Summary(pl):	Pliki nag³ówkowe i programy testowe dla biblioteki EWL
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
EWL header files and test programs.

%description devel -l pl
Pliki nag³ówkowe i programy testowe dla biblioteki EWL.

%package static
Summary:	Static EWL library
Summary(pl):	Statyczna biblioteka EWL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EWL library.

%description static -l pl
Statyczna biblioteka EWL.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* NEWS README TODO
%attr(755,root,root) %{_bindir}/ewl_test
%attr(755,root,root) %{_bindir}/ewl_*_test
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ewl-config
%attr(755,root,root) %{_libdir}/libewl.so
%{_libdir}/libewl.la
%dir %{_includedir}/ewl
%{_includedir}/ewl/Ewl.h
%{_includedir}/ewl/ewl_*.h
%{_pkgconfigdir}/ewl.pc
%{_aclocaldir}/ewl.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libewl.a
