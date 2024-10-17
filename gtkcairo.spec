%define major 2
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary:	Gtk widget wrapper for Cairo surfaces
Name:		gtkcairo
Version:	0.3
Release:	6
License:	LGPL
Group:		System/Libraries
Source0:	http://cairographics.org/snapshots/%name-%version.tar.bz2
Patch0:	gtkcairo-0.3-cairo.patch
URL:		https://cairographics.org/GtkCairo
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
GtkCairo is a library that provides a new widget to be used in your
GTK+ program: a Cairo surface.

%package -n %{libname}
Summary:	Cairo - multi-platform 2D graphics library
Group:		System/Libraries
Provides:	gtkcairo = %{version}-%{release}

%description -n %{libname}
GtkCairo is a library that provides a new widget to be used in your
GTK+ program: a Cairo surface.

%package -n %{libnamedev}
Summary:	Development files for Cairo library
Group:		Development/C
Requires:	%{libname} = %version
Provides:	%{name}-devel = %version-%release
Provides:	libgtkcairo-devel = %version-%release

%description -n %{libnamedev}
Development files for GtkCairo library.

%package -n %{libname}-static-devel
Summary:	Static GtkCairo library
Group:		Development/C
Requires:	%{libnamedev} = %version

%description -n %{libname}-static-devel
Static GtkCairo library.


%prep
%setup -q
%patch0 -p1 -b .cairo

%build
export CFLAGS="%optflags -I`pwd`/%name"
%configure2_5x
%make

%install

%makeinstall

%files -n %{libname}
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README NEWS
%attr(755,root,root) %_libdir/lib*.so.*

%files -n %{libnamedev}
%defattr(644,root,root,755)
%_libdir/lib*.so
%_includedir/*
%_libdir/pkgconfig/*.pc

%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%_libdir/lib*.a



%changelog
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-5mdv2009.0
+ Revision: 246676
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-3mdv2008.1
+ Revision: 126401
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel


* Fri Aug 12 2005 Götz Waschk <waschk@mandriva.org> 0.3-3mdk
- it's LGPL now
- patch for new cairo

* Sat Dec 25 2004 Marcel Pol <mpol@mandrake.org> 0.3-2mdk
- buildrequires gtk2-devel

* Fri Sep 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3-1mdk
- from Tigrux <tigrux@ximian.com> : 
	- First RPM, based on Cairo rpm

