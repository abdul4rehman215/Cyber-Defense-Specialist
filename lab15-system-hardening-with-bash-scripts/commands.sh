# Create working directory
mkdir ~/system-hardening
cd ~/system-hardening
pwd

# Create main hardening script
nano system_hardening.sh
chmod +x system_hardening.sh
sudo ./system_hardening.sh

# Create user security script
nano user_security.sh
chmod +x user_security.sh
sudo ./user_security.sh

# Create firewall configuration script
nano firewall_config.sh
chmod +x firewall_config.sh
sudo ./firewall_config.sh

# Create advanced iptables protection script
nano iptables_advanced.sh
chmod +x iptables_advanced.sh
sudo ./iptables_advanced.sh

# Create SSH hardening script
nano ssh_hardening.sh
chmod +x ssh_hardening.sh
sudo ./ssh_hardening.sh

# Create SSH validation script
nano validate_ssh.sh
chmod +x validate_ssh.sh
./validate_ssh.sh

# Create filesystem security script
nano filesystem_security.sh
chmod +x filesystem_security.sh
sudo ./filesystem_security.sh

# Create verification script
nano verify_hardening.sh
chmod +x verify_hardening.sh
sudo ./verify_hardening.sh
