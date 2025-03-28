{
  self,
  config,
  lib,
  pkgs,
  ...
}:
{
  config = lib.mkIf config.looniversity.desktop.environment.qtile.enable {
    xdg.configFile."desktop/default_settings.yaml".text = lib.generators.toYAML { } {
      keys = {
        Alt = "mod1";
        Ctrl = "control";
        Hyper = "mod3";
        Shift = "shift";
        Super = "mod4";
      };

      apps = {
        system-status = "${pkgs.htop}";
        system-menu = "${self.packages."${pkgs.system}".system-menu}";
        system-info = "${self.packages."${pkgs.system}".system-info}";
      };

      group = [
        {
          name = "WWW";
          options = {
            layout = "monadtall";
          };
          matches = [
            "brave-browser"
            "chromium"
            "firefox"
          ];
        }
        {
          name = "BRAIN";
          options = {
            layout = "max";
          };
          matches = [ "obsidian" ];
        }
        {
          name = "CODE";
          options = {
            layout = "max";
          };
          matches = [ "code-url-handler" ];
        }
        {
          name = "TERM";
          options = {
            layout = "monadtall";
          };
        }
        {
          name = "DOC";
          options = {
            layout = "monadtall";
          };
        }
        {
          name = "CHAT";
          options = {
            layout = "monadtall";
          };
          matches = [ "discord" ];
        }
        {
          name = "MUSIC";
          options = {
            layout = "monadtall";
          };
        }
        {
          name = "VIDEO";
          options = {
            layout = "max";
          };
        }
        {
          name = "GFX";
          options = {
            layout = "max";
          };
          matches = [
            "Darktable"
            "Gimp-\d+\.\d+"
            "org\.inkscape\.Inkscape"
          ];
        }
      ];
    };
  };
}
