#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightenment Widget Library
Summary(pl.UTF-8):	Biblioteka widgetów Enlightenmenta (Enlightenment Widget Library)
Name:		ewl
Version:	0.0.4.007
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	29bc8aec80b53480c2ea53aea1796e15
URL:		http://enlightenment.org/Libraries/Ewl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	libtool
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

%description libs
EWL library.

%description libs -l pl.UTF-8
Biblioteka EWL.

%package devel
Summary:	EWL header files and test programs
Summary(pl.UTF-8):	Pliki nagłówkowe i programy testowe dla biblioteki EWL
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* NEWS README TODO
%attr(755,root,root) %{_bindir}/ewl_test
%attr(755,root,root) %{_bindir}/ewl_*_test
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewl.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/tests
%attr(755,root,root) %{_libdir}/%{name}/tests/ewl_*.so

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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libewl.a
%endif
