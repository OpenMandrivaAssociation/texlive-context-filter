# revision 26248
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-filter
# catalog-date 2012-04-22 10:53:46 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-context-filter
Version:	20120422
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

%description
The filter module provides a simple interface to run external
programs on the contents of a start-stop environment. Options
are available to run the external program only if the content
of the environment has changed, to specify how the program
output should be read back, and to choose the name of the
temporary files that are created. The module is compatible with
both MkII and MkIV.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/filter/t-filter.mkii
%{_texmfdistdir}/tex/context/third/filter/t-filter.mkiv
%{_texmfdistdir}/tex/context/third/filter/t-module-catcodes.tex
%doc %{_texmfdistdir}/doc/context/third/filter/filter.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120422-1
+ Revision: 804539
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120319-1
+ Revision: 787576
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120212-1
+ Revision: 779424
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120128-1
+ Revision: 770136
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111228-1
+ Revision: 762565
- Update to latest upstream package

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111205-3
+ Revision: 750493
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111205-2
+ Revision: 745169
- texlive-context-filter

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111205-1
+ Revision: 739711
- texlive-context-filter

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111024-1
+ Revision: 718128
- texlive-context-filter
- texlive-context-filter
- texlive-context-filter
- texlive-context-filter

