%define	module	File-Edit
%define	name	perl-%{module}
%define	version	0.3.1
%define release	12

Summary:	File::Edit for inplace-editing of files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot/
Buildrequires:	perl-devel
Requires:	perl 
Buildarch:	noarch

%description
File::Edit is a Perl module which defines an easy to use interface for
inplace-editing of files. You can delete only one pattern or all
lines where the pattern matches.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc MANIFEST 
%{perl_vendorlib}/File
%{perl_vendorlib}/auto/File
%{_mandir}/*/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-10mdv2010.0
+ Revision: 430450
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-9mdv2009.0
+ Revision: 256877
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.3.1-7mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.3.1-7mdv2007.0
+ Revision: 108533
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-File-Edit

* Thu Feb 26 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3.1-6mdk
- rebuild
- Own dir

