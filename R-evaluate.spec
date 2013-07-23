%bcond_with bootstrap
%global packname  evaluate
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.4.4
Release:          1
Summary:          Parsing and evaluation tools that provide more details than the default
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-stringr 
%if %{without bootstrap}
Requires:         R-testthat R-ggplot2 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-stringr 
%if %{without bootstrap}
BuildRequires:    R-testthat R-ggplot2 
%endif
BuildRequires:    x11-server-xvfb

%description
Parsing and evaluation tools that make it easy to recreate the command
line behaviour of R.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME
#  length(dev.list()) not equal to 1
#...
#  cannot shut down device 1 (the null device)
%if 0
%check
xvfb-run %{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tests


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4.1-2
+ Revision: 778352
- Rebuild with proper dependencies

* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4.1-1
+ Revision: 775806
- Import R-evaluate
- Import R-evaluate

