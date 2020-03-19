#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sn
Version  : 1.5.5
Release  : 28
URL      : https://cran.r-project.org/src/contrib/sn_1.5-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sn_1.5-5.tar.gz
Summary  : The Skew-Normal and Related Distributions Such as the Skew-t
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-mnormt
Requires: R-numDeriv
BuildRequires : R-mnormt
BuildRequires : R-numDeriv
BuildRequires : buildreq-R

%description
family and some related ones, notably the skew-t family, and provide related
  statistical methods for data fitting and model diagnostics, in the univariate 
  and the multivariate case.

%prep
%setup -q -c -n sn

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580495367

%install
export SOURCE_DATE_EPOCH=1580495367
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sn
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sn
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sn
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc sn || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sn/CITATION
/usr/lib64/R/library/sn/DESCRIPTION
/usr/lib64/R/library/sn/INDEX
/usr/lib64/R/library/sn/Meta/Rd.rds
/usr/lib64/R/library/sn/Meta/data.rds
/usr/lib64/R/library/sn/Meta/features.rds
/usr/lib64/R/library/sn/Meta/hsearch.rds
/usr/lib64/R/library/sn/Meta/links.rds
/usr/lib64/R/library/sn/Meta/nsInfo.rds
/usr/lib64/R/library/sn/Meta/package.rds
/usr/lib64/R/library/sn/NAMESPACE
/usr/lib64/R/library/sn/NEWS
/usr/lib64/R/library/sn/R/sn
/usr/lib64/R/library/sn/R/sn.rdb
/usr/lib64/R/library/sn/R/sn.rdx
/usr/lib64/R/library/sn/data/ais.rda
/usr/lib64/R/library/sn/data/barolo.rda
/usr/lib64/R/library/sn/data/frontier.rda
/usr/lib64/R/library/sn/data/wines.rda
/usr/lib64/R/library/sn/doc/R.css
/usr/lib64/R/library/sn/doc/how_to_sample.pdf
/usr/lib64/R/library/sn/doc/pkg-overview.html
/usr/lib64/R/library/sn/doc/pkg_sn-intro.pdf
/usr/lib64/R/library/sn/doc/selm-intervals.pdf
/usr/lib64/R/library/sn/help/AnIndex
/usr/lib64/R/library/sn/help/aliases.rds
/usr/lib64/R/library/sn/help/paths.rds
/usr/lib64/R/library/sn/help/sn.rdb
/usr/lib64/R/library/sn/help/sn.rdx
/usr/lib64/R/library/sn/html/00Index.html
/usr/lib64/R/library/sn/html/R.css
