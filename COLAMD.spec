Summary:	COLAMD: column approximate minimum degree
Summary(pl.UTF-8):	COLAMD - przybliżony algorytm minimalnego stopnia dla kolumn
Name:		COLAMD
Version:	2.7.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/colamd/%{name}-%{version}.tar.gz
# Source0-md5:	7f41dd0e49d6db367f74e8c7a5e60918
Patch0:		colamd-ufconfig.patch
Patch1:		colamd-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/colamd/
BuildRequires:	UFconfig
BuildRequires:	libtool >= 2:1.5
Obsoletes:	colamd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The COLAMD column approximate minimum degree ordering algorithm
computes a permutation vector P such that the LU factorization of A
(:,P) tends to be sparser than that of A. The Cholesky factorization
of (A (:,P))'*(A (:,P)) will also tend to be sparser than that of
A'*A. SYMAMD is a symmetric minimum degree ordering method based on
COLAMD, available as a MATLAB-callable function. It constructs a
matrix M such that M'*M has the same pattern as A, and then uses
COLAMD to compute a column ordering of M. Colamd and symamd tend to be
faster and generate better orderings than their MATLAB counterparts,
colmmd and symmmd.

%description -l pl.UTF-8
Przybliżony algorytm porządkowania minimalnego stopnia dla kolumn
(COLAMD) oblicza wektor permutacji P taki, że rozkład LU A (:,P) jest
bardziej rzadki niż A. Rozkład Cholesky'ego (A (:,P))'*(A (:,P)) także
jest rzadszy niż A'*A. SYMAND to przybliżony algorytm porządkowania
minimalnego stopnia dla macierzy symetrycznych oparty na COLAMD,
dostępny jako funkcja do wywołania z MATLAB-a. Tworzy macierz M taką,
że M'*M ma ten sam wzór co A, a następnie używa algorytmu COLAMD do
obliczenia porządku kolumn M. COLAMD i SYMAMD są szybsze i generują
lepsze uporządkowania niż ich odpowiedniki z MATLAB-a: colmmd i
symmmd.

%package devel
Summary:	Header files for COLAMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki COLAMD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig
Obsoletes:	colamd-devel

%description devel
Header files for COLAMD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki COLAMD.

%package static
Summary:	Static COLAMD library
Summary(pl.UTF-8):	Statyczna biblioteka COLAMD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	colamd-static

%description static
Static COLAMD library.

%description static -l pl.UTF-8
Statyczna biblioteka COLAMD.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/colamd

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/colamd

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libcolamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolamd.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolamd.so
%{_libdir}/libcolamd.la
%{_includedir}/colamd

%files static
%defattr(644,root,root,755)
%{_libdir}/libcolamd.a
