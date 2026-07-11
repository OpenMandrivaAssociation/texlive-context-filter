%global tl_name context-filter
%global tl_revision 62070

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Run external programs on the contents of a start-stop environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-filter
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-filter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-filter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The filter module provides a simple interface to run external programs
on the contents of a start-stop environment. Options are available to
run the external program only if the content of the environment has
changed, to specify how the program output should be read back, and to
choose the name of the temporary files that are created. The module is
compatible with both MkII and MkIV.

