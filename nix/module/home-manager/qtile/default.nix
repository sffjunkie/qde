{
  self,
  config,
  lib,
  pkgs,
  ...
}:
{
  config = lib.mkIf config.looniversity.desktop.environment.qtile.enable {
    xdg.configFile = {
      "qtile" = {
        source = ../../../../qtile/config;
        recursive = true;
      };
    };
  };
}
