%define major 2
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary:	Gtk widget wrapper for Cairo surfaces
Name:		gtkcairo
Version:	0.3
Release:	%mkrel 3
License:	LGPL
Group:		System/Libraries
Source0:	http://cairographics.org/snapshots/%name-%version.tar.bz2
Patch:	gtkcairo-0.3-cairo.patch
URL:		http://cairographics.org/GtkCairo
BuildRequires:	cairo-devel
BuildRequires:	gtk2-devel
BuildRoot:	%_tmppath/%name-%version-root

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
%patch -p1 -b .cairo

%build
export CFLAGS="%optflags -I`pwd`/%name"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n %{libname} -p /sbin/ldconfig
%postun	-n %{libname} -p /sbin/ldconfig


%files -n %{libname}
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README NEWS
%_libdir/lib*.so.*

%files -n %{libnamedev}
%defattr(644,root,root,755)
%_libdir/lib*.so
%_libdir/lib*.la
%_includedir/*
%_libdir/pkgconfig/*.pc

%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%_libdir/lib*.a

