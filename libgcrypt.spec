Summary:	Cryptographic library based on the code from GnuPG
Summary(es):	Libgcrypt es una biblioteca general de desarrole embasada em GnuPG
Summary(pl):	Biblioteka kryptograficzna oparta na kodzie GnuPG
Summary(pt_BR):	libgcrypt é uma biblioteca de criptografia de uso geral baseada no GnuPG
Name:		libgcrypt
Version:	1.2.1
Release:	1
License:	LGPL
Group:		Libraries
# devel versions:
#Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libgcrypt/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.gnupg.org/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2
# Source0-md5:	b6d3217c9333c520fe54d2e8dc5e60ec
Patch0:		%{name}-no_libnsl.patch
Patch1:		%{name}-info.patch
URL:		http://www.gnu.org/directory/security/libgcrypt.html
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.3
BuildRequires:	binutils >= 2:2.12
BuildRequires:	gcc >= 3.2
BuildRequires:	libgpg-error-devel >= 0.5
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	texinfo
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

%description -l pt_BR
Libgcrypt é uma biblioteca de criptografia de uso geral baseada no
GnuPG.

%package devel
Summary:	Header files etc to develop libgcrypt applications
Summary(es):	Archivos de desarrollo de libgcrypt
Summary(pl):	Pliki nag³ówkowe i inne do libgcrypt
Summary(pt_BR):	Arquivos de desenvolvimento da libgcrypt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgpg-error-devel >= 0.5

%description devel
Header files etc to develop libgcrypt applications.

%description devel -l pl
Pliki nag³ówkowe i inne do libgcrypt.

%description devel -l pt_BR
Bibliotecas de desenvolvimento para libgcrypt.

%package static
Summary:	Static libgcrypt library
Summary(es):	Archivos de desarrollo de libgcrypt - estatico
Summary(pl):	Biblioteka statyczna libgcrypt
Summary(pt_BR):	Arquivos de desenvolvimento da libgcrypt - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgcrypt library.

%description static -l pl
Biblioteka statyczna libgcrypt.

%description static -l pt_BR
Bibliotecas de desenvolvimento para libgcrypt - estático.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libgcrypt.so.*.*.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib}; echo libgcrypt.so.*.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libgcrypt.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS THANKS NEWS README ChangeLog
%attr(755,root,root) /%{_lib}/libgcrypt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgcrypt-config
%attr(755,root,root) %{_libdir}/libgcrypt.so
%{_libdir}/libgcrypt.la
%{_infodir}/*.info*
%{_includedir}/*.h
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgcrypt.a
