{ pkgs }: {
  deps = [
    pkgs.nodejs-16_x
    pkgs.jq.bin
    pkgs.jq.bin
    pkgs.busybox
    pkgs.whois
    pkgs.vimHugeX
    pkgs.python38Full
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}