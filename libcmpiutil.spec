# -*- rpm-spec -*-

Summary: CMPI Utility Library
Name: libcmpiutil
Version: 0.5.7
Release: 1%{?dist}%{?extra_release}
License: LGPLv2+
Group: System Environment/Libraries
Source: ftp://libvirt.org/libvirt-cim/libcmpiutil-%{version}.tar.gz
Patch0: libcmpiutil-0.5.6-cast-align.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://libvirt.org/CIM/
BuildRequires: tog-pegasus-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: libxml2-devel
BuildConflicts: sblim-cmpi-devel

%description
Libcmpiutil is a library of utility functions for CMPI providers.
The goal is to reduce the amount of repetitive work done in
most CMPI providers by encapsulating common procedures with more
"normal" APIs.  This extends from operations like getting typed
instance properties to standardizing method dispatch and argument checking.

%package devel
Summary: Libraries, includes, etc. to use the CMPI utility library
Group: Development/Libraries
Requires: tog-pegasus-devel
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}

%description devel
Includes and documentations for the CMPI utility library
The goal is to reduce the amount of repetitive work done in
most CMPI providers by encapsulating common procedures with more
"normal" APIs.  This extends from operations like getting typed
instance properties to standardizing method dispatch and argument checking.

%prep
%setup -q
chmod -x *.c *.y *.h *.l

%patch0 -p0

%build
%configure --enable-static=no
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)

%doc doc/doxygen.conf doc/mainpage README COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, -)

%{_libdir}/lib*.so
%dir %{_includedir}/libcmpiutil
%{_includedir}/libcmpiutil/*.h
%{_libdir}/pkgconfig/libcmpiutil.pc

%doc doc/SubmittingPatches

%changelog
* Mon Apr 15 2013 Daniel Veillard <veillard@redhat.com> 0.5.7-1
- update to 0.5.7 upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.5.6-4
- Remove cast-align to fix FTBFS on ARM, 872543.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul  6 2011 Daniel Veillard <veillard@redhat.com> - 0.5.6-1
- Update to new upstream release 0.5.6

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 17 2010 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.1-1
- Updated to official 0.5.1 source release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5-1
- Updated to official 0.5 source release

* Tue May 20 2008 Dan Smith <danms@us.ibm.com> - 0.4-1
- Updated to official 0.4 source release

* Fri Feb 29 2008 Dan Smith <danms@us.ibm.com> - 0.3-1
- Updated to official 0.3 source release

* Wed Feb 13 2008 Dan Smith <danms@us.ibm.com> - 0.2-1
- Updated to official 0.2 source release

* Fri Nov 30 2007 Dan Smith <danms@us.ibm.com> - 0.1-6
- Updated to official 0.1 source release
- Added Source0 URL

* Fri Oct 26 2007 Daniel Veillard <veillard@redhat.com> - 0.1-1
- created
