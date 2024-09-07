from Model.base_model import BaseScreenModel
from sqlalchemy.orm import Session
import os
from Model.sqlalchemy.base_sqlite import OutboundTemp,InboundTemp,AdjustmentTemp,InventoryTemp,ControlQty
from sqlalchemy import insert,create_engine, Column, Integer, String, func,or_,and_,update,delete,select
from sqlalchemy import text,Text, REAL, MetaData
from Model.sqlalchemy.gsheet_connect import ActivateSheet
from Model.sqlalchemy.base_sqlite import Base
from sqlalchemy import Column,Sequence, Integer, String, MetaData, Table
from sqlalchemy.exc import NoResultFound
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
#   this function relate with gsheet

    def create_table_temp(self):
        # self.data = ()
        return
    
    def get_adjustment(self,gsheet):
        self.gsheet=gsheet

        self.data = ActivateSheets(self.gsheet)
        return self.data.get_adjustment()
    
    def get_outbound(self,gsheet):
        self.gsheet=gsheet
        self.data = ActivateSheets(self.gsheet)
        return self.data.get_outbound()
    
    def get_inventory(self,gsheet):
        self.gsheet=gsheet
        self.data = ActivateSheets(self.gsheet)
        return self.data.get_inventory()
    
    def get_inbound(self,gsheet):
        self.gsheet=gsheet
        self.data = ActivateSheets(self.gsheet)
        return self.data.get_inbound()
    
    def write_value(self,data,gsheet):
        self.datas = data
        self.gsheet = gsheet
        self.data = ActivateSheets(self.gsheet)
        return self.data.write_value(self.datas)

    def delete_value(self,data,gsheet):
        self.datas = data
        self.gsheet = gsheet
        self.data = ActivateSheets(self.gsheet)
        return self.data.delete_value(self.datas)

    def insert_data_in(self,id):
        self.id = id
        self.data = InBoundTemps()
        return self.data.insert_data(self.id)
    
    def delete_all_rows_inbound(self): 
        # self.id = id 
        self.data =InBoundTemps()
        return self.data.delete_all_rows()
    
    def delete_all_rows_adjusment(self):
        self.data = AdjustmentTemps()
        return self.data.delete_all_rows()

    def delete_all_rows_inventory(self):
        self.data = InventoryTemps()
        return self.data.delete_all_rows()

    def delete_all_rows_outbound(self):
        self.data = OutboundTemps()
        return self.data.delete_all_rows()

#   below function is for controlling qty

    def get_qty_by(self):
        # self.id = id 
        self.data = ControlQtys()
        return self.data.get_qty_by()
        # pass

    def insert_qty_by(self,data):
        self.datas=data


    def delete(self):
        pass 

   
    def update_inventory_temp(self):
        self.data = InventoryTemps()
        return self.data.query_all_inv_in_ou_ad()
    
    def add_outbound(self):
        self.data = OutboundTemps()

        return self.data.add()

    def select(self):
        pass

    def add_inbound(self):
        self.data=InBoundTemps()
        return self.data.add()
    
    def add_adjustment(self):
        self.data=AdjustmentTemps()
        return self.data.add()
    
    def insert_data_adj(self,data):
        self.datas = data
        self.data = AdjustmentTemps()
        return self.data.insert_data(self.datas)

    def insert_data_inv(self,data):
        self.datas = data 
        self.data = InventoryTemps()
        return self.data.insert_data(self.datas)
    
    def insert_data_out(self,data):
        self.datas=data
        self.data = OutboundTemps()
        return self.data.insert_data(self.datas)

    def add_inventory(self):
        self.data=InventoryTemps()
        return self.data.add()
    
    def update_data(self,data):
        self.datas=data
        self.data = ControlQtys()
        return self.data.update(self.datas)
    
    def sum_qty_inventory(self):
        self.data = InventoryTemps()
        return self.data.sum_qty()
    
    def query_all_inv_in_ou_ad(self):
        self.data = InventoryTemps()
        return self.data.query_all_inv_in_ou_ad()    
    
    # below is the crow from Outbound_temp
    def delete_adjusment(self):
        self.data = AdjustmentTemps()
        return self.data.delete_adjusment_temp()
    
    def add_outbound(self,id):
        self.id = id
        self.data = OutboundTemps()
        self.data.get_session()
        return self.data.create_outbound_temp(self,self.data.get_session(),self.id)


class ActivateSheets(ActivateSheet):
    
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.SPREADSHEET_ID = self.parent.view.textfield_id.text 
    

class Engine():

    def __init__(self):
        self.path_db = os.path.join('Model','sqlalchemy','tes.db')
        
        self.url = f'sqlite:///{self.path_db}'
        self.engine = create_engine(self.url)
        pass


class OutboundTemps(Engine):

    def __init__(self):
        super().__init__()
        # self.engine=Engine()
        self.session = Session(self.engine)

    def update(self):
        stmt = ""

    def add(self):
        data=[]

        with self.session as sess:
            
            for i in range(1000000):
                stmt = OutboundTemp()
                data.append(stmt)
                i=i+1
            
            sess.add_all(data)

            sess.commit()

    # AI Approach
    def get_session(self):
        self.session = Session(self.engine)
        # return SessionLocal() 
        return self.session

    def create_outbound_temp(self,session, outbound_temp_data):
        outbound_temp = OutboundTemp(**outbound_temp_data)
        session.add(outbound_temp)
        session.commit()
        session.refresh(outbound_temp)
        return outbound_temp

    def read_outbound_temp(self,session, id_outbound):
        try:
            return session.query(OutboundTemp).filter(OutboundTemp.id_outbound == id_outbound).one()
        except NoResultFound:
            return None

    def update_outbound_temp(self,session, id_outbound, updated_data):
        outbound_temp = self.read_outbound_temp(session, id_outbound)
        if outbound_temp:
            for key, value in updated_data.items():
                setattr(outbound_temp, key, value)
            session.commit()
            session.refresh(outbound_temp)
        return outbound_temp

    def delete_outbound_temp(self,session, id_outbound):
        outbound_temp = self.read_outbound_temp(session, id_outbound)
        if outbound_temp:
            session.delete(outbound_temp)
            session.commit()
        return outbound_temp

    def insert_data(self,data):
        self.datas = data
        for dat in self.datas :
    
            self.session=Session(self.engine)
            self.stmt=text(""" INSERT INTO outbound_temp (
                              No,
                              [Shipped Data],
                              [Document No],
                              Shipper,
                              Nopol,
                              PLTID,
                              Location,
                              Material,
                              [Material Description],
                              Batch,
                              Qty,
                              Uom,
                              Remarks,
                              User
                          )
                          VALUES (
                              :No,
                              :Shipped_Data,
                              :Document_No,
                              :Shipper,
                              :Nopol,
                              :PLTID,
                              :Location,
                              :Material,
                              :Material_Description,
                              :Batch,
                              :Qty,
                              :Uom,
                              :Remarks,
                              :User
                          );

            """)
                                    
                                
    
            self.params = { "No" :dat.get('No'),
                            "Shipped_Data": dat.get('Shipped Data'),
                            "Document_No": dat.get('Document No'),
                            "Shipper":dat.get('Shipper'),
                            "Nopol":dat.get('Nopol'),
                            "PLTID":dat.get('PLTID'),
                            "Location":dat.get('Location'),
                            "Material":dat.get('Material'),
                            "Material_Description":dat.get('Material Description'),
                            "Batch":dat.get('Batch'),
                            "Qty":dat.get('Qty'),
                            "Uom":dat.get('Uom'),
                            "Remarks":dat.get('Remarks'),
                            "User":dat.get('User'),
            }
            self.session.execute(self.stmt,self.params)
            self.session.commit()
            self.session.close()

    def delete_all_rows(self):
        self.session = Session(self.engine)
        # Delete all rows from the table
        self.session.query(OutboundTemp).delete()
        self.session.commit()
        print("All rows deleted.")


class InBoundTemps(Engine):

    def __init__(self):
        super().__init__()
        self.session=Session(self.engine)
    
    def add(self):
        data=[]

        with self.session as sess:
            
            for i in range(1000000):
                stmt = InboundTemp()
                data.append(stmt)
                i=i+1
            
            sess.add_all(data)

            sess.commit()

    def delete_all_rows(self):
        # self.data=data
        self.session = Session(self.engine)
        # Delete all rows from the table
        self.session.query(InboundTemp).delete()
        self.session.commit()
        print("All rows deleted.")

    def insert_data(self,data):
        self.datas = data
        for dat in self.datas :
            self.session=Session(self.engine)
            self.stmt=text(""" INSERT INTO inbound_temp (
                                Header,
                                No,
                                [Receive Date],
                                [Document No],
                                Consigne,
                                Nopol,
                                Material,
                                [Material Description],
                                Batch,
                                [Inbound Qty],
                                Uom,
                                PLTID,
                                Location,
                                Remarks,
                                User
                            )
                            VALUES (
                                :Header,
                                :No,
                                :Receive_Date,
                                :Document_No,
                                :Consigne,
                                :Nopol,
                                :Material,
                                :Material_Description,
                                :Batch,
                                :Inbound_Qty,
                                :Uom,
                                :PLTID,
                                :Location,
                                :Remarks,
                                :User                         
                            );
            """)
                                    
                                
    
            self.params = {"Header" : dat.get('Header'),
                            "No" :dat.get('No'),
                            "Receive_Date": dat.get('Receive Date'),
                            "Document_No": dat.get('Document No'),
                            "Consigne":dat.get('Consigne'),
                            "Nopol":dat.get('Nopol'),
                            "Material":dat.get('Material'),
                            "Material_Description":dat.get('Material Description'),
                            "Batch":dat.get('Batch'),
                            "Inbound_Qty":dat.get('Inbound Qty'),
                            "Uom":dat.get('Uom'),
                            "PLTID":dat.get('PLTID'),
                            "Location":dat.get('Location'),
                            "Remarks":dat.get('Remarks'),
                            "User":dat.get('User'),
            }
            self.session.execute(self.stmt,self.params)
            self.session.commit()
            self.session.close()


class AdjustmentTemps(Engine):
    

    def __init__(self):
        super().__init__()
        self.session=Session(self.engine)
    
    def add(self):
        data = []

        with self.session as sess:
            
            for i in range(1000000):
                stmt = AdjustmentTemp()
                data.append(stmt)
                i=i+1
            
            sess.add_all(data)

            sess.commit()

    def insert_data(self,dataku):
        self.datas = dataku

        for dat in self.datas :
            self.session=Session(self.engine)
            self.stmt=text(""" INSERT INTO adjustment_temp (
                                No,
                                Date,
                                Refference,
                                Location,
                                PLTID,
                                Material,
                                [Material Description],
                                batch,
                                Uom,
                                Qty,
                                Remarks
                            )
                            VALUES (
                                :No,
                                :Date,
                                :Refference,
                                :Location,
                                :PLTID,
                                :Material,
                                :Material_Description,
                                :batch,
                                :Uom,
                                :Qty,
                                :Remarks                     
                            );
            """)
                                    
                            
            self.params = { "No" :dat.get('No'),
                            "Date": dat.get('Date'),
                            "Refference": dat.get('Refference'),
                            "Location":dat.get('Location'),
                            "PLTID":dat.get('PLTID'),
                            "Material":dat.get('Material'),
                            "Material_Description":dat.get('Material Description'),
                            "batch":dat.get('Batch'),
                            "Uom":dat.get('Uom'),
                            "Qty":dat.get('Qty'),
                            "Remarks":dat.get('Remarks'),
            }
            self.session.execute(self.stmt,self.params)
            self.session.commit()
            self.session.close()

    def delete_all_rows(self):
        self.session = Session(self.engine)
        # Delete all rows from the table
        self.session.query(AdjustmentTemp).delete()
        self.session.commit()
        print("All rows deleted.")

    def get_session(self):
        self.session = Session(self.engine)
        # return SessionLocal() 
        return self.session

    def create_adjusment_temp(self,session, adjusment_temp_data):
        adjusment_temp = OutboundTemp(**adjusment_temp_data)
        session.add(adjusment_temp)
        session.commit()
        session.refresh(adjusment_temp)
        return adjusment_temp

    def read_adjusment_temp(self,session, id_adjusment):
        try:
            return session.query(AdjustmentTemp).filter(AdjustmentTemp.id == id_adjusment).one()
        except NoResultFound:
            return None

    def update_adjusment_temp(self,session, id_adjusment, updated_data):
        adjusment_temp = self.read_outbound_temp(session, id_adjusment)
        if adjusment_temp:
            for key, value in updated_data.items():
                setattr(adjusment_temp, key, value)
            session.commit()
            session.refresh(adjusment_temp)
        return adjusment_temp

    def delete_adjusment_temp(self,session, id_adjusment):
        outbound_temp = self.read_adjusment_temp(session, id_adjusment)
        if outbound_temp:
            session.delete(outbound_temp)
            session.commit()
        return outbound_temp


class InventoryTemps(Engine):

    def __init__(self):
        super().__init__()

    def add(self):
        self.session = Session(self.engine)
        data=[]
        
        with self.session as sess:
            
            for i in range(1000000):
                stmt = InventoryTemp()
                data.append(stmt)
                i=i+1
            
            sess.add_all(data)

            sess.commit()
        
    def sum_qty(self):
        self.session = Session(self.engine)
        print('hh')
        # with self.session as sess:
        stmt = self.session.query(InventoryTemp.Receive_Date,func.sum(InventoryTemp.Unrestricted).label('Total Qty')).group_by(and_(InventoryTemp.PLTID,InventoryTemp.Location,InventoryTemp.Material,InventoryTemp.Batch))

        results = stmt.all()
        for result in results:
            print (result)
        
        self.session.close()

    def update_by(self,id,data):

        self.data = data 
        self.id=id

        print('updating')
        k = 1
        print(k)

        for i in range(1000000):
            self.session = Session(self.engine)
            stmt = update(InventoryTemp).where(and_
                (InventoryTemp.id_inventory==k)).values({InventoryTemp.No:k})
                #                                                   ,
                # InventoryTemp.Receive_Date,InventoryTemp.Location,InventoryTemp.PLTID,
                # InventoryTemp.Material,InventoryTemp.Material_Description,InventoryTemp.Batch,
                # InventoryTemp.Uom,InventoryTemp.Unrestricted,InventoryTemp.Quality_Inspection,
                # InventoryTemp.Blocked,InventoryTemp.Transit_and_Transfer,InventoryTemp.Stock_in_Transit,
                # InventoryTemp.Remarks,InventoryTemp.Downloads)
            result = self.session.execute(stmt)
            k=k+1
            self.session.commit()
            self.session.close()

    def query_all_inv_in_ou_ad(self,id=None,data=None):
        self.id = id 
        self.data=data
        self.session=Session(self.engine)
        # stmt =text("""SELECT inventory_temp.PLTID||inventory_temp.Location||inventory_temp.Material||inventory_temp.Batch,
        # outbound_temp.PLTID||outbound_temp.Location||outbound_temp.Material||outbound_temp.Batch
        # FROM inventory_temp
        # Inner join outbound_temp on  inventory_temp.id_inventory = outbound_temp.id_outbound""")
        # where inventory_temp.Location||inventory_temp.Material||inventory_temp.Batch =
        # outbound_temp.Location||outbound_temp.Material||outbound_temp.Batch 
        # """
        stmt = text(
"""
Select
    inventory_temp.No,
    inventory_temp."Receive Date",
    inventory_temp.Location,
    inventory_temp.PLTID,
    inventory_temp.Material,
    inventory_temp."Material Description",
    inventory_temp.Batch,
    inventory_temp.Uom,
    (COALESCE(d.suminv,0)+COALESCE(r.sumadj,0)-COALESCE(k.sumout,0)) as refixinv,
    inventory_temp."Quality Inspection",
    inventory_temp.Blocked,
    inventory_temp."Transit and Transfer",
    inventory_temp."Stock in Transit",
    inventory_temp.Remarks,
    inventory_temp.Downloads, 
    inventory_temp.PLTID||inventory_temp.Location||inventory_temp.Material||inventory_temp.Batch as invb
       
  FROM inventory_temp

Left join (select *
from(
select  outbound_temp.PLTID||outbound_temp.Location||outbound_temp.Material||outbound_temp.Batch as outb
        ,sum(outbound_temp.Qty) as sumout
from outbound_temp
group by outb)) k on invb = k.outb


Left join (select *
from(
select  inbound_temp.PLTID||inbound_temp.Location||inbound_temp.Material||inbound_temp.Batch as inb
        ,sum(inbound_temp."Inbound Qty") as suminv
from inbound_temp
group by inb))  d on invb=d.inb 

    
Left join (select *
from(
select  adjustment_temp.PLTID||adjustment_temp.Location||adjustment_temp.Material||adjustment_temp.Batch as adjb
        ,sum(adjustment_temp.Qty) as sumadj
from adjustment_temp
group by adjb)) r on invb=r.adjb

where inventory_temp."Receive Date" is not Null

"""
        )
        results = self.session.execute(stmt).fetchall()
        self.result = []
        for result in results :
            print(result)
            self.result.append(result)
        self.session.commit()
        self.session.close()
        print(results)
    
        return self.result


    def get_session(self):
        self.session = Session(self.engine)
        # return SessionLocal() 
        return self.session

    def create_inventory_temp(self,session, inventory_temp_data):
        inventory_temp = InventoryTemp(**inventory_temp_data)
        session.add(inventory_temp)
        session.commit()
        session.refresh(inventory_temp)
        return inventory_temp

    def read_adjusment_temp(self,session, id_inventory):
        try:
            return session.query(InventoryTemp).filter(InventoryTemp.id_inventory == id_inventory).one()
        except NoResultFound:
            return None

    def update_inventory_temp(self,session, id_inventory, updated_data):
        inventory_temp = self.read_inventory_temp(session, id_inventory)
        if inventory_temp:
            for key, value in updated_data.items():
                setattr(inventory_temp, key, value)
            session.commit()
            session.refresh(inventory_temp)
        return inventory_temp

    def delete_adjusment_temp(self,session, id_adjusment):
        outbound_temp = self.read_adjusment_temp(session, id_adjusment)
        if outbound_temp:
            session.delete(outbound_temp)
            session.commit()
        return outbound_temp

    def delete_all_rows(self):
        # self.data=data
        self.session = Session(self.engine)
        # Delete all rows from the table
        self.session.query(InventoryTemp).delete()
        self.session.commit()
        print("All rows deleted.")

    def insert_data(self,dataku):
        self.datas = dataku

        for dat in self.datas :
            self.session=Session(self.engine)
            self.stmt=text(""" INSERT INTO inventory_temp (
                               No,
                               [Receive Date],
                               Location,
                               PLTID,
                               Material,
                               [Material Description],
                               Batch,
                               Uom,
                               Unrestricted,
                               [Quality Inspection],
                               Blocked,
                               [Transit and Transfer],
                               [Stock in Transit],
                               Remarks,
                               Downloads
                           )
                           VALUES (
                               :No,
                               :Receive_Date,
                               :Location,
                               :PLTID,
                               :Material,
                               :Material_Description,
                               :Batch,
                               :Uom,
                               :Unrestricted,
                               :Quality_Inspection,
                               :Blocked,
                               :Transit_and_Transfer,
                               :Stock_in_Transit,
                               :Remarks,
                               :Downloads
                           );
            """)
                                    
                            
            self.params = { "No" :dat.get('No'),
                            "Receive_Date": dat.get('Receive Date'),
                            "Location":dat.get('Location'),
                            "PLTID":dat.get('PLTID'),
                            "Material":dat.get('Material'),
                            "Material_Description":dat.get('Material Description'),
                            "Batch":dat.get('Batch'),
                            "Uom":dat.get('Uom'),
                            "Unrestricted":dat.get('Unrestricted'),
                            "Quality_Inspection":dat.get('Quality_Inspection'),
                            "Blocked":dat.get('Blocked'),
                            "Transit_and_Transfer":dat.get('Transit_and_Transfer'),
                            "Stock_in_Transit":dat.get('Stock_in_Transit'),
                            "Remarks":dat.get('Remarks'),
                            "Downloads":dat.get('Downloads'),
            }
            self.session.execute(self.stmt,self.params)
            self.session.commit()
            self.session.close()


class ControlQtys(Engine):

    def __init__(self):
        super().__init__()

    def get_qty_by(self):
        # self.id = id
        self.session=Session(self.engine)

        stmt = select(ControlQty.qty_total_control,ControlQty.type_entity)
        # .where(ControlQty.type_entity.ilike(f'%{self.id}%'))
        add_list = []
        add_data = []
        results = self.session.execute(stmt).all()
        for result in results:
            add_list.append(result[0])
        # result = result[0]
        self.session.close()
        # import pdb 
        # pdb.set_trace()
        return add_list
    
    def update(self,data):
        self.datas = data 

        for dat in self.datas :
            self.session=Session(self.engine)
            
            self.stmt=text(""" UPDATE control_qty
                            SET qty_total_control = :qty_total_control
                            WHERE 
                                type_entity = :type_entity  
            """)
                                    
                            
            self.params = { "qty_total_control" :dat.get('qty_total_control'),
                            "type_entity": dat.get('type_entity'),
                            }
            self.session.execute(self.stmt,self.params)
            self.session.commit()
            self.session.close()

# class Temp_table(Engine):


#     def __init__(self):
#         super().__init__()
#         self.connect = self.engine.connect()
#         self.Meta_data = MetaData(bind=self.connect)
#         self.temp_table = Table(
            



# Define the base class for the ORM models
# Base = declarative_base()

# Define the InboundTemp class
# class InboundTemp(Base):
#     __tablename__ = 'inbound_temp'

#     id_inbound = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     Header = Column(Text)
#     No = Column(Integer)
#     Receive_Date = Column(Integer)
#     Document_No = Column(Text)
#     Consigne = Column(Text)
#     Nopol = Column(Text)
#     Material = Column(Text)
#     Material_Description = Column(Text)
#     Batch = Column(Text)
#     Inbound_Qty = Column(REAL)
#     Uom = Column(Text)
#     PLTID = Column(Integer)
#     Location = Column(Text)
#     Remarks = Column(Text)
#     User = Column(Text)

#     # Create an engine that stores data in the local directory's autocompute.db file
#     engine = create_engine('sqlite:///autocompute.db')

#     # Create all tables in the engine
#     Base.metadata.create_all(engine)

#     # Create a configured "Session" class
#     Session = sessionmaker(bind=engine)

#     # Create a session
#     session = Session()

#     def add_record(self):
#     # Example: Add a new inbound_temp record
#         self.new_record = InboundTemp(
#             Header='Example Header',
#             No=1,
#             Receive_Date=20230721,
#             Document_No='DOC123',
#             Consigne='Consignee Name',
#             Nopol='NOPOL123',
#             Material='Material1',
#             Material_Description='Material Description',
#             Batch='BATCH1',
#             Inbound_Qty=100.0,
#             Uom='kg',
#             PLTID=123,
#             Location='Location1',
#             Remarks='Remarks',
#             User='User1'
#         )

#         # Add the record to the session
#         self.session.add(new_record)

#         # Commit the record to the database
#         self.session.commit()

#         # Close the session
#         self.session.close()