Name:           decklink-devel
Version:        11.5.1
Release:        1%{?dist}
Summary:        Blackmagic Design DeckLink SDK
License:        Proprietary
URL:            https://www.blackmagicdesign.com/
BuildArch:      noarch

Source0:        Blackmagic_DeckLink_SDK_%{version}.zip

%description
This SDK provides developer support for Desktop Video that allows updating
of hardware control and software interfaces for Desktop Video products.

%package        samples
Summary:        Sample files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    samples
The %{name}-samples package contains sample programs and source code for the
DeckLink SDK.

%prep
%autosetup -c -T -a 0
mv "Blackmagic DeckLink SDK %{version}"/{Examples,Linux,*.*} .
rm -fr \
    Examples/Mac \
    Examples/Win \
    Examples/Examples.sln \
    Examples/Examples.xcodeproj \
    Examples/Linux/bin

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 Linux/include/* %{buildroot}%{_includedir}

%files
%doc ReadMe.rtf "Blackmagic DeckLink SDK.pdf"
%{_includedir}/*

%files samples
%doc Examples/

%changelog
* Sat May 23 2020 Simone Caronni <negativo17@gmail.com> - 11.5.1-1
- Update to 11.5.1.

* Sun Mar 15 2020 Simone Caronni <negativo17@gmail.com> - 11.4-1
- Update to 11.4.

* Mon Jul 16 2018 Simone Caronni <negativo17@gmail.com> - 10.11-1
- Update to 10.11.

* Fri Feb 02 2018 Simone Caronni <negativo17@gmail.com> - 10.9.10-1
- First build.
- 
