# TODO:
# - java docs doesn't build on builders, please fix this and include them again
Summary:	Easy to use and powerful layout manager for Java
Summary(pl.UTF-8):	Łatwy w użyciu i potężny zarządca układów graficznych dla Javy
Name:		higlayout
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.autel.cz/dmi/HIGLayout%{version}.zip
# Source0-md5:	5bd79f33157824499b0fc03d6a5e080a
URL:		http://www.autel.cz/dmi/tutorial.html
BuildRequires:	java-sun
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jre >= 1.4
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use and powerful layout manager for Java.

%description -l pl.UTF-8
Łatwy w użyciu i potężny zarządca układów graficznych dla Javy.

%prep
%setup -q -c
mv src/cz .
sed -i -e 's/\r//g' examples/*.java tutorial/*.html *.txt
rm -rf apidoc ; mkdir apidoc

%build
javac -source 1.4 cz/autel/dmi/*.java
jar cf %{name}.jar cz/autel/dmi/*.class

%install
rm -rf $RPM_BUILD_ROOT

install -Dpm 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.txt LGPLicense.txt readme.txt examples/ tutorial/
%{_javadir}/%{name}*.jar
