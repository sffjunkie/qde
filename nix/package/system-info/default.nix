{
  config,
  lib,
  pkgs,
  ...
}:
let
  system-info = pkgs.writeScriptBin "system-info" ''
    #!${pkgs.runtimeShell}
    width=$(tput cols)
    ${pkgs.figlet}/bin/figlet -w ''${width} "System Information"
    ${pkgs.fastfetch}/bin/fastfetch
  '';
in
system-info
