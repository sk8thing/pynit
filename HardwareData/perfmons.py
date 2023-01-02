from enum import StrEnum

class Perfmon(StrEnum):
    BASE_CLK = r"\Processor Information(_Total)\Processor Frequency"
    PERFORMANCE = r"\Processor Information(_Total)\% Processor Performance"
    USAGE = r"\Processor Information(_Total)\% Processor Utility"
    THREADS = r"\Process(_Total)\Thread Count"
    CPU_TEMP = r"\Thermal Zone Information(*)\Temperature"
    FREE_MEMORY = r"\Memory\Free & Zero Page List Bytes"
    MODIFIED_MEMORY = r"\Memory\Modified Page List Bytes"