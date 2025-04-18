{
  description = "QTile based desktop environment";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs =
    {
      self,
      nixpkgs,
      ...
    }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [
        "aarch64-linux"
        "x86_64-linux"
      ];
    in
    {
      packages = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          app-launcher = pkgs.callPackage ./nix/package/app-launcher { inherit pkgs; };
          clipboard = pkgs.callPackage ./nix/package/clipboard { inherit pkgs; };
          music-notify = pkgs.callPackage ./nix/package/music-notify { inherit pkgs; };
          system-info = pkgs.callPackage ./nix/package/system-info { inherit pkgs; };
          system-menu = pkgs.callPackage ./nix/package/system-menu { inherit pkgs; };
        }
      );

      nixosModules = {
        default =
          {
            config,
            lib,
            pkgs,
            ...
          }:
          import ./nix/module/nixos/qde {
            inherit
              config
              lib
              pkgs
              self
              ;
          };
      };

      homeManagerModules = {
        qtile =
          {
            config,
            lib,
            pkgs,
            ...
          }:
          import ./nix/modules/home-manager/qtile {
            inherit
              config
              lib
              pkgs
              self
              ;
          };

        settings =
          {
            config,
            lib,
            pkgs,
            ...
          }:
          import ./nix/modules/home-manager/settings {
            inherit
              config
              lib
              pkgs
              self
              ;
          };

        theme =
          {
            config,
            lib,
            pkgs,
            ...
          }:
          import ./nix/modules/home-manager/theme {
            inherit
              config
              lib
              pkgs
              self
              ;
          };
      };

      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.buildPackages.python312;

          libPath = pkgs.lib.makeLibraryPath [
            pkgs.cairo
            pkgs.gdk-pixbuf
            pkgs.glib
            pkgs.libxkbcommon
            pkgs.pango
            pkgs.xorg.libxcb
          ];
        in
        {
          default = pkgs.mkShell {
            nativeBuildInputs = [
              python

              pkgs.uv
              pkgs.mypy
              python.pkgs.coverage
              python.pkgs.pytest

              python.pkgs.dbus-fast
              python.pkgs.mpd2
              python.pkgs.pulsectl-asyncio
              python.pkgs.pydantic

              self.packages.x86_64-linux.app-launcher
              self.packages.x86_64-linux.clipboard
              self.packages.x86_64-linux.music-notify
              self.packages.x86_64-linux.system-info
              self.packages.x86_64-linux.system-menu
            ];

            shellHook = ''
              export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${libPath}
            '';
          };
        }
      );
    };
}
