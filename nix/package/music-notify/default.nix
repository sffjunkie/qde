{
  config,
  lib,
  pkgs,
  ...
}:
let
  ffmpeg = "${pkgs.ffmpeg}/bin/ffmpeg";
  mpc = "${pkgs.mpc-cli}/bin/mpc";
  notify-send = "${pkgs.libnotify}/bin/notify-send";
  music-notify = pkgs.writeScriptBin "music-notify" ''
    #!${pkgs.runtimeShell}
    music_dir="/mnt/music"
    filename="$(${mpc} --format "$music_dir"/%file% current)"

    previewdir="/tmp/ncmpcpp_previews"
    mkdir -p $previewdir
    previewname="$previewdir/$(${mpc} --format %album% current | base64).png"
    [ -e "$previewname" ] || ${ffmpeg} -y -i "$filename" -an -vf scale=512:512 "$previewname" > /dev/null 2>&1

    ${notify-send} -a music-notify -r 27072 -t 2000 "Now Playing" "$(${mpc} --format '%title% by %artist% in %album%' current)" -i "$previewname"
  '';
  inherit (lib) mkEnableOption mkIf;
in
music-notify
