# revision 24389
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-filter
# catalog-date 2011-10-24 18:25:01 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-context-filter
Version:	20111024
Release:	1
Summary:	Run external programs on the contents of a start-stop environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-filter
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-filter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-filter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context
Conflicts:	texlive-texmf <= 20110705-3

%description
The filter module provides a simple interface to run external
programs on the contents of a start-stop environment. Options
are available to run the external program only if the content
of the environment has changed, to specify how the program
output should be read back, and to choose the name of the
temporary files that are created. The module is compatible with
both MkII and MkIV.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/filter/t-filter.tex
%{_texmfdistdir}/tex/context/third/filter/t-module-catcodes.tex
%doc %{_texmfdistdir}/doc/context/third/filter/filter.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
