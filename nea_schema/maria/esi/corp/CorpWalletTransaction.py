from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import \
    BIGINT as BigInt, \
    BOOLEAN as Boolean, \
    DATETIME as DateTime, \
    DOUBLE as Double, \
    INTEGER as Integer, \
    TEXT as Text, \
    TINYINT as TinyInt, \
    TINYTEXT as TinyText

from ...Base import Base

class CorpWalletTransaction(Base):    
    __tablename__ = 'corp_WalletTransaction'
    
    ## Columns
    record_time = Column(DateTime)
    etag = Column(TinyText)
    client_id = Column(BigInt(unsigned=True))
    date = Column(DateTime)
    division = Column(TinyInt(unsigned=True))
    is_buy = Column(Boolean)
    journal_ref_id = Column(BigInt(unsigned=True))
    location_id = Column(BigInt(unsigned=True))
    quantity = Column(BigInt(unsigned=True))
    transaction_id = Column(BigInt(unsigned=True), primary_key=True, autoincrement=False)
    type_id = Column(Integer(unsigned=True), ForeignKey('inv_Type.type_id'))
    unit_price = Column(Double(unsigned=True))
    
    ## Relationships
    type = relationship('Type')
    journal = relationship(
        'CorpWalletJournal',
        primaryjoin='CorpWalletTransaction.journal_ref_id == foreign(CorpWalletJournal.journal_id)',
        viewonly=True, uselist=False,
    )

    @classmethod
    def esi_parse(cls, esi_return, division):
        class_obj = [cls(**{
            'record_time': dt.strptime(esi_return.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z'),
            'etag': esi_return.headers.get('Etag'),
            'client_id': row.get('client_id'),
            'date': dt.strptime(row.get('date'), '%Y-%m-%dT%H:%M:%SZ'),
            'division': division,
            'is_buy': row.get('is_buy', False),
            'journal_ref_id': row.get('journal_ref_id'),
            'location_id': row.get('location_id'),
            'quantity': row.get('quantity'),
            'transaction_id': row.get('transaction_id'),
            'type_id': row.get('type_id'),
            'unit_price': row.get('unit_price'),
        }) for row in esi_return.json()]
        return class_obj
