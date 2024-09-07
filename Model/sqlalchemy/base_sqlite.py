from typing import Optional

from sqlalchemy import Float, Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class AdjustmentTemp(Base):
    __tablename__ = 'adjustment_temp'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    No: Mapped[Optional[int]] = mapped_column(Integer)
    Date: Mapped[Optional[int]] = mapped_column(Integer)
    Refference: Mapped[Optional[str]] = mapped_column(Text)
    Location: Mapped[Optional[str]] = mapped_column(Text)
    PLTID: Mapped[Optional[int]] = mapped_column(Integer)
    Material: Mapped[Optional[str]] = mapped_column(Text)
    Material_Description: Mapped[Optional[str]] = mapped_column('Material Description', Text)
    batch: Mapped[Optional[str]] = mapped_column(Text)
    Uom: Mapped[Optional[str]] = mapped_column(Text)
    Qty: Mapped[Optional[float]] = mapped_column(Float)
    Remarks: Mapped[Optional[str]] = mapped_column(Text)


class ControlQty(Base):
    __tablename__ = 'control_qty'

    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    type_entity: Mapped[Optional[str]] = mapped_column(Text)
    qty_total_control: Mapped[Optional[int]] = mapped_column(Integer)


class InboundTemp(Base):
    __tablename__ = 'inbound_temp'

    id_inbound: Mapped[int] = mapped_column(Integer, primary_key=True)
    Header: Mapped[Optional[str]] = mapped_column(Text)
    No: Mapped[Optional[int]] = mapped_column(Integer)
    Receive_Date: Mapped[Optional[int]] = mapped_column('Receive Date', Integer)
    Document_No: Mapped[Optional[str]] = mapped_column('Document No', Text)
    Consigne: Mapped[Optional[str]] = mapped_column(Text)
    Nopol: Mapped[Optional[str]] = mapped_column(Text)
    Material: Mapped[Optional[str]] = mapped_column(Text)
    Material_Description: Mapped[Optional[str]] = mapped_column('Material Description', Text)
    Batch: Mapped[Optional[str]] = mapped_column(Text)
    Inbound_Qty: Mapped[Optional[float]] = mapped_column('Inbound Qty', Float)
    Uom: Mapped[Optional[str]] = mapped_column(Text)
    PLTID: Mapped[Optional[int]] = mapped_column(Integer)
    Location: Mapped[Optional[str]] = mapped_column(Text)
    Remarks: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[str]] = mapped_column(Text)


class InventoryTemp(Base):
    __tablename__ = 'inventory_temp'

    id_inventory: Mapped[int] = mapped_column(Integer, primary_key=True)
    No: Mapped[Optional[int]] = mapped_column(Integer)
    Receive_Date: Mapped[Optional[int]] = mapped_column('Receive Date', Integer)
    Location: Mapped[Optional[str]] = mapped_column(Text)
    PLTID: Mapped[Optional[int]] = mapped_column(Integer)
    Material: Mapped[Optional[str]] = mapped_column(Text)
    Material_Description: Mapped[Optional[str]] = mapped_column('Material Description', Text)
    Batch: Mapped[Optional[str]] = mapped_column(Text)
    Uom: Mapped[Optional[str]] = mapped_column(Text)
    Unrestricted: Mapped[Optional[float]] = mapped_column(Float)
    Quality_Inspection: Mapped[Optional[int]] = mapped_column('Quality Inspection', Integer)
    Blocked: Mapped[Optional[int]] = mapped_column(Integer)
    Transit_and_Transfer: Mapped[Optional[int]] = mapped_column('Transit and Transfer', Integer)
    Stock_in_Transit: Mapped[Optional[int]] = mapped_column('Stock in Transit', Integer)
    Remarks: Mapped[Optional[str]] = mapped_column(Text)
    Downloads: Mapped[Optional[str]] = mapped_column(Text)


class OutboundTemp(Base):
    __tablename__ = 'outbound_temp'

    id_outbound: Mapped[int] = mapped_column(Integer, primary_key=True)
    No: Mapped[Optional[int]] = mapped_column(Integer)
    Shipped_Data: Mapped[Optional[int]] = mapped_column('Shipped Data', Integer)
    Document_No: Mapped[Optional[str]] = mapped_column('Document No', Text)
    Shipper: Mapped[Optional[str]] = mapped_column(Text)
    Nopol: Mapped[Optional[str]] = mapped_column(Text)
    PLTID: Mapped[Optional[int]] = mapped_column(Integer)
    Location: Mapped[Optional[str]] = mapped_column(Text)
    Material: Mapped[Optional[str]] = mapped_column(Text)
    Material_Description: Mapped[Optional[str]] = mapped_column('Material Description', Text)
    Batch: Mapped[Optional[str]] = mapped_column(Text)
    Qty: Mapped[Optional[float]] = mapped_column(Float)
    Uom: Mapped[Optional[str]] = mapped_column(Text)
    Remarks: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[str]] = mapped_column(Text)


class SpreadsheetTableTemp(Base):
    __tablename__ = 'spreadsheet_table_temp'

    id_spread: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(Text)
    status: Mapped[Optional[int]] = mapped_column(Integer)
