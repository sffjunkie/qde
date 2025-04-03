{
  config,
  lib,
  pkgs,
  ...
}:
let
  app-launcher = pkgs.writeScriptBin "app-launcher" ''
    #!${pkgs.runtimeShell}
    ${lib.getExe pkgs.rofi} \
      -theme-str '@import "looniversity"' \
      -modi drun \
      -show drun
  '';
  inherit (lib) mkDefault mkEnableOption mkIf;
in
app-launcher
