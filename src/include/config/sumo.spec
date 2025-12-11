Name:           sumo
Summary:        3D Aircraft modeling, mesh generation & postprocessing
Version:        2.7.6
Release:        1
License:        GPL
Group:          Productivity/Scientific
Source:         sumo-%{version}.tar.xz

BuildRoot:      %{_tmppath}/build-root-%{name}
Packager:       David Eller
Url:            http://www.larosterna.com/sumo.html
Provides:       sumo
Provides:       scope
Vendor:         KTH Flight Dynamics

# use LZMA compression for binary and gzip for source
%define _binary_payload w7.xzdio
%define _source_payload w0.gzdio

# icon directory
%define ico_dir_kde3 /opt/kde3/share/icons/hicolor/128x128/apps
%define ico_dir_kde4 /usr/share/icons/hicolor/48x48/apps/

# directory naming logic
# we install into a fixed location for now
# %define dwf_revision r__SUMO_REVISION__
%define dwf_prefix /usr/local/larosterna/

%ifos linux

%ifarch x86_64

%define qspec linux-g++-64
%define lib_dir    lib64
%define bitenv     BITFLAG="-m64"
%endif

%ifarch i386 i586 i686
%define qspec linux-g++-32
%define lib_dir    lib
%define bitenv     BITFLAG="-m32"
%endif

%define dwf_libdir %{dwf_prefix}/%{lib_dir}
%define dwf_bindir %{dwf_prefix}/bin

%endif  # linux

%description

Sumo is an open-source program surface modeling program for aircraft geometries. 
It is not a full-featured CAD system, but rather strongly specialized towards 
the efficient creation of both conventional and innovative aircraft geometries.
Furthermore, sumo can automatically generate unstructured surface meshes for use 
with the dwfs unsteady potential flow solver.

Scope is the companion program to visualize data on unstructured surface meshes.
It can display mesh files, draw color contour plots for scalar surface data, 
animate deformations such as structural eigenmodes or complex-valued flutter
modeshapes. Additionally, it can be used to show trajectories which result from
flight simulations, even including structural deformations.

svn revision: r5371

%changelog 
* Thu Oct 1 2015 David Eller <david@larosterna.com>
- scope : Improved deformation mapping
- scope : Import ply stress data from PCH files
- scope : Simplify load mapping for multiple load cases
- scope : Generate abs-max value fields across stress subcases
- sumo  : Incorporate robustness improvements in hybrid mesh generation
- sumo  : Elongate/droop airfoils for fairings

* Fri Nov 7 2014 David Eller <david@larosterna.com>
- scope : Fix crash in deformation smoothing solver
- sumo  : Improve fitting of very thin airfoils from overlay

* Mon Oct 20 2014 David Eller <david@larosterna.com>
- scope : Better performance on Hi-DPI screens
- scope : Generate search trees on demand, not on load
- sumo  : Improved hybrid mesh generation when NLopt present

* Thu Jul 31 2014 David Eller <david@larosterna.com>
- scope : Many improvements to deformation mapping
- scope : Improved slice plots & printing
- scope : Import of AEREL files now supported (thanks Mikaela!)
- sumo  : Mouse event handling bugfix

* Wed Mar 19 2014 David Eller <david@larosterna.com>
- scope : Improved mapping of deformations
- sumo  : Improved RANS volume mesh generation with tetgen-1.5

* Wed Nov 20 2013 David Eller <david@larosterna.com>
- scope : Updated deformation mapping
- scope : Many bugfixes in NASTRAN import
- scope : Modified OpenGL rendering backend
- sumo  : Experimental integration of hybrid mesh generator
- sumo  : Better error handling
- global: Add command-line tools to RPM package

* Tue Mar 5 2013 David Eller <david@larosterna.com>
- scope : bugfix for handling of trajectory w/o structural states
- scope : Sidebar tree to simplify renaming and access of structured solutions
- scope : Display mesh annotations
- scope : New GUI for displacement mapping
- sumo  : quick, preliminary bugfix in sidebar tree update 
- sumo  : Better handling of inconsistent .smx files from external sources

* Thu Nov 29 2012 David Eller <david@larosterna.com>
- scope : New formats: SU2, Legacy VTK
- sumo : Many bugs fixed in airfoil-to-overlay fitting procedure
- sumo : Support volume mesh export in non-standard CGNS (BCs as sections)
- sumo : New mesh export format: SU2

* Thu Sep 6 2012 David Eller <david@larosterna.com>
- scope : Very basic support for Abaqus mesh read/write
- sumo : New batch mode functions
- sumo : Fit airfoil sections to overlay

* Sun Jun 3 2012 David Eller <david@larosterna.com>
- scope : New function for sections through surface meshes
- Rebuilding for ubuntu 12.04 (netcdf dependency problem)

* Fri Apr 13 2012 David Eller <david@larosterna.com>
- scope : Support for i/o of simple TAU mesh files
- sumo : Volume wave drag computation integrated 
- sumo : Numerous improvements to IGES overlay import
- sumo : Experimental support for writing TAU mesh files
- sumo : Bugfix for batch mode (mesh settings not read correctly)
- libs : Many, many bugfixes in libraries

* Tue Jan 3 2012 David Eller <david@larosterna.com>
- sumo : Support importing STL overlay
- sumo : Much improved performance in overlay handling
- scope : Bugfix in section/boco color handling

* Wed Sep 21 2011 David Eller <david@larosterna.com>
- sumo : Remove internal tetrahedra from multiple unconnected components
- sumo : Write STL files which gmsh can understand

* Mon Aug 8 2011 David Eller <david@larosterna.com>
- sumo: Optionally reversed parametrization in wing sections
- sumo: Manual ordering of sections within wing
- scope: Improved GUI for load mapping 

* Mon May 16 2011 David Eller <david@larosterna.com>
- Show sections of IGES/Step geometry in frame editor
- Implement fit-to-overlay for points and frames 
- Improved NASTRAN import in scope
- First implementation of GUI for load mapping

* Wed Jan 19 2011 David Eller <david@larosterna.com>
- Display IGES/STEP geometry as overlay on top of sumo geometry
- Numerous bugfixes in scope, improve hedgehog plots
- Improve handling of mesh files with hundreds of data fields

* Wed Oct 13 2010 David Eller <david@gmx.net>
- Maintenance release
- Displacement visualization in scope, new hedgehog plot type
- Improve display of quadratic elements (Tria6, Tet10) in scope
- Implemented drag'n'drop support in sumo and scope (input files)
- Improved IGES export - maintain product structure, export section curves
- Minor UI improvements
- Several minor bufixes

* Thu Mar 4 2010 David Eller <david@gmx.net>
- Bugfix release

* Tue Feb 9 2010 David Eller <david.eller@gmx.net>
- Scope : Update flight path visualization
- Scope : Implement mesh transformations
- Scope : Mesh mergings/overlay for modeshape comparison etc.
- Sumo : Improve ceasiom import, better diagnostics
- Sumo : Additional end cap type (polar)

* Mon Nov 30 2009 David Eller <david.eller@gmx.net>
- Sumo : Improved engine inlet model
- Sumo : Bugfixes related to inlet mesh generation
- Switch to MSVC on Microsoft operating systems. 

* Fri Nov 6 2009 David Eller <david.eller@gmx.net>
- Sumo : Simple engine inlet modelling
- Sumo : Improve accuracy of lateral/top drawings 
- Scope : Simple dwfs interface for steady analyses
- Scope : Display surface mesh quality (stretch)
- Scope : Display stretched tetraedra
- Scope : Vector fields as tuffts (no streamlines yet))
- Correctly package image plugins on windows

* Tue Sep 1 2009 David Eller <david.eller@gmx.net>
- Replaced scope with 1.5.2, new volume mesh drawing
- Improvements in handling very large xml files 
- Moved multithreading support to boost for portability
- Use OpenGL VBOs where available
- Bugfix for background images (+enable in frame view)

* Wed Jul 15 2009 David Eller <david.eller@gmx.net>
- Add zip file support to libgenua
- Fix ambiguities in FFA file format support
- Revert and minor bugfixes in sumo
- scope : dump animation frames for movies

* Thu Apr 30 2009 David Eller <david.eller@gmx.net>
- Update to scope : Fix bug in Nastran import

* Thu Mar 19 2009 David Eller <david.eller@gmx.net>
- Bugfix in IGES export
- Bugfix for body cap/main surface intersection
- Mark ceasiom engine inlet/nozzle surfaces as such
- Change ceasiom control surface definition to relative span

* Fri Feb 27 2009 David Eller <david.eller@gmx.net>
- Insert a further refinement pass after intersection
  to improve robustness for coarse mesh generation
- Many small bufixes
- Use all processor cores, whenever possible
- Complete ceasiom import for pylons and fairings

* Tue Feb 10 2009 David Eller <david.eller@gmx.net>
- Implemented mesh cut, area distributions
- Lots of bug fixes and quality improvements over 1.8.1
- Link statically against Qt 4.4.3 for compatibility with older systems

* Tue Jan 27 2009 David Eller <david.eller@gmx.net>
- Integrated completely new intersection computation
- Tag components in final mesh

* Tue Nov 11 2008 David Eller <david.eller@gmx.net>
- Added some support for CEASIOM xml files
- TE/LE refinement option for wing meshes
- Builtin airfoil library 

* Mon Jun 16 2008 David Eller <david.eller@gmx.net>
- Updated most template models, added bjet and widebody
- Fix crash in control pattern definitions

* Thu Jun 12 2008 David Eller <david.eller@gmx.net>
- Allow editing of control points in frame view
- Crash in adaptive mesh merge fixed 
- Sumo simplifies skinned surfaces to 100 control points (IGES)
- Fixed visualization bug for kinked wings
- Remember tetgen settings during session

* Thu May 29 2008 David Eller <david.eller@gmx.net>
- Updated sources to sumo 1.6
- Experimental support for IGES export
- Bugfix for bmsh/FFA files on windows
- Additional options for tetgen interface
- Background images in skeleton view

* Mon May 19 2008 David Eller <david.eller@gmx.net>
- Updated sources to sumo 1.5
- Export volume mesh in edge bmsh format
- Improved robustness for complex body intersections

* Mon Apr 7 2008 David Eller <david.eller@gmx.net>
- Updated sources to sumo 1.4
- Major addition: Volume mesh generation using tetgen

* Wed Jan 23 2008 David Eller <david.eller@gmx.net>
- Included examples cases in rpm package

* Mon Jan 21 2008 David Eller <david.eller@gmx.net>
- Updated sources to sumo 1.3 
- Several bugfixes in scope/trajectory visualization

* Tue Jan 15 2008 David Eller <david.eller@gmx.net>
- Adapted to provide both sumo and scope

* Mon Jan 14 2008 David Eller <david.eller@gmx.net>
- initial rpm release

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build

DEVTOOLS=/opt/rh/devtoolset-2/root/usr/bin/
if [[ -x "/opt/rh/devtoolset-2/root/usr/bin/g++" ]]
then
export CC=$DEVTOOLS/gcc
export CXX=$DEVTOOLS/g++
elif [[ -x "/usr/bin/g++-4.7" ]]
then
export CC="gcc-4.7"
export CXX="g++-4.7"
fi

if [[ -x "/opt/Qt/5/bin/qmake" ]]
then
  QMK=/opt/Qt/5/bin/qmake
elif [[ -x "/opt/Qt/4/bin/qmake" ]]
then
  QMK=/opt/Qt/4/bin/qmake
else
  QMK=qmake
fi

QCFG="CONFIG+=release CONFIG-=debug CONFIG*=distrib"

cd src/boost
$QMK -spec %{qspec} $QCFG
make %{?_smp_mflags}

cd ../QGLViewer/QGLViewer
$QMK -spec %{qspec} $QCFG
make %{?_smp_mflags}

cd ../../predicates
$QMK -spec %{qspec} $QCFG
make %{?_smp_mflags}

cd ../genua
$QMK -spec %{qspec} $QCFG genua.pro -o Makefile
make %{?_smp_mflags}

cd ../surf
$QMK -spec %{qspec} $QCFG surf.pro -o Makefile
make %{?_smp_mflags}

cd ./tools/surfmap
$QMK -spec %{qspec} $QCFG surfmap.pro -o Makefile
make %{?_smp_mflags}

cd ../../tools/pentagrow
$QMK -spec %{qspec} $QCFG pentagrow.pro -o Makefile
make %{?_smp_mflags}
cd ../..

cd ../sumo
$QMK -spec %{qspec} $QCFG sumo.pro -o Makefile
make %{?_smp_mflags}

cd ../scope
$QMK -spec %{qspec} $QCFG scope.pro -o Makefile
make %{?_smp_mflags}

cd ../tetgen
make clean
make -j2
strip tetgen
cp tetgen ../../bin

cd ../..
strip bin/*

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}%{dwf_prefix}
mkdir -p %{buildroot}/usr/local/bin

cp -a bin doc %{buildroot}%{dwf_prefix}

ln -s %{dwf_prefix}/bin/pentagrow $RPM_BUILD_ROOT/usr/local/bin/pentagrow
ln -s %{dwf_prefix}/bin/surfmap $RPM_BUILD_ROOT/usr/local/bin/surfmap
ln -s %{dwf_prefix}/bin/tetgen $RPM_BUILD_ROOT/usr/local/bin/tetgen
ln -s %{dwf_prefix}/bin/dwfsumo $RPM_BUILD_ROOT/usr/local/bin/sumo
ln -s %{dwf_prefix}/bin/dwfscope $RPM_BUILD_ROOT/usr/local/bin/scope

if [ -d %{ico_dir_kde4} ]; then
  echo "KDE4 icon directory found." 
  mkdir -p %{buildroot}%{ico_dir_kde4}
  cp src/sumo/icons/sumo.png %{buildroot}%{ico_dir_kde4}
fi

%clean
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}

%files

%defattr(-,root,root)

%{dwf_prefix}
%{ico_dir_kde4}
/usr/local/bin/pentagrow
/usr/local/bin/surfmap
/usr/local/bin/sumo
/usr/local/bin/scope
/usr/local/bin/tetgen
