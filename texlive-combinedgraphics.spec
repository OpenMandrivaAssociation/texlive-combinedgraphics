# revision 27198
# category Package
# catalog-ctan /macros/latex/contrib/combinedgraphics
# catalog-date 2012-07-16 18:35:20 +0200
# catalog-license gpl
# catalog-version 0.2.2
Name:		texlive-combinedgraphics
Version:	0.2.2
Release:	2
Summary:	Include graphic (EPS or PDF)/LaTeX combinations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/combinedgraphics
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combinedgraphics.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2.2-1
+ Revision: 812144
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1alpha-2
+ Revision: 750390
- Rebuild to reduce used resources

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1alpha-1
+ Revision: 722998
- texlive-combinedgraphics
- texlive-combinedgraphics
- texlive-combinedgraphics
- texlive-combinedgraphics
- texlive-combinedgraphics

