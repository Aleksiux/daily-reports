from lxml import etree
import os
from CRUD import insert_into

NAMESPACES = {
    'default': 'http://www.nrf-arts.org/IXRetail/namespace/',
    # No need to use VRArtsPoslogExt in namescpaces because we didn't use any.
    # 'VRArtsPoslogExt': 'http://schemas.vismaretail.com/poslog/',
}
DIRECTORY = 'receipts'
XSD_SCHEMA = etree.XMLSchema(etree.parse('POSLogV6.0.0.xsd'))


def get_files():
    files = os.listdir(DIRECTORY)
    files = [f"{DIRECTORY}\\{f}" for f in files if os.path.isfile(DIRECTORY + '/' + f)]
    return files


def get_xml_tree():
    xml_files = []

    try:
        for file in get_files():
            with open(file, 'rb') as xml_file:
                xml_tree = etree.parse(xml_file)
                if XSD_SCHEMA.validate(xml_tree) and test_xml_file(xml_tree):
                    print("XML is valid.")
                    xml_files.append(xml_tree)
                else:
                    print("XML is NOT valid!")
                    for error in XSD_SCHEMA.error_log:
                        print(error)
        return xml_files
    except Exception as error:
        print(f"Error processing XML: {error}")


def test_xml_file(xml_tree):
    try:
        full_price = xml_tree.xpath('//default:RetailTransaction/default:Total['
                                    '@TotalType="TransactionNetAmount"]/text()', namespaces=NAMESPACES)[0]
        store_id = xml_tree.xpath('//default:UnitID/text()', namespaces=NAMESPACES)[0]
        quantity = xml_tree.xpath('//default:RetailTransaction/default:LineItem/default:Sale/default:Quantity/text()',
                                  namespaces=NAMESPACES)[0]

        return bool(full_price and store_id and quantity)

    except Exception as error:
        print(f"Error testing XML file: {error}")
        return False


class GetReceiptData:
    def __init__(self):
        self.store_id = []
        self.quantity = []
        self.unit_cost_price = []

    def get_store_id(self, file):
        self.store_id.append(file.xpath('//default:UnitID/text()', namespaces=NAMESPACES)[0])
        return self.store_id

    def get_unit_cost_price(self, file):
        self.unit_cost_price.append(file.xpath('//default:RetailTransaction/default:Total['
                                               '@TotalType="TransactionNetAmount"]/text()',
                                               namespaces=NAMESPACES)[0])
        return self.unit_cost_price

    def get_quantity(self, file):
        self.quantity.append(file.xpath(
            '//default:RetailTransaction/default:LineItem/default:Sale/default:Quantity/text()',
            namespaces=NAMESPACES
        )[0])
        return self.quantity

    def get_data_and_insert(self):
        for file in get_xml_tree():
            self.get_store_id(file)
            self.get_quantity(file)
            self.get_unit_cost_price(file)
        insert_into(self.store_id, self.quantity, self.unit_cost_price)
        return self.store_id, self.quantity, self.unit_cost_price


receipt_data = GetReceiptData()

receipt_data.get_data_and_insert()
