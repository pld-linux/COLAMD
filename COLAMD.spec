Summary:	COLAMD: column approximate minimum degree
Name:		colamd
Version:	2.6.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/colamd/COLAMD-%{version}.tar.gz
# Source0-md5:	49e185756896c1e918a535ec409c48b9
URL:		http://www.cise.ufl.edu/research/sparse/colamd/
Patch0:		%{name}-ufconfig.patch
BuildRequires:	UFconfig
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

%package devel
Summary:	Header files for colamd library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for colamd library.

%package static
Summary:	Static colamd library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static colamd library.

%prep
%setup -q -n COLAMD
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}
cp -a colamd.h $RPM_BUILD_ROOT%{_includedir}
cp -a libcolamd.a $RPM_BUILD_ROOT%{_libdir}/libcolamd.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt

%files devel
%defattr(644,root,root,755)
%{_includedir}/colamd.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcolamd.a
