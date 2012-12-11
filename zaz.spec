Name:           zaz
Version:        1.0.0
Release:        1
Summary:        A puzzle game where the player has to arrange balls in triplets
Group:          Games/Arcade
# Music released under CC-BY-SA
License:        GPLv3+ and CC-BY-SA
URL:            http://sourceforge.net/projects/zaz/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(SDL_image)
BuildRequires: pkgconfig(theora)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(ftgl)
BuildRequires: gettext
BuildRequires: desktop-file-utils

%description
Zaz is an arcade action puzzle game where the goal is to get rid of all 
incoming balls by rearranging their order and making triplets.
It currently includes 6 different levels. The game's name is recursive and 
stands for "Zaz ain't Z".

A 3D accelerator is needed for decent game play.


%prep
%setup -q
rm -fr win32.zip

# Fix permissions
chmod 644 src/*.{cpp,h}


%build
%configure
%make


%install
%makeinstall_std

# Remove docs
rm -r $RPM_BUILD_ROOT/usr/share/doc/

# Fix desktop file
desktop-file-install \
   --delete-original \
   --add-category LogicGame \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING data/copyright.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm







%changelog
* Wed Nov 16 2011 Sergey Zhemoitel <serg@mandriva.org> 1.0.0-1
+ Revision: 730828
- imported package zaz

