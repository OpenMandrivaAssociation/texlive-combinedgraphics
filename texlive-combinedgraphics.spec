%global tl_name combinedgraphics
%global tl_revision 27198

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.2
Release:	%{tl_revision}.1
Summary:	Include graphic (EPS or PDF)/LaTeX combinations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/combinedgraphics
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a macro (\includecombinedgraphics) for the
inclusion of combined EPS/LaTeX and PDF/LaTeX graphics (an export format
of Gnuplot, Xfig, and maybe other programs). Instead of including the
graphics with a simple \input, the \includecombinedgraphics macro has
some comforts: changing the font and color of the text of the LaTeX
part; rescaling the graphics without affecting the font of the LaTeX
part; automatic inclusion of the vector graphics part, as far as LaTeX
part does not do it (e.g., for files exported from Gnuplot before
version 4.2); and rescaling and rotating of complete graphics (similar
to \includegraphics from the graphicx package).

