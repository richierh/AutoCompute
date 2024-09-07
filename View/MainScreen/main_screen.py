from View.base_screen import BaseScreenView
from kivy.clock import Clock
import threading


class MainScreenView(BaseScreenView):


    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """


    def cek(self,*args):
        print('hello')
        for i in range(2):
            self.controller.query_all_inv_in_ou_ad()
            print(i)

    def close(self):
        # self.app.stop()
        pass

    def activate(self):
        # self.controller.get_adjustment()
        self.controller.controller_app(self)
        # self.controller.delete_all_rows()

        # while inbound_sum != gsheetinbound_inbound_sum or outbound_sum != gsheetoutbound_outbound_sum: or adjustment_sum != gsheetdjja
        

            # self.controller.add_outbound()
            # self.controller.add_inbound()
            # self.controller.add_adjustment()
            # self.controller.sum_qty_inventory()
            # self.controller.add_inventory()

        # def cek(*args):
        #     print('hello')
        #     for i in range(2):
        #         self.controller.query_all_inv_in_ou_ad()
        #         print(i)
        
        # t1.join()
        # Clock.schedule_once(self.cek,1)

        

        # id=1
        # self.id= str(1)
        # self.data = ["dfdf"]
        # self.controller.update_inventory_temp(self.id,self.data)

        # if self.label_activate.text=='unactivate':
        #     self.label_activate.text='active'
        #     self.t1 = threading.Thread(target=self.cek)
        #     self.t1.start()

        # else:
        #     self.t2 = threading.Thread(target=self.close)
        #     # self.t2.join()
        #     self.t1.join()
        #     self.app.get_running_app().stop()
        #     # self.t2.join()
        #     # self.t1.join()
        #     self.label_activate.text='unactivate'
        #     # self.app.get_running_app().stop()
        #     # import pdb 
        #     # pdb.set_trace()
