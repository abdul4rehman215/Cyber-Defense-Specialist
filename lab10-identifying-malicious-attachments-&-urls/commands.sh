#!/bin/bash

# Create working directory structure
mkdir -p ~/malware_lab/{attachments,urls,samples,reports}
cd ~/malware_lab

# Upgrade pip
pip3 install --upgrade pip

# Install required Python libraries
pip3 install --user python-magic requests beautifulsoup4

# Update system packages
sudo apt update

# Install required system libraries
sudo apt install -y file libmagic1 python3-magic

# Create test sample files
echo "Normal text document content" > samples/document.txt
echo -e "#!/bin/bash\necho 'Script content'" > samples/script.sh
chmod +x samples/script.sh
echo "Test content" > samples/invoice.pdf.exe
echo "Legitimate business document" > samples/report.docx

# Verify sample files
ls -lh samples/

# Create attachment scanner
nano ~/malware_lab/attachment_scanner.py
chmod +x ~/malware_lab/attachment_scanner.py

# Test single file scan
python3 attachment_scanner.py samples/script.sh

# Test directory scan
python3 attachment_scanner.py samples/

# Create URL test list
nano ~/malware_lab/test_urls.txt

# Create URL analyzer
nano ~/malware_lab/url_analyzer.py
chmod +x ~/malware_lab/url_analyzer.py

# Test single URL scan
python3 url_analyzer.py https://www.google.com

# Test batch URL scan
python3 url_analyzer.py test_urls.txt

# Create integrated scanner
nano ~/malware_lab/integrated_scanner.py
chmod +x ~/malware_lab/integrated_scanner.py

# Create sample email file
nano ~/malware_lab/sample_email.txt

# Run integrated email analysis
python3 integrated_scanner.py sample_email.txt samples/

# Verify generated reports
ls -lh reports/
