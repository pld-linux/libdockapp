Summary:	DockApp Making Standard Library
Summary(pl):	Biblioteka do tworzenia dokowalnych aplikacji
Name:		libdockapp
Version:	0.4.0
Release:	3
License:	Distributable
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
URL:		http://shadowmere.student.utwente.nl/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	docklib

%define 	_prefix 	/usr/X11R6

%description
DockApp Making Standard Library.

%description -l pl
Standardowa biblioteka do tworzenia dokowalnych aplikacji.

%package devel
Summary:	Header files etc to develop DockApps
Summary(pl):	Pliki nag³ówkowe i inne do tworzenia dokowalnych aplikacji
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc to develop DockApps.

%description -l pl devel
Pliki nag³ówkowe i inne niezbêdne do tworzenia dokowalnych aplikacji w
oparciu o tê bibliotekê.

%package static
Summary:	Static libdockapp library
Summary(pl):	Biblioteka statyczna libdockapp
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libdockapp library.

%description -l pl static
Biblioteka statyczna libdockapp.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS NEWS ChangeLog

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,AUTHORS,NEWS,ChangeLog}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdockapp.a
