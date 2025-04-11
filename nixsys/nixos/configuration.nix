{ config, pkgs, ... }:
{
  imports = [./hardware-configuration.nix];
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  networking.hostName = "EMMADESK";
  networking.networkmanager.enable = true;
  time.timeZone = "America/Los_Angeles";
  i18n.defaultLocale = "en_US.UTF-8";

  services.xserver.xkb = {
    layout = "us";
    variant = "";
  };
  services.xserver.enable = true;
  services.displayManager.sddm.enable = true;

  users.users.r1shy = { 
    isNormalUser = true;
    extraGroups = [ "networkmanager" "wheel" "audio" "video" ];
  };
nix.settings.experimental-features = [ "nix-command" "flakes" ];
  nixpkgs.config.allowUnfree = true;
  programs.hyprland.enable = true;
  environment.systemPackages = with pkgs; [
    neovim 
    wget
    sddm
    kitty
    firefox
    git
    waybar
  ];
fonts.packages = with pkgs; [ nerdfonts ];
programs.mtr.enable = true;
programs.gnupg.agent = {
     enable = true;
     enableSSHSupport = true;
};

services.openssh.enable = true;
system.stateVersion = "24.11";

}
