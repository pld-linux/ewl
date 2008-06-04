#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		ecore_ver	0.9.9.043
%define		edje_ver	0.9.9.043
%define		efreet_ver	0.5.0.043
%define		emotion_ver	0.1.0.042
%define		epsilon_ver	0.3.0.012
%define		evas_ver	0.9.9.043

Summary:	Enlightenment Widget Library
Summary(pl.UTF-8):	Biblioteka widgetów Enlightenmenta (Enlightenment Widget Library)
Name:		ewl
Version:	0.5.2.042
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/snapshots/2008-01-25/%{name}-%{version}.tar.bz2
# Source0-md5:	c25a57cdee3e58b016ad8ad5e0767902
URL:		http://enlightenment.org/p.php?p=about/libs/ewl
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
# ecore-file ecore-txt
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	edje >= %{edje_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	efreet-devel >= %{efreet_ver}
BuildRequires:	emotion-devel >= %{emotion_ver}
BuildRequires:	epsilon-devel >= %{epsilon_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
EWL is a widget library which uses the E Foundation Libraries (EFL).

%description -l pl.UTF-8
EWL to biblioteka widgetów używająca EFL (E Foundation Libraries -
podstawowych bibliotek Englightenmenta).

%package libs
Summary:	EWL library
Summary(pl.UTF-8):	Biblioteka EWL
Group:		Libraries
Requires:	ecore-file >= %{ecore_ver}
Requires:	ecore-txt >= %{ecore_ver}
Requires:	edje-libs >= %{edje_ver}
Requires:	efreet >= %{efreet_ver}
Requires:	emotion >= %{emotion_ver}
Requires:	epsilon-libs >= %{epsilon_ver}
Requires:	evas >= %{evas_ver}

%description libs
EWL library.

%description libs -l pl.UTF-8
Biblioteka EWL.

%package devel
Summary:	EWL header files and test programs
Summary(pl.UTF-8):	Pliki nagłówkowe i programy testowe dla biblioteki EWL
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# ecore-file ecore-txt
Requires:	ecore-devel >= %{ecore_ver}
Requires:	edje-devel >= %{edje_ver}
Requires:	efreet-devel >= %{efreet_ver}
Requires:	emotion-devel >= %{emotion_ver}
Requires:	epsilon-devel >= %{epsilon_ver}
Requires:	evas-devel >= %{evas_ver}

%description devel
EWL header files and test programs.

%description devel -l pl.UTF-8
Pliki nagłówkowe i programy testowe dla biblioteki EWL.

%package static
Summary:	Static EWL library
Summary(pl.UTF-8):	Statyczna biblioteka EWL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EWL library.

%description static -l pl.UTF-8
Statyczna biblioteka EWL.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/ewl_config
%attr(755,root,root) %{_bindir}/ewl_test
%attr(755,root,root) %{_bindir}/ewl_embed_test
%attr(755,root,root) %{_bindir}/ewl_simple_test
%dir %{_sysconfdir}/ewl
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ewl/ewl.cfg
%dir %{_libdir}/%{name}/tests
%attr(755,root,root) %{_libdir}/%{name}/tests/ewl_*.so
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libewl.so.1
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/engines
# missing -avoid-version
%attr(755,root,root) %{_libdir}/%{name}/engines/*.so*
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/ewl_io_manager_*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewl.so
%{_libdir}/libewl.la
%dir %{_includedir}/ewl
%{_includedir}/ewl/Ewl.h
%{_includedir}/ewl/Ewl_Test.h
%{_includedir}/ewl/ewl_*.h
%{_pkgconfigdir}/ewl.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libewl.a
%endif
