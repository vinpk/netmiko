from __future__ import unicode_literals
import time
from netmiko.cisco_base_connection import CiscoSSHConnection


class UbiquitiEdgeSSH(CiscoSSHConnection):
    """
    Implements support for Ubiquity EdgeSwitch devices.

    Mostly conforms to Cisco IOS style syntax with a few minor changes.

    This is NOT for EdgeRouter devices.
    """

    def session_preparation(self):
        self._test_channel_read()
        self.set_base_prompt()
        self.enable()
        self.set_base_prompt()
        self.disable_paging()
        self.set_terminal_width()

        # Clear the read buffer
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()

    def check_config_mode(self, check_string=")#"):
        """Checks if the device is in configuration mode or not."""
        return super(UbiquitiEdgeSSH, self).check_config_mode(check_string=check_string)

    def config_mode(self, config_command="configure"):
        """Enter configuration mode."""
        return super(UbiquitiEdgeSSH, self).config_mode(config_command=config_command)

    def exit_config_mode(self, exit_config="exit"):
        """Exit configuration mode."""
        return super(UbiquitiEdgeSSH, self).exit_config_mode(exit_config=exit_config)

    def exit_enable_mode(self, exit_command="exit"):
        """Exit enable mode."""
        return super(UbiquitiEdgeSSH, self).exit_enable_mode(exit_command=exit_command)

    def save_config(self, cmd="write memory", confirm=False, confirm_response=""):
        """Saves configuration."""
        return super(UbiquitiEdgeSSH, self).save_config(
            cmd=cmd, confirm=confirm, confirm_response=confirm_response
        )
