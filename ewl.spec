Summary:	Enlightenment Widget Library
Name:		ewl
Version:	0.0.4
%define	_snap	20050106
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	3ec91875fa1f5f0733da62bbe03ea017
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	etox-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EWL is a widget library which uses the E Foundation Libraries (EFL).

%package devel
Summary:	EWL headers and development libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
EWL development files.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* NEWS README TODO
%attr(755,root,root) %{_libdir}/libewl.so.*
%{_libdir}/libewl.la
%attr(755,root,root) %{_bindir}/ewl_edb_ed
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_aclocaldir}/ewl.m4
%attr(755,root,root) %{_libdir}/libewl.so
%{_libdir}/libewl.la
%{_pkgconfigdir}/ewl.pc
%{_includedir}/ewl/Ewl.h
%{_includedir}/ewl/ewl_*.h
%attr(755,root,root) %{_bindir}/ewl-config
%attr(755,root,root) %{_bindir}/ewl_test
%attr(755,root,root) %{_bindir}/ewl_embed_test
%attr(755,root,root) %{_bindir}/ewl_media_test
%attr(755,root,root) %{_bindir}/ewl_simple_test

%files static
%defattr(644,root,root,755)
%{_libdir}/libewl.a
