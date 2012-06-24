#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	DockApp Making Standard Library
Summary(pl.UTF-8):	Biblioteka do tworzenia dokowalnych aplikacji
Summary(pt_BR.UTF-8):	Biblioteca para desenvolver aplicativos dock
Name:		libdockapp
Version:	0.6.2
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://solfertje.student.utwente.nl/~dalroi/libdockapp/files/%{name}-%{version}.tar.bz2
# Source0-md5:	05a9a5f295d956397e6bb53bad3a0322
Patch0:		%{name}-Makefile.patch
URL:		http://solfertje.student.utwente.nl/~dalroi/libdockapp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-proto-xextproto-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	docklib

%description
DockApp Making Standard Library.

%description -l pl.UTF-8
Standardowa biblioteka do tworzenia dokowalnych aplikacji.

%description -l pt_BR.UTF-8
Esta biblioteca provê um início básico para o desenvolvimento de
aplicativos dock.

%package devel
Summary:	Header files etc to develop DockApps
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do tworzenia dokowalnych aplikacji
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento para a libdockapp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXpm-devel

%description devel
Header files etc to develop DockApps.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne niezbędne do tworzenia dokowalnych aplikacji w
oparciu o tę bibliotekę.

%description devel -l pt_BR.UTF-8
Arquivo de cabeçalho e bibliotecas de desenvolvimento para a
libdockapp

%package static
Summary:	Static libdockapp library
Summary(pl.UTF-8):	Biblioteka statyczna libdockapp
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libdockapp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdockapp library.

%description static -l pl.UTF-8
Biblioteka statyczna libdockapp.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libdockapp

%prep
%setup -q
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
