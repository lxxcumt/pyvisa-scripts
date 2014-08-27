def amrelsps_constant_current(instrument, setcurrent=0, output_on=0):
    """Put Amrel SPS8-150-K0E1 programmable power supply into constant current mode.

    :param instrument: Instrument object to control. Use get_instrument() function of
                       visa.ResourceManager() object to assign a name to an instrument.
    :param setcurrent: Sets the current (unit ampere). Defaults to 0.
    :param output_on:  Controls instrument output status, i.e. output_on=1 means the
                       instrument outputs current, output_on=0 means it does not. Defaults to 0.
    """
    instrument.write('CURRent %f; OUTPut %d' % (setcurrent, output_on))

def amrelsps_constant_voltage(instrument, setvoltage=0, output_on=0):
    """Put Amrel SPS8-150-K0E1 programmable power supply into constant voltage mode.

    :param instrument: Instrument object to control. Use get_instrument() function of
                       visa.ResourceManager() object to assign a name to an instrument.
    :param setvoltage: Sets the voltage (unit volt). Defaults to 0.
    :param output_on:  Controls instrument output status, i.e. output_on=1 means the
                       instrument outputs current, output_on=0 means it does not. Defaults to 0.
    """
    instrument.write('VOLTage %f; OUTPut %d' % (setvoltage, output_on))
