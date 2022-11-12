Name:		texlive-context-filter
Version:	62070
Release:	1
Summary:	Run external programs on the contents of a start-stop environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-filter
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-filter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-filter.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/context/third/filter
%doc %{_texmfdistdir}/doc/context/third/filter

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
