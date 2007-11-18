#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightenment Widget Library
Summary(pl.UTF-8):	Biblioteka widgetów Enlightenmenta (Enlightenment Widget Library)
Name:		ewl
Version:	0.5.1.008
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	d660de3d11b0b3219634c6736fe975fd
URL:		http://enlightenment.org/p.php?p=about/libs/ewl
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4
# ecore-file ecore-txt
BuildRequires:	ecore-devel >= 0.9.9.038
BuildRequires:	edje >= 0.5.0.038
BuildRequires:	edje-devel >= 0.5.0.038
BuildRequires:	efreet-devel >= 0.0.3
BuildRequires:	emotion-devel >= 0.0.1
BuildRequires:	epsilon-devel >= 0.3.0.008
BuildRequires:	evas-devel >= 0.9.9.038
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
Requires:	ecore-file >= 0.9.9.038
Requires:	ecore-txt >= 0.9.9.038
Requires:	edje-libs >= 0.5.0.038
Requires:	efreet >= 0.0.3
Requires:	emotion >= 0.0.1
Requires:	epsilon-libs >= 0.3.0.008
Requires:	evas >= 0.9.9.038

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
Requires:	ecore-devel >= 0.9.9.038
Requires:	edje-devel >= 0.5.0.038
Requires:	efreet-devel >= 0.0.3
Requires:	emotion-devel >= 0.0.1
Requires:	epsilon-devel >= 0.3.0.008
Requires:	evas-devel >= 0.9.9.038

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
%doc AUTHORS COPYING NEWS README TODO
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
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/engines
# missing -avoid-version
%attr(755,root,root) %{_libdir}/%{name}/engines/*.so*
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/ewl_io_manager_*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ewl-config
%attr(755,root,root) %{_libdir}/libewl.so
%{_libdir}/libewl.la
%dir %{_includedir}/ewl
%{_includedir}/ewl/Ewl.h
%{_includedir}/ewl/Ewl_Test.h
%{_includedir}/ewl/ewl_*.h
%{_pkgconfigdir}/ewl.pc
%{_aclocaldir}/ewl.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libewl.a
%endif
