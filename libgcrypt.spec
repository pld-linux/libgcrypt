Summary:	Cryptographic library based on the code from GnuPG
Name:		libgcrypt
Version:	1.1.3
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/gnulist/production/libgcrypt.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a general purpose cryptographic library based on the code from
GnuPG. It provides functions for all cryptograhic building blocks:
symmetric ciphers (AES,DES,Blowfish,CAST5,Twofish,Arcfour), hash
algorithms (MD5, RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all
hash algorithms), public key algorithms (RSA, ElGamal, DSA), large
integer functions, random numbers and a lot of supporting functions.

%package devel
Summary:	Header files etc to develop libgcrypt applications
Summary(pl):	Pliki naglowkowe i inne do libgcrypt
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc to develop libgcrypt applications.

%description -l pl devel
Pliki naglowkowe i inne do libgcrypt.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libgcrypt/*
%attr(755,root,root) %{_bindir}/libgcrypt-config

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_datadir}/libgcrypt/*
%{_aclocaldir}/*
