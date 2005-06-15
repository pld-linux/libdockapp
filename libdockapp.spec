# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	DockApp Making Standard Library
Summary(pl):	Biblioteka do tworzenia dokowalnych aplikacji
Summary(pt_BR):	Biblioteca para desenvolver aplicativos dock
Name:		libdockapp
Version:	0.5.0
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://solfertje.student.utwente.nl/~dalroi/libdockapp/files/%{name}-%{version}.tar.bz2
# Source0-md5:	918693a30bdff72e629ef8b85a3f6779
Patch0:		%{name}-Makefile.patch
URL:		http://solfertje.student.utwente.nl/~dalroi/libdockapp/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	docklib

%description
DockApp Making Standard Library.

%description -l pl
Standardowa biblioteka do tworzenia dokowalnych aplikacji.

%description -l pt_BR
Esta biblioteca provê um início básico para o desenvolvimento de
aplicativos dock.

%package devel
Summary:	Header files etc to develop DockApps
Summary(pl):	Pliki nag³ówkowe i inne do tworzenia dokowalnych aplikacji
Summary(pt_BR):	Arquivos de desenvolvimento para a libdockapp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel

%description devel
Header files etc to develop DockApps.

%description devel -l pl
Pliki nag³ówkowe i inne niezbêdne do tworzenia dokowalnych aplikacji w
oparciu o tê bibliotekê.

%description devel -l pt_BR
Arquivo de cabeçalho e bibliotecas de desenvolvimento para a
libdockapp

%package static
Summary:	Static libdockapp library
Summary(pl):	Biblioteka statyczna libdockapp
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libdockapp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libdockapp library.

%description static -l pl
Biblioteka statyczna libdockapp.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libdockapp

%prep
%setup -q -n dockapp
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf examples/[br]* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
fontpostinst misc

%postun
/sbin/ldconfig
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_fontsdir}/misc/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_examplesdir}/%name-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdockapp.a
%endif
