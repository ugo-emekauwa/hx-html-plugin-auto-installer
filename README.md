# HyperFlex HTML Plug-In Automated Installer

The HyperFlex HTML Plug-In Automated Installer automates installing the Cisco HyperFlex HTML Plug-In for VMware vCenter.

## Prerequisites:
1. Python 3 installed, which can be downloaded from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Clone or download the HyperFlex HTML Plug-In Automated Installer repository by using the ![GitHub Code Button](./assets/GitHub_Code_Button.png "GitHub Code Button") link on the main repository web page or by running the following command:
    ```
    git clone https://github.com/ugo-emekauwa/hx-html-plugin-auto-installer
    ```
3. Install the required Python module **paramiko**. The requirements.txt file in the repository can be used by running the following command:
    ```
    python -m pip install -r requirements.txt
    ```
4. The IP address of one the service controller VMs on the targeted Cisco HyperFlex cluster.
5. User credentials with administrative rights on the targeted Cisco HyperFlex cluster.
6. The IP address of the targeted VMware vCenter managing the VMware ESXi hosts of the Cisco HyperFlex cluster.
7. User credentials with administrative rights on the targeted VMware vCenter.
8. A copy of the latest Cisco HyperFlex HTML Plug-In for VMware vCenter .zip file. This can be downloaded from the [Cisco Software Download Site](https://software.cisco.com/download/home/286305544/type/286305994/release).

## How to Use:
1. Please ensure that the above prerequisites have been met.
2. Open the **hx_datastore_safeguard.py** file in an IDE or text editor.
3. Go to the comment section named **Required Variables**, as shown below.
    ```python
    ######################
    # Required Variables #
    ######################
    ```
4. Provide values for the variables listed under **Required Variables**. Samples values are already provided.
5. Save and then run **hx_vc_html_plugin_auto_installer.py** directly from your IDE or from the command line e.g.:
    ```
    python hx_html_plugin_auto_installer.py
    ```

## Use Cases:
The HyperFlex HTML Plug-In Automated Installer is part of the automation solution used to support and maintain the following upcoming Cisco Data Center product demonstrations on Cisco dCloud:

1. _Cisco HyperFlex Edge 4.5 with Intersight v1 (All Flash, 3-Node)_
2. _Cisco HyperFlex Edge 4.5 with Intersight v1 (All Flash, 2-Node)_
3. _Cisco HyperFlex Edge 4.5 with Intersight v1 (Hybrid, 2-Node)_

Cisco dCloud is available at [https://dcloud.cisco.com](https://dcloud.cisco.com), where product demonstrations and labs can be found in the Catalog.

## Related Tools:
Here are similar tools to help deploy and manage Cisco HyperFlex.
- [HyperFlex Notification Tool for Cisco Intersight](https://github.com/ugo-emekauwa/hyperflex-notification-tool)
- [Cisco HyperFlex API Token Manager](https://github.com/ugo-emekauwa/hx-api-token-manager)
- [HyperFlex Edge Automated Deployment Tool for Cisco Intersight](https://github.com/ugo-emekauwa/hx-auto-deploy)

## Author:
Ugo Emekauwa

## Contact Information:
uemekauw@cisco.com or uemekauwa@gmail.com
