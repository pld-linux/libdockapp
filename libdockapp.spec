Summary:	DockApp Making Standard Library
Summary(pl):	Biblioteka do tworzenia dokowalnych aplikacji
Name:		libdockapp
Version:	0.4.0
Release:	5
License:	distributable
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
URL:		http://shadowmere.student.utwente.nl/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	docklib

%define 	_prefix 	/usr/X11R6

%description
DockApp Making Standard Library.

%description -l pl
Standardowa biblioteka do tworzenia dokowalnych aplikacji.

%package devel
Summary:	Header files etc to develop DockApps
Summary(pl):	Pliki nagЁСwkowe i inne do tworzenia dokowalnych aplikacji
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files etc to develop DockApps.

%description -l pl devel
Pliki nagЁСwkowe i inne niezbЙdne do tworzenia dokowalnych aplikacji w
oparciu o tЙ bibliotekЙ.

%package static
Summary:	Static libdockapp library
Summary(pl):	Biblioteka statyczna libdockapp
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static libdockapp library.

%description -l pl static
Biblioteka statyczna libdockapp.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS NEWS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
