Name:           decklink-devel
Version:        12.0
Release:        1%{?dist}
Summary:        Blackmagic Design DeckLink SDK
License:        End User License Agreement for the Software Development Kit
URL:            https://www.blackmagicdesign.com/
BuildArch:      noarch

Source0:        Blackmagic_DeckLink_SDK_%{version}.zip

%description
This SDK provides developer support for Desktop Video that allows updating
of hardware control and software interfaces for Desktop Video products.

%package        samples
Summary:        Sample files and documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    samples
The %{name}-samples package contains documentation and samplese for the
DeckLink SDK.

%prep
%autosetup -c
rm -fr Blackmagic\ DeckLink\ SDK\ %{version}/{Mac,Win,Examples/Mac,Examples/Win}
rm -fr Blackmagic\ DeckLink\ SDK\ %{version}/Linux/Samples/bin

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 0644 Linux/include/* %{buildroot}%{_includedir}

%files
%license "End User License Agreement.pdf"
%{_includedir}/*

%files samples
%doc ReadMe.rtf "Blackmagic DeckLink SDK.pdf"
%doc Examples/

%changelog
* Thu Mar 25 2021 Simone Caronni <negativo17@gmail.com> - 12.0-1
- Update to 12.0.

* Sat May 23 2020 Simone Caronni <negativo17@gmail.com> - 11.5.1-1
- Update to 11.5.1.

* Sun Mar 15 2020 Simone Caronni <negativo17@gmail.com> - 11.4-1
- Update to 11.4.

* Mon Jul 16 2018 Simone Caronni <negativo17@gmail.com> - 10.11-1
- Update to 10.11.

* Fri Feb 02 2018 Simone Caronni <negativo17@gmail.com> - 10.9.10-1
- First build.
- 
