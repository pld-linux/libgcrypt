#
# Conditional build:
%bcond_without	dietlibc	# don't build static dietlibc library
#
Summary:	Cryptographic library based on the code from GnuPG
Summary(es.UTF-8):	Libgcrypt es una biblioteca general de desarrole embasada em GnuPG
Summary(pl.UTF-8):	Biblioteka kryptograficzna oparta na kodzie GnuPG
Summary(pt_BR.UTF-8):	libgcrypt é uma biblioteca de criptografia de uso geral baseada no GnuPG
Name:		libgcrypt
Version:	1.4.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
# devel versions:
#Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libgcrypt/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.gnupg.org/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2
# Source0-md5:	34105aa927e23c217741966496b97e67
Patch0:		%{name}-info.patch
Patch1:		%{name}-sparc64.patch
Patch2:		%{name}-libgcrypt_config.patch
URL:		http://www.gnu.org/directory/security/libgcrypt.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	binutils >= 2:2.12
%{?with_dietlibc:BuildRequires:	dietlibc-static >= 2:0.31-5}
BuildRequires:	gcc >= 5:3.2
BuildRequires:	libgpg-error-devel >= 1.4
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# for some reason known only to rpm there must be "\\|" not "\|" here
%define		dietarch	%(echo %{_target_cpu} | sed -e 's/i.86\\|pentium.\\|athlon/i386/;s/amd64/x86_64/;s/armv.*/arm/')
%define		dietlibdir	%{_prefix}/lib/dietlibc/lib-%{dietarch}

%description
This is a general purpose cryptographic library based on the code from
GnuPG. It provides functions for all cryptograhic building blocks:
symmetric ciphers (AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash
algorithms (MD5, RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all
hash algorithms), public key algorithms (RSA, ElGamal, DSA), large
integer functions, random numbers and a lot of supporting functions.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę kryptograficzną ogólnego przeznaczenia,
opartą na kodzie GnuPG. Biblioteka ta dostarcza funkcje do wszystkich
podstawowych bloków kryptografii: szyfrów symetrycznych (AES, DES,
Blowfish, CAST5, Twofish, Acrfour), algorytmów mieszających (MD5,
RIPE-MD160, SHA-1, RIGER-192), MAC-ów (HMAC dla wszystkich algorytmów
mieszających), algorytmów klucza publicznego (RSA, ElGamal, DSA),
funkcji dużych liczb całkowitych, liczb losowych i wiele funkcji
pomocniczych.

%description -l pt_BR.UTF-8
Libgcrypt é uma biblioteca de criptografia de uso geral baseada no
GnuPG.

%package devel
Summary:	Header files etc to develop libgcrypt applications
Summary(es.UTF-8):	Archivos de desarrollo de libgcrypt
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do libgcrypt
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libgcrypt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgpg-error-devel >= 1.4

%description devel
Header files etc to develop libgcrypt applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do libgcrypt.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libgcrypt.

%package static
Summary:	Static libgcrypt library
Summary(es.UTF-8):	Archivos de desarrollo de libgcrypt - estatico
Summary(pl.UTF-8):	Biblioteka statyczna libgcrypt
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libgcrypt - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgcrypt library.

%description static -l pl.UTF-8
Biblioteka statyczna libgcrypt.

%description static -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libgcrypt - estático.

%package dietlibc
Summary:	Static dietlibc libgcrypt library
Summary(pl.UTF-8):	Biblioteka statyczna dietlibc libgcrypt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description dietlibc
Static dietlibc libgcrypt library.

%description dietlibc -l pl.UTF-8
Biblioteka statyczna dietlibc libgcrypt.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm m4/libtool.m4
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

%if %{with dietlibc}
%configure \
	CC="diet %{__cc} -Os %{rpmldflags}" \
	--enable-static \
	--disable-shared

# libtool sucks, build just the libs
%{__make} -C cipher
%{__make} -C mpi
%{__make} -C random
%{__make} -C src
mv src/.libs/libgcrypt.a diet-libgcrypt.a
%{__make} clean
%endif

%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{?with_dietlibc:install -d $RPM_BUILD_ROOT%{dietlibdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libgcrypt.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libgcrypt.so.*.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libgcrypt.so

%{?with_dietlibc:install diet-libgcrypt.a $RPM_BUILD_ROOT%{dietlibdir}/libgcrypt.a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/dumpsexp
%attr(755,root,root) %{_bindir}/hmac256
%attr(755,root,root) /%{_lib}/libgcrypt.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libgcrypt.so.11

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgcrypt-config
%attr(755,root,root) %{_libdir}/libgcrypt.so
%{_libdir}/libgcrypt.la
%{_infodir}/gcrypt.info*
%{_includedir}/gcrypt*.h
%{_aclocaldir}/libgcrypt.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgcrypt.a

%if %{with dietlibc}
%files dietlibc
%defattr(644,root,root,755)
%{dietlibdir}/libgcrypt.a
%endif
