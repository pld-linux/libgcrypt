Summary:	Cryptographic library based on the code from GnuPG
Name:		libgcrypt
Version:	1.1.6
Release:	1
License:	GPL
Group:		Libraries
Group(cs):	Knihovny
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(ja):	╔И╔╓╔ж╔И╔Й
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libgcrypt/%{name}-%{version}.tar.gz
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
Group(cs):	VЩvojovИ prostЬedky/Knihovny
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(ja):	Ё╚х╞/╔И╔╓╔ж╔И╔Й
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files etc to develop libgcrypt applications.

%description -l pl devel
Pliki naglowkowe i inne do libgcrypt.

%package static
Summary:	Static libgcrypt library
Summary(pl):	Biblioteka statyczna libgcrypt
Group:		Development/Libraries
Group(cs):	VЩvojovИ prostЬedky/Knihovny
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(ja):	Ё╚х╞/╔И╔╓╔ж╔И╔Й
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static libgcrypt library.

%description -l pl static
Biblioteka statyczna libgcrypt.

%prep
%setup -q

%build
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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
