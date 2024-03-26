Name: nvptx-tools
Version: 20240326
Release: 1
Source0: https://github.com/SourceryTools/nvptx-tools/archive/refs/heads/master.tar.gz
Summary: Binutils-like tools for using Nvidia GPUs with GCC
URL: https://github.com/SourceryTools/nvptx-tools
License: GPL-3.0
Group: Development/Tools

%description
Binutils-like tools for using Nvidia GPUs with GCC

%prep
%autosetup -p1 -n %{name}-master
%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/nvptx-*
%{_prefix}/nvptx-none
