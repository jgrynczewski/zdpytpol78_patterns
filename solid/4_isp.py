# isp

# class IMachine:
#     def print(self, document):
#         ...
#
#     def fax(self, document):
#         ...
#
#     def scan(self, document):
#         ...
#
#
# class MultiFunctionalPrinter(IMachine):
#     def print(self, document):
#         ...
#
#     def fax(self, document):
#         ...
#
#     def scan(self, document):
#         ...
#
#
# class OldFashionedPrinter(IMachine):
#     def print(self, document):
#         ...
#
#     def fax(self, document):
#         raise NotImplemented("Printer cannot fax")
#
#     def scan(self, document):
#         raise NotImplemented("Printer cannot scan")
#
#


class IPrinterInterface:
    def print(self, document):
        ...


class IFaxInterface:
    def fax(self, document):
        ...


class IScannerInterface:
    def scan(self, document):
        ...


class OldFashionedPrinter(IPrinterInterface):
    def print(self, document):
        ...


class MultiFunctionalPrinter(IPrinterInterface, IFaxInterface, IScannerInterface):
    def print(self, document):
        ...

    def fax(self, document):
        ...

    def scan(self, document):
        ...
