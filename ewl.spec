Summary:	Enlightenment Widget Library
Summary(pl):	Biblioteka widgetów Enlightenmenta (Enlightenment Widget Library)
Name:		ewl
Version:	0.0.4.004
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	aed8f9eaf06ed5f0120d6f9ce2dc985c
URL:		http://enlightenment.org/Libraries/Ewl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EWL is a widget library which uses the E Foundation Libraries (EFL).

%description -l pl
EWL to biblioteka widgetów u¿ywaj±ca EFL (E Foundation Libraries -
podstawowych bibliotek Englightenmenta).

%package devel
Summary:	EWL header files and test programs
Summary(pl):	Pliki nag³ówkowe i programy testowe dla biblioteki EWL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
%setup -q
echo 'AC_DEFUN([AC_C___ATTRIBUTE__],
 [
  AC_MSG_CHECKING(for __attribute__)
  AC_CACHE_VAL(ac_cv___attribute__, [
  AC_TRY_COMPILE([#include <stdlib.h>],
  [int func(int x); int foo(int x __attribute__ ((unused))) { exit(1); }],
  ac_cv___attribute__=yes, ac_cv___attribute__=no)])
  if test "$ac_cv___attribute__" = "yes"; then
    AC_DEFINE(HAVE___ATTRIBUTE__, 1, [Define to 1 if compiler has __attribute__])
  fi
  AC_MSG_RESULT($ac_cv___attribute__)])' > acinclude.m4

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
%attr(755,root,root) %{_bindir}/ewl_edb_ed
%attr(755,root,root) %{_libdir}/libewl.so.*.*.*
%{_libdir}/libewl.la
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ewl-config
%attr(755,root,root) %{_bindir}/ewl_test
%attr(755,root,root) %{_bindir}/ewl_embed_test
%attr(755,root,root) %{_bindir}/ewl_media_test
%attr(755,root,root) %{_bindir}/ewl_simple_test
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
