from lxml import etree
import os
from CRUD import insert_into

NAMESPACES = {
    'default': 'http://www.nrf-arts.org/IXRetail/namespace/',
    # No need to use VRArtsPoslogExt in namescpaces because we didn't use any.
    # 'VRArtsPoslogExt': 'http://schemas.vismaretail.com/poslog/',
}
DIRECTORY = 'receipts'


def get_files():
    files = os.listdir(DIRECTORY)
    files = [f for f in files if os.path.isfile(DIRECTORY + '/' + f)]
    return files


def get_xml_tree():
    xml_files = []
    for file in get_files():
        xsd_file = "POSLogV6.0.0.xsd"
        xsd_schema = etree.XMLSchema(etree.parse(xsd_file))
        xml_tree = etree.parse(f'{DIRECTORY}\\{file}')
        if xsd_schema.validate(xml_tree):
            # print("XML is valid.")
            xml_files.append(xml_tree)
        else:
            print("XML is NOT valid!")
            for error in xsd_schema.error_log:
                print(error)
    return xml_files


class ReceiptData:
    def __init__(self):
        self.store_id = []
        self.quantity = []
        self.unit_cost_price = []

    def get_store_id(self, file):
        self.store_id.append(file.xpath('//default:UnitID/text()', namespaces=NAMESPACES)[0])
        return self.store_id

    def get_unit_cost_price(self, file):
        self.unit_cost_price.append(file.xpath('//default:LineItem/default:Sale/default:UnitCostPrice/text()',
                                               namespaces=NAMESPACES)[0])
        return self.unit_cost_price

    def get_quantity(self, file):
        self.quantity.append(file.xpath(
            '//default:RetailTransaction/default:LineItem/default:Sale/default:Quantity/text()',
            namespaces=NAMESPACES)[0])
        return self.quantity


receipt_data = ReceiptData()


def get_data():
    for file in get_xml_tree():
        receipt_data.get_store_id(file)
        receipt_data.get_quantity(file)
        receipt_data.get_unit_cost_price(file)
    return receipt_data.store_id, receipt_data.quantity, receipt_data.unit_cost_price


# print(data.quantity)
# insert_into(receipt_data.get_store_id()[0], receipt_data.get_quantity()[0], receipt_data.get_unit_cost_price()[0])

#
