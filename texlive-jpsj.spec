# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/jpsj
# catalog-date 2007-03-14 08:57:39 +0100
# catalog-license lppl
# catalog-version 1.2.2
Name:		texlive-jpsj
Version:	1.2.2
Release:	1
Summary:	Document Class for Journal of the Physical Society of Japan
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jpsj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jpsj.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jpsj.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive jpsj package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/jpsj/jpsj2.cls
%doc %{_texmfdistdir}/doc/latex/jpsj/dummy.eps
%doc %{_texmfdistdir}/doc/latex/jpsj/injpsj2.pdf
%doc %{_texmfdistdir}/doc/latex/jpsj/injpsj2.tex
%doc %{_texmfdistdir}/doc/latex/jpsj/template.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
