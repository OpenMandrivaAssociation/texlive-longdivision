Name:		texlive-longdivision
Version:	59979
Release:	2
Summary:	Typesets long division
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/longdivision
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longdivision.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/longdivision.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package executes the long division algorithm and typesets
the solutions. The dividend must be a positive decimal number
and the divisor must be a positive integer. Repeating decimals
is handled correctly, putting a bar over the repeated part of
the decimal. Dividends up to 20 digits long are handled
gracefully (though the typeset result will take up about a
page), and dividends between 20 and 60 digits long slightly
less gracefully. The package defines two macros, \longdivision
and \intlongdivision. Each takes two arguments, a dividend and
a divisor. \longdivision keeps dividing until the remainder is
zero, or it encounters a repeated remainder. \intlongdivision
stops when the dividend stops (though the dividend doesn't have
to be an integer). This package depends on the xparse package
from the l3packages bundle.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/longdivision
%doc %{_texmfdistdir}/doc/latex/longdivision

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
