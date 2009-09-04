%define	module	File-Edit
%define	name	perl-%{module}
%define	version	0.3.1
%define	release	%mkrel 10

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


