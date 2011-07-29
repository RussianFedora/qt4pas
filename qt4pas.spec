#%define fpc_unit_dir %{_libdir}/fpc/2.4.2/units/%{_target}/qt4
%define fpc_unit_dir %{_datadir}/fpcsrc/packages/qt4

Name:           qt4pas
Version:        2.4
Release:        3%{?dist}
Summary:        Free Pascal Qt4 Binding

License:        LGPL
URL:            http://users.pandora.be/Jan.Van.hijfte/qtforfpc/fpcqt4.html
Source0:        http://users.telenet.be/Jan.Van.hijfte/qtforfpc/V%{version}/%{name}-V%{version}_Qt4.5.3.tar.gz

BuildRequires:  qt4-devel >= 4.5.3 qt-webkit-devel >= 4.5.3
Requires:	fpc-src

%description
Free Pascal Qt4 Binding

%prep
%setup -q -n %{name}-V%{version}_Qt4.5.3


%build
qmake-qt4
make %{?_smp_mflags} 


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT
install -D -m 644 qt4.pas $RPM_BUILD_ROOT%{fpc_unit_dir}/qt4.pas

%files
%doc README.TXT COPYING.TXT
%{_libdir}/libQt4Pas.so*
%{fpc_unit_dir}/qt4.pas



%changelog
* Fri Jul 29 2011 Alexei Panov <elemc AT atisserv DOT ru> - 2.1-1
- Initial build
