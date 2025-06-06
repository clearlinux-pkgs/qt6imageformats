#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v22
# autospec commit: 247c192
#
Name     : qt6imageformats
Version  : 6.9.0
Release  : 24
URL      : https://download.qt.io/official_releases/qt/6.9/6.9.0/submodules/qtimageformats-everywhere-src-6.9.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.9/6.9.0/submodules/qtimageformats-everywhere-src-6.9.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0 libtiff
Requires: qt6imageformats-lib = %{version}-%{release}
Requires: qt6imageformats-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpdemux)
BuildRequires : pkgconfig(libwebpmux)
BuildRequires : qt6base-dev
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[Useful links]
* http://en.wikipedia.org/wiki/Apple_Icon_Image_format - Wikipedia article about ICNS format
* http://www.macdisk.com/maciconen.php - Unofficial tech info about the format

%package dev
Summary: dev components for the qt6imageformats package.
Group: Development
Requires: qt6imageformats-lib = %{version}-%{release}
Provides: qt6imageformats-devel = %{version}-%{release}
Requires: qt6imageformats = %{version}-%{release}

%description dev
dev components for the qt6imageformats package.


%package lib
Summary: lib components for the qt6imageformats package.
Group: Libraries
Requires: qt6imageformats-license = %{version}-%{release}

%description lib
lib components for the qt6imageformats package.


%package license
Summary: license components for the qt6imageformats package.
Group: Default

%description license
license components for the qt6imageformats package.


%prep
%setup -q -n qtimageformats-everywhere-src-6.9.0
cd %{_builddir}/qtimageformats-everywhere-src-6.9.0
pushd ..
cp -a qtimageformats-everywhere-src-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743643926
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1743643926
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6imageformats
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6imageformats/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6imageformats/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6imageformats/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6imageformats/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6imageformats/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/LICENSES/libtiff.txt %{buildroot}/usr/share/package-licenses/qt6imageformats/a2f64f2a85f5fd34bda8eb713c3aad008adbb589 || :
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/src/3rdparty/libtiff/COPYRIGHT %{buildroot}/usr/share/package-licenses/qt6imageformats/a2f64f2a85f5fd34bda8eb713c3aad008adbb589 || :
cp %{_builddir}/qtimageformats-everywhere-src-%{version}/src/3rdparty/libwebp/COPYING %{buildroot}/usr/share/package-licenses/qt6imageformats/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/Qt6/FindLibmng.cmake
/usr/lib64/cmake/Qt6/FindWrapJasper.cmake
/usr/lib64/cmake/Qt6/FindWrapWebP.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QICNSPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QICNSPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QICNSPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QICNSPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QICNSPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QICNSPluginTargets.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTgaPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTgaPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTgaPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTgaPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTgaPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTgaPluginTargets.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTiffPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTiffPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTiffPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTiffPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTiffPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QTiffPluginTargets.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWbmpPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWbmpPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWbmpPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWbmpPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWbmpPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWbmpPluginTargets.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWebpPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWebpPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWebpPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWebpPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWebpPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QWebpPluginTargets.cmake

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/imageformats/libqicns.so
/V3/usr/lib64/qt6/plugins/imageformats/libqtga.so
/V3/usr/lib64/qt6/plugins/imageformats/libqtiff.so
/V3/usr/lib64/qt6/plugins/imageformats/libqwbmp.so
/V3/usr/lib64/qt6/plugins/imageformats/libqwebp.so
/usr/lib64/qt6/plugins/imageformats/libqicns.so
/usr/lib64/qt6/plugins/imageformats/libqtga.so
/usr/lib64/qt6/plugins/imageformats/libqtiff.so
/usr/lib64/qt6/plugins/imageformats/libqwbmp.so
/usr/lib64/qt6/plugins/imageformats/libqwebp.so
/usr/lib64/qt6/sbom/qtimageformats-6.9.0.spdx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6imageformats/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6imageformats/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9
/usr/share/package-licenses/qt6imageformats/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6imageformats/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6imageformats/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
/usr/share/package-licenses/qt6imageformats/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6imageformats/f45ee1c765646813b442ca58de72e20a64a7ddba
