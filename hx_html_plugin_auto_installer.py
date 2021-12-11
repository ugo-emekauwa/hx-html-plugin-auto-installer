"""
HyperFlex HTML Plug-In Automated Installer v1
Author: Ugo Emekauwa
Contact: uemekauw@cisco.com, uemekauwa@gmail.com
Summary: The HyperFlex HTML Plug-In Automated Installer automates installing
         the Cisco HyperFlex HTML Plug-In for VMware vCenter.
Notes: Tested on Cisco HyperFlex HTML Plug-In for VMware vCenter 2.0.0, HyperFlex 4.5(1a), and VMware vCenter 7.0.1.003
"""

# Import needed Python modules
import sys
import time
import paramiko


######################
# Required Variables #
######################
hx_vc_html_plugin_file_name = "HyperFlex-VC-HTML-Plugin-2.1.0.zip"
hx_vc_html_plugin_local_directory = "c:\\Software\\"
hxdp_remote_workspace_directory = "/home/admin/tmp_hx_vc_html_plugin_install/"
hxdp_service_controller_vm_ip_address = "198.18.135.100"
hxdp_service_controller_vm_username = "admin"
hxdp_service_controller_vm_password = "C1sco12345!"
vcenter_username = "administrator@vsphere.local"
vcenter_password = "C1sco12345!"


# Setup function to print SSH output from the HXDP Service Controller VM
def returned_ssh_output(max_data_byte_size=1024):
    """This is a function that returns the SSH output when using the Paramiko
    SSH client.

    Args:
        max_data_byte_size: The maximum byte size of the returned SSH output
            data. The default is 1024 bytes.

    Returns:
        The returned SSH output, if available. The returned SSH output data is
        converted from bytes to a UTF-8 encoded string.
    """
    
    if ssh_client_shell.recv_ready():
        returned_ssh_output = ssh_client_shell.recv(max_data_byte_size)
        return f"Returned SSH Output: {returned_ssh_output.decode('utf-8')}"
    else:
        return "There is no returned SSH output available."


# Setup function to send SSH commands to the HXDP Service Controller VM
def send_ssh_command(command, response_delay=5):
    """This is a function to send commands over SSH when using the Paramiko SSH
    client.

    Args:
        command: The commands to be sent over SSH. The commands should be
            provided in string format.
        response_delay: The time delay in seconds after sending the provided
            SSH command. The time delay allows for the sent SSH command to be
            fully processed before another command is sent. The default is 
            five seconds.

    Returns:
        The returned SSH output, if available. The returned SSH output data is
        converted from bytes to a UTF-8 encoded string.
    """
    
    ssh_client_shell.send(command)
    time.sleep(response_delay)
    result = returned_ssh_output()
    return result


try:
    # Start the HyperFlex HTML Plug-In Automated Installer
    print("Starting the HyperFlex HTML Plug-In Automated Installer...\n")

    # Setup the SSH client
    print("Setting up the SSH client...\n")
    ssh_client = paramiko.SSHClient()

    # Configure the SSH client to accept missing host keys
    print("Configuring the SSH client to accept missing host keys...\n")
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect the SSH client to the target HXDP Service Controller VM
    print("Connecting the SSH client to the target HXDP Service Controller VM...\n")
    ssh_client.connect(hostname = hxdp_service_controller_vm_ip_address,
                       username = hxdp_service_controller_vm_username,
                       password = hxdp_service_controller_vm_password)

    # Setup the SSH client shell
    print("Setting up the SSH client shell...\n")
    ssh_client_shell = ssh_client.invoke_shell()

    # Send command over SSH to create a work space directory on the HXDP Service Controller VM
    print("Sending command over SSH to create a work space directory on the HXDP "
          "Service Controller VM...\n")
    send_ssh_command(f"mkdir {hxdp_remote_workspace_directory}\n")

    # Setup the SFTP client
    print("Setting up the SFTP client...\n")
    sftp_client = ssh_client.open_sftp()

    # Transfer over SFTP the HX vCenter HTML plug-in file from the local source directory to the work space directory on the HXDP Service Controller VM
    print("Transferring over SFTP the HX vCenter HTML plug-in file from the local "
          "source directory to the work space directory on the HXDP Service "
          "Controller VM...\n")
    sftp_client.put(f"{hx_vc_html_plugin_local_directory}{hx_vc_html_plugin_file_name}",
                    f"{hxdp_remote_workspace_directory}{hx_vc_html_plugin_file_name}")

    # Close the SFTP client
    print("Closing the SFTP client...\n")
    sftp_client.close

    # Send command over SSH to change to the work space directory on the HXDP Service Controller VM
    print("Sending command over SSH to change to the work space directory on the HXDP Service Controller VM...\n")
    send_ssh_command(f"cd {hxdp_remote_workspace_directory}\n")

    # Send command over SSH to unzip the HX vCenter HTML plug-in file
    print("Sending command over SSH to unzip the HX vCenter HTML plug-in file...\n")
    send_ssh_command(f"unzip -u {hx_vc_html_plugin_file_name}\n")

    # Provide buffer for unzipping the HX vCenter HTML plug-in file
    print("Providing 20 second buffer for unzipping the HX vCenter HTML plug-in file...\n")
    time.sleep(20)

    # Send command over SSH to run the install_vc_plugin.py script on the HXDP Service Controller VM
    print("Sending command over SSH to run the install_vc_plugin.py script on the "
          "HXDP Service Controller VM...\n")
    send_ssh_command("install_vc_plugin\n")

    # Send command over SSH to enter the HXDP Service Controller 'admin' password for the install_vc_plugin.py script
    print("Sending command over SSH to enter the HXDP 'admin' username password for "
                 "the install_vc_plugin.py script...\n")
    send_ssh_command(f"{hxdp_service_controller_vm_password}\n")

    # Send command over SSH to enter the VMware vCenter username for the install_vc_plugin.py script
    print("Sending command over SSH to enter the VMware vCenter username for the "
                 "install_vc_plugin.py script...\n")
    send_ssh_command(f"{vcenter_username}\n")

    # Send command over SSH to enter the VM vCenter password for the install_vc_plugin.py script
    print("Sending command over SSH to enter the VMware vCenter password for the "
                 "install_vc_plugin.py script...\n")
    hx_vc_html_plugin_install_result = send_ssh_command(f"{vcenter_password}\n")

    # Provide buffer for login to VMware vCenter
    print("Providing 20 second buffer for login to VMware vCenter...\n")
    time.sleep(20)

    # Check if the Cisco HyperFlex HTML Plug-In for VMware vCenter is already installed
    hx_vc_html_plugin_installed_keyphrase = "is already installed"
    if hx_vc_html_plugin_installed_keyphrase in hx_vc_html_plugin_install_result:
        print("The Cisco HyperFlex HTML Plug-In for VMware vCenter is already "
              "installed.\n")
        print("The HyperFlex HTML Plug-In Automated Installer will now exit.\n")
        # Close the SSH client connection to the HXDP Service Controller VM
        print("Closing the SSH client connection to the HXDP Service Controller VM...\n")
        ssh_client.close
    else:
        print("The install process for the Cisco HyperFlex HTML Plug-In for "
              "VMware vCenter has completed.\n")
        # Close the SSH client connection to the HXDP Service Controller VM
        print("Closing the SSH client connection to the HXDP Service Controller VM...\n")
        ssh_client.close
except Exception as exception_message:
    print("Unable to complete running the HyperFlex HTML Plug-In Automated Installer due to an error.\n")
    print(f"Exception Message: {exception_message}\n")
    print("Exiting the HyperFlex Cluster Post-Deployment Tasks Tool due to the error.\n")
    sys.exit(0)

# Exit the HyperFlex HTML Plug-In Automated Installer
print("Exiting the HyperFlex HTML Plug-In Automated Installer.\n")
sys.exit(0)
