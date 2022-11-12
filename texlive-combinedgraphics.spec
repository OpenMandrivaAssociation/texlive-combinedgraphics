Name:		texlive-combinedgraphics
Version:	27198
Release:	1
Summary:	Include graphic (EPS or PDF)/LaTeX combinations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/combinedgraphics
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a macro (\includecombinedgraphics) for
the inclusion of combined EPS/LaTeX and PDF/LaTeX graphics (an
export format of Gnuplot, Xfig, and maybe other programs).
Instead of including the graphics with a simple \input, the
\includecombinedgraphics macro has some comforts: - changing
the font and color of the text of the LaTeX part; - rescaling
the graphics without affecting the font of the LaTeX part; -
automatic inclusion of the vector graphics part, as far as
LaTeX part does not do it (e.g., for files exported from
Gnuplot before version 4.2); and - rescaling and rotating of
complete graphics (similar to \includegraphics from the
graphicx package).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/combinedgraphics/combinedgraphics.sty
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/COPYING
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/Makefile
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/README
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/combinedgraphics.pdf
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/Makefile
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/combinedgraphics_test.pdf
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/combinedgraphics_test.tex
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/gnuplot42.eps
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/gnuplot42.pdf
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/gnuplot42.plt
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/gnuplot42.tex
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/xfig325.eps
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/xfig325.fig
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/xfig325.pdf
%doc %{_texmfdistdir}/doc/latex/combinedgraphics/test/xfig325.tex
#- source
%doc %{_texmfdistdir}/source/latex/combinedgraphics/combinedgraphics.dtx
%doc %{_texmfdistdir}/source/latex/combinedgraphics/combinedgraphics.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
