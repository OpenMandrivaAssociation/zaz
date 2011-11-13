Name:           zaz
Version:        1.0.0
Release:        %mkrel 1
Summary:        A puzzle game where the player has to arrange balls in triplets
Group:          Games/Arcade
# Music released under CC-BY-SA
License:        GPLv3+ and CC-BY-SA
URL:            http://sourceforge.net/projects/zaz/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libmesagl1-devel
BuildRequires: libSDL_image-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: libftgl-devel
BuildRequires: gettext


%description
Zaz is an arcade action puzzle game where the goal is to get rid of all 
incoming balls by rearranging their order and making triplets.
It currently includes 6 different levels. The game's name is recursive and 
stands for "Zaz ain't Z".

A 3D accelerator is needed for decent gameplay.


%prep
%setup -q

# Fix permissions
chmod 644 src/*.{cpp,h}


%build
%configure

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Symlink system fonts
#rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/FreeMonoBold.ttf
#ln -s %{_datadir}/fonts/gnu-free/FreeMonoBold.ttf \
#    $RPM_BUILD_ROOT%{_datadir}/%{name}/data/FreeMonoBold.ttf
#rm $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
#ln -s %{_datadir}/fonts/gnu-free/FreeSans.ttf \
#   $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
#m $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf
#n -s %{_datadir}/fonts/oflb-dignas-handwriting/phranzysko_-_Digna_s_Handwriting.ttf \
#   $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf

# Remove docs
rm -r $RPM_BUILD_ROOT/usr/share/doc/

# Fix desktop file
desktop-file-install \
   --delete-original \
   --add-category LogicGame \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
#{_datadir}/%{name}/FreeMonoBold.ttf
#{_datadir}/%{name}/FreeSans.ttf

%doc AUTHORS ChangeLog COPYING data/copyright.txt


