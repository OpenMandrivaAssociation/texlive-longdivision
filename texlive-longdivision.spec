%global tl_name longdivision
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.2
Release:	%{tl_revision}.1
Summary:	Typesets long division
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/longdivision
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/longdivision.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/longdivision.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package executes the long division algorithm and typesets the
solutions. The dividend must be a positive decimal number and the
divisor must be a positive integer. Repeating decimals is handled
correctly, putting a bar over the repeated part of the decimal.
Dividends up to 20 digits long are handled gracefully (though the
typeset result will take up about a page), and dividends between 20 and
60 digits long slightly less gracefully. The package defines two macros,
\longdivision and \intlongdivision. Each takes two arguments, a dividend
and a divisor. \longdivision keeps dividing until the remainder is zero,
or it encounters a repeated remainder. \intlongdivision stops when the
dividend stops (though the dividend doesn't have to be an integer). This
package depends on the xparse package from the l3packages bundle.

