Summary:	Cryptographic library based on the code from GnuPG
Summary(pl):	Biblioteka kryptograficzna oparta na kodzie GnuPG
Name:		libgcrypt
Version:	1.1.6
Release:	4
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libgcrypt/%{name}-%{version}.tar.gz
Patch0:		%{name}-initializer_fix.patch
URL:		http://www.gnu.org/gnulist/production/libgcrypt.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a general purpose cryptographic library based on the code from
GnuPG. It provides functions for all cryptograhic building blocks:
symmetric ciphers (AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash
algorithms (MD5, RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all
hash algorithms), public key algorithms (RSA, ElGamal, DSA), large
integer functions, random numbers and a lot of supporting functions.

%description -l pl
Ten pakiet zawiera bibliotekê kryptograficzn± ogólnego przeznaczenia,
opart± na kodzie GnuPG. Biblioteka ta dostarcza funkcje do wszystkich
podstawowych bloków kryptografii: szyfrów symetrycznych (AES, DES,
Blowfish, CAST5, Twofish, Acrfour), algorytmów mieszaj±cych (MD5,
RIPE-MD160, SHA-1, RIGER-192), MAC-ów (HMAC dla wszystkich algorytmów
mieszaj±cych), algorytmów klucza publicznego (RSA, ElGamal, DSA),
funkcji du¿ych liczb ca³kowitych, liczb losowych i wiele funkcji
pomocniczych.

%package devel
Summary:	Header files etc to develop libgcrypt applications
Summary(pl):	Pliki nag³ówkowe i inne do libgcrypt
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc to develop libgcrypt applications.

%description devel -l pl
Pliki nag³ówkowe i inne do libgcrypt.

%package static
Summary:	Static libgcrypt library
Summary(pl):	Biblioteka statyczna libgcrypt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libgcrypt library.

%description static -l pl
Biblioteka statyczna libgcrypt.

%prep
%setup -q
%patch0

%build
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgcrypt-config
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/libgcrypt
%attr(755,root,root) %{_libdir}/libgcrypt/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
