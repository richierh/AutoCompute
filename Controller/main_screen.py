
from View.MainScreen.main_screen import MainScreenView
from kivy.clock import Clock
import threading
from time import sleep


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)
        # self.view.label_activate.text='activate'

    def get_view(self) -> MainScreenView:
        return self.view
    
    def add_outbound(self):
        return self.model.add_outbound()
    
    def add_inbound(self):
        return self.model.add_inbound()
    
    def add_adjustment(self):
        return self.model.add_adjustment()
    
    def add_inventory(self):
        return self.model.add_inventory()
    
    def sum_qty_inventory(self):
        return self.model.sum_qty_inventory()
    
    def update_inventory_temp(self,id,data):
        self.id = id
        self.data=data
        return self.model.update_inventory_temp(self.id,data)

    def query_all_inv_in_ou_ad(self):
        return self.model.query_all_inv_in_ou_ad()
    
    def get_adjustment(self):
        return self.model.get_adjustment(self)
        
    def get_outbound(self):
        return self.model.get_outbound(self)
    
    def get_inventory(self):
        return self.model.get_inventory(self)
    
    def get_inbound(self):
        return self.model.get_inbound(self)

    def get_qty_by(self):
        
        return self.model.get_qty_by()
    
    def delete_all_rows(self):
        self.model.delete_all_rows()


    def thread_while(self):

        while self.thread1 :
            # try:
            sleep(3)
            print('f')
            if self.view.label_activate.text =='unactivate':
                break

            self.id = ["inbound",'outbound','adjustment']

            self.get_qty_by()
            out_r,out_qty = self.get_outbound()
            adj_r,adj_qty = self.get_adjustment()
            inb_r,inb_qty = self.get_inbound()
            if self.get_qty_by()[0]!=inb_qty or self.get_qty_by()[1]!=out_qty or self.get_qty_by()[2]!=adj_qty:
                inv_r,inv_qty = self.get_inventory()
                self.model.delete_value(inv_r,self)

                self.data_inventory_from_inbound = []
                for data in inb_r:
                    data_in = {
                        'Header': data[0],
                        'No':data[1],
                        'Receive Date':data[2],
                        'Document No':data[3],
                        'Consigne':data[4],
                        'Nopol':data[5],
                        'Material':data[6],
                        'Material Description':data[7],
                        'Batch':data[8],
                        'Inbound Qty':data[9],
                        'Uom':data[10],
                        'PLTID':data[11],
                        'Location':data[12],
                        'status':data[13],
                        'Remarks':data[14],
                        'User':data[15]
                    }
                    data_inv_from_inbound = [data_in.get('No'),
                                                data_in.get('Receive Date'),
                                                data_in.get('Location'),
                                                data_in.get('PLTID'),
                                                data_in.get('Material'),
                                                data_in.get('Material Description'),
                                                data_in.get('Batch'),
                                                data_in.get('Uom'),
                                                data_in.get('Inbound Qty'),
                                                "0",
                                                "0",
                                                data_in.get('Status'),
                                                "0",
                                                data_in.get('Remarks'),
                                                "0"                                              
                                                ]
                    self.data_inventory_from_inbound.append(data_inv_from_inbound)

                print('okay')
                print('okay')
                print('okay')
                print('okay')
                print('okay')
                print('okay')
                print('okay')
                print('okay')
                print('okay')
                print('okay')
                print('okay')
                # keys for inbound

                self.data_qty = [['inbound',inb_qty],['outbound',out_qty],['adjustment',adj_qty],['inventory',inv_qty]]
                keys_inbound = [
                'Header', 'No', 'Receive Date', 'Document No', 'Consigne', 'Nopol',
                'Material', 'Material Description', 'Batch', 'Inbound Qty', 'Uom',
                'PLTID', 'Location', 'Remarks', 'User']            

                keys_adjusment = [
                'No',
                'Date',
                'Reference',
                'Location',
                'PLTID',
                'Material',
                'Material Description',
                'Batch',
                'Uom',
                'Qty',
                'Remarks'
                ]

                keys_outbound=[
                'No',
                'Shipped Data',
                'Document No',
                'Shipper',
                'Nopol',
                'PLTID',
                'Location',
                'Material',
                'Material Description',
                'Batch',
                'Qty',
                'Uom',
                'Remarks',
                'User'
                ]

                keys_inventory=[
                        "No",
                "Receive Date",
                "Location",
                "PLTID",
                "Material",
                "Material Description",
                "Batch",
                "Uom",
                "Unrestricted",
                "Quality Inspection",
                "Blocked",
                "Transit and Transfer",
                "Stock in Transit",
                "Remarks",
                "Downloads"
                ]

                keys_qty=[
                    'type_entity',
                    'qty_total_control',
                ]


                # convert list to data

                data_dicts_qty = [dict(zip(keys_qty, row)) for row in self.data_qty]
                data_dicts_inv =  [dict(zip(keys_inventory, row)) for row in self.data_inventory_from_inbound]
                # data_dicts_inv=  [dict(zip(keys_inventory, row)) for row in inv_r]
                data_dicts_in  =  [dict(zip(keys_inbound, row)) for row in inb_r]
                data_dicts_out = [dict(zip(keys_outbound, row)) for row in out_r]
                data_dicts_adj = [dict(zip(keys_adjusment, row)) for row in adj_r]


                self.model.delete_all_rows_adjusment()
                self.model.delete_all_rows_inventory()
                self.model.delete_all_rows_outbound()
                self.model.delete_all_rows_inbound()

                self.model.insert_data_in(data_dicts_in)
                self.model.insert_data_adj(data_dicts_adj)
                self.model.insert_data_out(data_dicts_out)
                self.model.insert_data_inv(data_dicts_inv)


                self.data_inv = self.model.update_inventory_temp()
                # print(self.data_inv)
                self.data_new_inv = []
                for dataku in self.data_inv:
                    if  dataku[8]>=float(0.1):
                        self.data_new_inv.append(dataku)

                    else:

                        pass

                # inv_r,inv_qty = self.get_inventory()
                # self.model.delete_value(inv_r,self)
                # import pdb 
                # pdb.set_trace()
                # self.data_new_inv=self.data_inv

                self.model.write_value(self.data_new_inv,self)

                # updating qty of data
                self.model.update_data(data_dicts_qty)


            # except:
            #     print('error')

    def controller_app(self,view):
        self.view = view
        print('activate is running')
        # if self.view.label_activate.text == 'unactivate':
        # elif self.view.label_activate.text =='activate':

        if self.view.label_activate.text == 'unactivate' or self.view.label_activate.text == '':
            self.thread1 = threading.Thread(target = self.thread_while,args=())
            self.thread1.start()
            self.view.label_activate.text='activate'
            self.view.button_activate.text = 'Stop'
        
        else :
            self.view.label_activate.text='unactivate'
            self.view.button_activate.text = 'Start'

            self.thread1.join()

        pass